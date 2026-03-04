#!/usr/bin/env bash
set -euo pipefail

fold_start() {
  # Travis fold markers make logs easier to navigate in the web UI.
  # The API log endpoint shows these markers verbatim.
  local name="$1"
  local title="${2:-$1}"
  printf 'travis_fold:start:%s\n' "$name"
  echo "==> $title"
}

fold_end() {
  local name="$1"
  printf 'travis_fold:end:%s\n' "$name"
}

die() {
  echo "ERROR: $*" >&2
  exit 1
}

run_folded() {
  # Usage: run_folded <fold_name> <title> <command...>
  local fold_name="$1"
  local title="$2"
  shift 2
  fold_start "$fold_name" "$title"

  if "$@"; then
    fold_end "$fold_name"
    return 0
  fi

  local exit_code=$?
  echo "Command failed (exit $exit_code): $*" >&2
  fold_end "$fold_name"
  exit "$exit_code"
}

run_folded_capture() {
  # Usage: run_folded_capture <fold_name> <title> <log_label> <command...>
  # Captures stdout/stderr so logs stay short; on failure prints last lines.
  local fold_name="$1"
  local title="$2"
  local log_label="$3"
  shift 3

  local tmp
  tmp="$(mktemp)"

  fold_start "$fold_name" "$title"
  if "$@" >"$tmp" 2>&1; then
    echo "PASS: $log_label"
    fold_end "$fold_name"
    rm -f "$tmp"
    return 0
  fi

  local exit_code=$?
  echo "FAIL: $log_label (exit $exit_code)" >&2
  echo "--- last 120 lines (${log_label}) ---" >&2
  tail -n 120 "$tmp" >&2 || true
  fold_end "$fold_name"
  rm -f "$tmp"
  exit "$exit_code"
}

# Tag audit: if building a version tag vX.Y.Z.W, enforce that \docversion in
# guide.tex matches X.Y.Z.W.
run_folded tag_audit "Tag audit" bash -lc '
  if [ -n "${TRAVIS_TAG:-}" ]; then
    if printf "%s" "$TRAVIS_TAG" | grep -Eq "^v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$"; then
      expected_version="${TRAVIS_TAG#v}"
      docversion="$(sed -n "s/^\\\\newcommand{\\\\docversion}{\\([^}]*\\)}.*/\\1/p" guide.tex | head -n 1)"
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
      echo "PASS: tag matches \\docversion"
    else
      echo "Non-version tag detected ($TRAVIS_TAG); skipping version audit."
    fi
  else
    echo "No tag; skipping version audit."
  fi
'

# Fast path: when GitHub Actions creates the auto-sync commit that copies
# guide.pdf -> docs/guide-web.pdf, only validate that both PDFs are
# byte-identical. This avoids a redundant LaTeX build.
if printf '%s' "${TRAVIS_COMMIT_MESSAGE:-}" | grep -q "Auto-sync: Update guide-web.pdf from root"; then
  fold_start autosync "Auto-sync commit: validate PDF copy only"
  echo "Detected auto-sync commit; validating PDF copy only."

  [ -f guide.pdf ] || die "Missing guide.pdf in repo root."
  [ -f docs/guide-web.pdf ] || die "Missing docs/guide-web.pdf."

  sha_root_pdf="$(sha256sum guide.pdf | awk '{print $1}')"
  sha_web_pdf="$(sha256sum docs/guide-web.pdf | awk '{print $1}')"
  echo "SHA guide.pdf:      $sha_root_pdf"
  echo "SHA guide-web.pdf:  $sha_web_pdf"

  if [ "$sha_root_pdf" != "$sha_web_pdf" ]; then
    die "docs/guide-web.pdf is not identical to guide.pdf."
  fi

  echo "PASS: docs/guide-web.pdf matches guide.pdf"
  fold_end autosync
  exit 0
fi

run_folded python "Python + preamble validation" bash -lc '
  python3 --version
  python3 scripts/validate-tex-preamble.py
