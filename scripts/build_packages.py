#!/usr/bin/env python3
"""Build reproducible installation ZIPs only from this repository's distributions."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPECS = {
    'khanato-codex.zip': ('codex/skills/khanato', 'khanato/'),
    'khanato-claude-plugin.zip': ('claude', ''),
    'khanato-claude-skill.zip': ('claude/skills/khanato', 'khanato/'),
}

def expected_content(source, prefix):
    result = {}
    for path in sorted(source.rglob('*')):
        if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
            raise ValueError(f'Linked path not allowed: {path.relative_to(ROOT)}')
        if path.is_file():
            relative = path.relative_to(source)
            if '__pycache__' in relative.parts or path.suffix in {'.pyc', '.pyo'}:
                continue
            if path.suffix not in {'.md', '.json', '.yaml', '.py'}:
                raise ValueError(f'Unexpected distribution file: {path.relative_to(ROOT)}')
            result[prefix+relative.as_posix()] = path.read_bytes()
    return result

def main():
    output = ROOT/'packages'
    output.mkdir(exist_ok=True)
    manifest = {'distribution': json.loads((ROOT/'versions.json').read_text(encoding='utf-8'))['distribution'], 'packages': []}
    for name, (source, prefix) in SPECS.items():
        files = expected_content(ROOT/source, prefix)
        target = output/name
        with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path, content in files.items():
                entry = zipfile.ZipInfo(path, date_time=(2026, 10, 3, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, content, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        manifest['packages'].append({'file': name, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest(), 'bytes': target.stat().st_size, 'files': len(files), 'source': source})
    (output/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
    (output/'SHA256SUMS').write_text(''.join(f'{p["sha256"]}  {p["file"]}\n' for p in manifest['packages']), encoding='utf-8', newline='\n')
    print(json.dumps(manifest, ensure_ascii=False))

if __name__ == '__main__':
    main()
