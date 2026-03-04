#!/usr/bin/env bash
set -euo pipefail

# Tag audit: if building a version tag vX.Y.Z.W, enforce that \docversion in
# guide.tex matches X.Y.Z.W.
if [ -n "${TRAVIS_TAG:-}" ]; then
  if printf '%s' "$TRAVIS_TAG" | grep -Eq '^v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'; then
    expected_version="${TRAVIS_TAG#v}"
    docversion="$(sed -n 's/^\\newcommand{\\docversion}{\([^}]*\)}.*/\1/p' guide.tex | head -n 1)"
    echo "Tag detected: $TRAVIS_TAG"
    echo "Expected docversion: $expected_version"
    echo "guide.tex docversion: ${docversion:-<missing>}"

    if [ -z "${docversion:-}" ]; then
      echo "Could not extract \\docversion from guide.tex"
      exit 1
    fi
    if [ "$docversion" != "$expected_version" ]; then
      echo "Version mismatch: tag is $expected_version but \\docversion is $docversion"
      exit 1
    fi
  else
    echo "Non-version tag detected ($TRAVIS_TAG); skipping version audit."
  fi
fi

# Fast path: when GitHub Actions creates the auto-sync commit that copies
# guide.pdf -> docs/guide-web.pdf, only validate that both PDFs are
# byte-identical. This avoids a redundant LaTeX build.
if printf '%s' "${TRAVIS_COMMIT_MESSAGE:-}" | grep -q "Auto-sync: Update guide-web.pdf from root"; then
  echo "Detected auto-sync commit; validating PDF copy only."

  if [ ! -f guide.pdf ]; then
    echo "Missing guide.pdf in repo root."
    exit 1
  fi
  if [ ! -f docs/guide-web.pdf ]; then
    echo "Missing docs/guide-web.pdf."
    exit 1
  fi

  sha_root_pdf="$(sha256sum guide.pdf | awk '{print $1}')"
  sha_web_pdf="$(sha256sum docs/guide-web.pdf | awk '{print $1}')"
  echo "SHA guide.pdf:      $sha_root_pdf"
  echo "SHA guide-web.pdf:  $sha_web_pdf"

  if [ "$sha_root_pdf" != "$sha_web_pdf" ]; then
    echo "docs/guide-web.pdf is not identical to guide.pdf."
    exit 1
  fi

  echo "PASS: docs/guide-web.pdf matches guide.pdf"
  exit 0
fi

python3 --version
python3 scripts/validate-tex-preamble.py

# Site consistency: the repo should contain the web PDF and the site should
# reference it. Do not enforce equality with guide.pdf here because a
# separate GitHub Actions workflow performs the sync and commits later.
if [ ! -f docs/guide-web.pdf ]; then
  echo "Missing docs/guide-web.pdf (expected for GitHub Pages)."
  exit 1
fi
if [ -f docs/index.html ] && ! grep -q 'guide-web\.pdf' docs/index.html; then
  echo "docs/index.html does not reference guide-web.pdf"
  exit 1
fi

# Alpha audit (lightweight):
# - Detect the latest alpha snapshot in wip/ (guide-vX.Y.Z.W-alpha.N[.M]-YYYYMMDD.tex)
# - Ensure we are not advertising a non-existent alpha
# - Only compile alpha when it is advertised (README/docs) OR when the alpha .tex changed
alpha_env="$(
python3 - <<'PY'
import re
from pathlib import Path

wip = Path('wip')
tex_pat = re.compile(r'^guide-(v[\d.]+-alpha\.[\d.]+)-(\d{8})\.tex$')

def sort_key(version: str, yyyymmdd: str):
    core_part, alpha_part = version[1:].split('-alpha.')
    core_nums = tuple(int(n) for n in core_part.split('.'))
    alpha_nums = tuple(int(n) for n in alpha_part.split('.'))
    return core_nums, alpha_nums, int(yyyymmdd)

candidates = []
if wip.exists():
    for f in wip.iterdir():
        if not f.is_file():
            continue
        m = tex_pat.match(f.name)
        if m:
            version, date = m.group(1), m.group(2)
            candidates.append((sort_key(version, date), version, f.name))

