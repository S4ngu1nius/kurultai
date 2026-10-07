#!/usr/bin/env python3
"""Verify repository distributions and local helper contracts; no model calls or network."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from urllib.parse import unquote
from build_packages import SPECS, expected_content

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packages', action='store_true')
    args = parser.parse_args()
    versions = json.loads((ROOT/'versions.json').read_text(encoding='utf-8'))
    codex = ROOT/'codex/skills/khanato'
    claude = ROOT/'claude/skills/khanato'
    manifest = json.loads((ROOT/'claude/.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    marketplace = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    assert manifest['name'] == 'khanato' and manifest['version'] == versions['claude']['plugin']
    assert marketplace['plugins'][0]['name'] == manifest['name'] and marketplace['plugins'][0]['source'] == './claude'
    agent_paths = list((ROOT/'claude/agents').glob('*.md'))
    assert len(agent_paths) == 50
    for agent_path in agent_paths:
        declaration = agent_path.read_text(encoding='utf-8').split('---', 2)[1]
        assert re.search(r'^name: ' + re.escape(agent_path.stem) + r'$', declaration, re.M)
        assert re.search(r'^model: inherit$', declaration, re.M)
    assert {p.parent.name for p in (ROOT/'claude/skills').glob('*/SKILL.md')} == {'khanato', 'arauto', 'curia', 'nous', 'vigil', 'voz-do-contra'}
    assert (codex/'agents/openai.yaml').is_file()
    shared = ['00-CONSTITUICAO-ESTRUTURA-FLUXOS.md', '01-GRANDE-KHAN.md', '02-EMPRESAS-LIDERANCA.md', '03-EMPRESAS-SQUAD.md', '04-CURIA-JURIDICO.md', '05-ARAUTO-MARKETING.md', '10-EXPANSAO.md', '11-ORGANIZACAO-FLUXOS.md', '13-REPERTORIO-UX.md', '14-SEGURANCA-APLICACOES.md', '15-FORMATOS-OBSIDIAN.md']
    for name in shared:
        assert (codex/'references'/name).read_bytes() == (claude/'references'/name).read_bytes(), f'Common core differs: {name}'
    for name in ['create_eval_workspace.py', 'validate_eval_results.py', 'test_validate_eval_results.py']:
        assert (codex/'scripts'/name).read_bytes() == (claude/'scripts'/name).read_bytes(), f'Helper differs: {name}'
    routes = 0
    for path in ROOT.rglob('*.md'):
        if any(part in {'.git', '.local', '__pycache__', 'obsidian-pending'} for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding='utf-8')
        assert not re.search(r'\b[A-Za-z]:\\[^\s`]|/(?:home|Users)/[^\s`/]+/', text), f'Local absolute path: {path.relative_to(ROOT)}'
        for url in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
            url = url.strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', url):
                continue
            filename = unquote(url.split('#', 1)[0])
            target = (path.parent/filename).resolve() if filename else path.resolve()
            assert target.is_relative_to(ROOT) and target.exists(), f'Broken or external local link: {path.relative_to(ROOT)} -> {url}'
            routes += 1
    for edition, core in [('codex', codex), ('claude', claude)]:
        text = (core/'SKILL.md').read_text(encoding='utf-8')
        assert f'version: "{versions[edition]["skill"]}"' in text
        for script_args in [['scripts/test_validate_eval_results.py'], ['scripts/validate_eval_results.py', 'evals/results-template.json']]:
            result = subprocess.run([sys.executable, '-B', *script_args], cwd=core, capture_output=True, text=True, encoding='utf-8')
            assert result.returncode == 0, f'{edition}: {result.stdout}\n{result.stderr}'
            print(f'{edition}: {script_args[0]} passed')
    if args.packages:
        record = json.loads((ROOT/'packages/manifest.json').read_text(encoding='utf-8'))
        assert record['distribution'] == versions['distribution']
        assert {p['file'] for p in record['packages']} == set(SPECS)
        for package in record['packages']:
            path = ROOT/'packages'/package['file']
            assert hashlib.sha256(path.read_bytes()).hexdigest() == package['sha256']
            source, prefix = SPECS[package['file']]
            expected = expected_content(ROOT/source, prefix)
            with zipfile.ZipFile(path) as archive:
                assert archive.testzip() is None
                assert set(archive.namelist()) == set(expected) and len(archive.namelist()) == len(expected)
                for name in archive.namelist():
                    assert not PurePosixPath(name).is_absolute() and '..' not in PurePosixPath(name).parts and ':' not in name
                    assert archive.read(name) == expected[name], f'ZIP drift: {name}'
        expected_sums = ''.join(f'{p["sha256"]}  {p["file"]}\n' for p in record['packages'])
        assert (ROOT/'packages/SHA256SUMS').read_text(encoding='utf-8') == expected_sums
    print(json.dumps({'status': 'pass', 'markdown_routes': routes, 'shared_reference_files': len(shared), 'packages_checked': args.packages, 'model_runtime_tests': 'not_run'}))

if __name__ == '__main__':
    main()
