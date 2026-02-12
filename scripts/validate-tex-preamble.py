#!/usr/bin/env python3
"""
Validador de preâmbulo e conteúdo mínimo para arquivos .tex do projeto BMS Guide.
- Valida todos os .tex em wip/ (recursivo) e guide.tex na raiz.
- Compara comandos/pacotes do preâmbulo com o template.
- Checa ausência de placeholders proibidos (TBD, TODO).
- Reporta divergências, ausências e comandos obsoletos.

Uso:
  python scripts/validate-tex-preamble.py
"""
import os
import re
from pathlib import Path

# Caminhos
REPO_ROOT = Path(__file__).parent.parent.resolve()
TEMPLATE = REPO_ROOT / 'template' / 'template-wip-V1.0.tex'
WIP_DIR = REPO_ROOT / 'wip'
GUIDE_TEX = REPO_ROOT / 'guide.tex'

# Regex para extrair preâmbulo (até \begin{document} ou primeira section)
PREAMBLE_END_RE = re.compile(r'\\begin\{document\}|^%+.*FIM DO PREAMBULO', re.MULTILINE)
PLACEHOLDER_RE = re.compile(r'\b(TBD|TODO)\b', re.IGNORECASE)

# Função para extrair preâmbulo
def extract_preamble(tex_path):
    with open(tex_path, encoding='utf-8') as f:
        content = f.read()
    match = PREAMBLE_END_RE.search(content)
    return content[:match.start()] if match else content

def get_all_tex_files():
    tex_files = [GUIDE_TEX]
    for path in WIP_DIR.rglob('*.tex'):
        tex_files.append(path)
    return tex_files

def main():
    # Extrai preâmbulo do template
    template_preamble = extract_preamble(TEMPLATE)
    # Extrai comandos/pacotes do template
    template_cmds = set(re.findall(r'\\[a-zA-Z@]+', template_preamble))
    template_pkgs = set(re.findall(r'\\usepackage\{([^}]+)\}', template_preamble))

    errors = 0
    for tex_path in get_all_tex_files():
        preamble = extract_preamble(tex_path)
        cmds = set(re.findall(r'\\[a-zA-Z@]+', preamble))
        pkgs = set(re.findall(r'\\usepackage\{([^}]+)\}', preamble))
        missing_cmds = template_cmds - cmds
        missing_pkgs = template_pkgs - pkgs
        placeholders = PLACEHOLDER_RE.findall(open(tex_path, encoding='utf-8').read())
        if missing_cmds or missing_pkgs or placeholders:
            print(f'\nArquivo: {tex_path.relative_to(REPO_ROOT)}')
            if missing_cmds:
                print(f'  Comandos ausentes: {sorted(missing_cmds)}')
            if missing_pkgs:
                print(f'  Pacotes ausentes: {sorted(missing_pkgs)}')
            if placeholders:
                print(f'  Placeholders proibidos encontrados: {set(placeholders)}')
            errors += 1
    if errors == 0:
        print('Todos os arquivos .tex estão em conformidade com o preâmbulo e conteúdo mínimo!')
        exit(0)
    else:
        print(f'\nTotal de arquivos com problemas: {errors}')
        exit(1)

if __name__ == '__main__':
    main()