alpha_version = ''
alpha_tex = ''
alpha_pdf = ''
if candidates:
    candidates.sort()
    _, alpha_version, alpha_tex_name = candidates[-1]
    alpha_tex = f"wip/{alpha_tex_name}"
    expected_pdf = (wip / alpha_tex_name).with_suffix('.pdf')
    if expected_pdf.exists():
        alpha_pdf = f"wip/{expected_pdf.name}"

print(f'ALPHA_VERSION={alpha_version}')
print(f'ALPHA_TEX={alpha_tex}')
print(f'ALPHA_PDF={alpha_pdf}')
PY
)"

ALPHA_VERSION="$(printf '%s\n' "$alpha_env" | sed -n 's/^ALPHA_VERSION=//p')"
ALPHA_TEX="$(printf '%s\n' "$alpha_env" | sed -n 's/^ALPHA_TEX=//p')"
ALPHA_PDF="$(printf '%s\n' "$alpha_env" | sed -n 's/^ALPHA_PDF=//p')"

if [ -n "${ALPHA_TEX:-}" ]; then
  echo "Alpha snapshot detected: ${ALPHA_TEX} (${ALPHA_VERSION})"

  advertise_readme=0
  advertise_site=0

  if grep -q "Alpha pre-release available:" README.md; then
    advertise_readme=1
    if ! grep -q "Alpha pre-release available: ${ALPHA_VERSION}" README.md; then
      echo "README alpha footer does not match latest alpha version (${ALPHA_VERSION})."
      exit 1
    fi
  fi

  if [ -f docs/index.html ] && grep -q "Alpha ${ALPHA_VERSION}" docs/index.html; then
    advertise_site=1
    if [ -z "${ALPHA_PDF:-}" ]; then
      echo "docs/index.html references alpha ${ALPHA_VERSION} but matching alpha PDF is missing (expected ${ALPHA_TEX%.tex}.pdf)."
      exit 1
    fi
  fi

  alpha_tex_changed=0
  if [ -n "${TRAVIS_COMMIT_RANGE:-}" ]; then
    if git diff --name-only "${TRAVIS_COMMIT_RANGE}" | grep -qx "${ALPHA_TEX}"; then
      alpha_tex_changed=1
    fi
  fi

  if [ "${advertise_readme}" -eq 1 ] || [ "${advertise_site}" -eq 1 ] || [ "${alpha_tex_changed}" -eq 1 ]; then
    echo "Compiling alpha snapshot (advertised or changed)."
    latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error "${ALPHA_TEX}"
  else
    echo "Skipping alpha compilation (not advertised and alpha .tex unchanged)."
  fi
else
  if grep -q "Alpha pre-release available:" README.md; then
    echo "README advertises an alpha but no alpha snapshot exists in wip/."
    exit 1
  fi
fi

# Snapshot integrity: require exactly one active snapshot in wip/guide and it
# must be byte-identical to guide.tex.
count="$(find wip/guide -maxdepth 1 -type f -name '*.tex' | wc -l | tr -d ' ')"
if [ "$count" -ne 1 ]; then
  echo "Expected exactly 1 snapshot in wip/guide, found $count"
  find wip/guide -maxdepth 1 -type f -name '*.tex' -print
  exit 1
fi

snapshot="$(find wip/guide -maxdepth 1 -type f -name '*.tex' -print -quit)"
sha_snapshot="$(sha256sum "$snapshot" | awk '{print $1}')"
sha_root_tex="$(sha256sum guide.tex | awk '{print $1}')"

echo "Snapshot: $snapshot"
echo "SHA snapshot: $sha_snapshot"
echo "SHA root tex: $sha_root_tex"

if [ "$sha_snapshot" != "$sha_root_tex" ]; then
  echo "guide.tex does not match the active snapshot in wip/guide."
  exit 1
fi

# Build guide.pdf (multiple passes for TOC/refs); run twice to ensure the
# custom HOTAS list file (guide.hotas) is fully updated.
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error guide.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error guide.tex