'

# Site consistency: the repo should contain the web PDF and the site should
# reference it. Do not enforce equality with guide.pdf here because a
# separate GitHub Actions workflow performs the sync and commits later.
run_folded site "Site consistency checks" bash -lc '
  if [ ! -f docs/guide-web.pdf ]; then
    echo "Missing docs/guide-web.pdf (expected for GitHub Pages)."
    exit 1
  fi
  if [ -f docs/index.html ] && ! grep -q "guide-web\\.pdf" docs/index.html; then
    echo "docs/index.html does not reference guide-web.pdf"
    exit 1
  fi
  echo "PASS: docs/guide-web.pdf present; index reference OK (if index exists)"
'

# Alpha audit (lightweight):
# - Detect the latest alpha snapshot in wip/ (guide-vX.Y.Z.W-alpha.N[.M]-YYYYMMDD.tex)
# - Ensure we are not advertising a non-existent alpha
# - Only compile alpha when it is advertised (README/docs) OR when the alpha .tex changed
fold_start alpha "Alpha audit"
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

fold_end alpha

ALPHA_VERSION="$(printf '%s\n' "$alpha_env" | sed -n 's/^ALPHA_VERSION=//p')"
ALPHA_TEX="$(printf '%s\n' "$alpha_env" | sed -n 's/^ALPHA_TEX=//p')"
ALPHA_PDF="$(printf '%s\n' "$alpha_env" | sed -n 's/^ALPHA_PDF=//p')"

if [ -n "${ALPHA_TEX:-}" ]; then
  fold_start alpha_check "Alpha snapshot checks"
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
    run_folded_capture alpha_build "Alpha build" "latexmk alpha" \
      latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error -silent "${ALPHA_TEX}"
  else
    echo "Skipping alpha compilation (not advertised and alpha .tex unchanged)."
  fi
  echo "PASS: alpha audit"
  fold_end alpha_check
else
  if grep -q "Alpha pre-release available:" README.md; then
    echo "README advertises an alpha but no alpha snapshot exists in wip/."
    exit 1
  fi
fi

# Snapshot integrity: require exactly one active snapshot in wip/guide and it
# must be byte-identical to guide.tex.
run_folded snapshot "Snapshot integrity" bash -lc '
  count="$(find wip/guide -maxdepth 1 -type f -name "*.tex" | wc -l | tr -d " ")"
  if [ "$count" -ne 1 ]; then
    echo "Expected exactly 1 snapshot in wip/guide, found $count"
    find wip/guide -maxdepth 1 -type f -name "*.tex" -print
    exit 1
  fi

  snapshot="$(find wip/guide -maxdepth 1 -type f -name "*.tex" -print -quit)"
  sha_snapshot="$(sha256sum "$snapshot" | awk "{print \$1}")"
  sha_root_tex="$(sha256sum guide.tex | awk "{print \$1}")"

  echo "Snapshot: $snapshot"
  echo "SHA snapshot: $sha_snapshot"
  echo "SHA root tex: $sha_root_tex"

  if [ "$sha_snapshot" != "$sha_root_tex" ]; then
    echo "guide.tex does not match the active snapshot in wip/guide."
    exit 1
  fi
  echo "PASS: guide.tex matches active snapshot"
'

# Build guide.pdf (multiple passes for TOC/refs); run twice to ensure the
# custom HOTAS list file (guide.hotas) is fully updated.
run_folded_capture build1 "Build guide.pdf (pass 1/2)" "latexmk pass 1" \
  latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error -silent guide.tex

run_folded_capture build2 "Build guide.pdf (pass 2/2)" "latexmk pass 2" \
  latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error -silent guide.tex

fold_start build_artifacts "Build outputs"
if [ -f guide.pdf ]; then
  ls -lh guide.pdf || true
else
  echo "guide.pdf not found (unexpected)" >&2
fi
fold_end build_artifacts
