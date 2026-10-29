"""Validate catalog contracts locally; does not access GitHub or install plugins."""
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / '.agents/plugins/marketplace.json').read_text())
assert catalog['name'] == 'pablopoo-plugins'
assert catalog['interface']['displayName']
plugins = catalog['plugins']
assert plugins, 'Catalog must contain plugins'
names = [entry['name'] for entry in plugins]
assert len(names) == len(set(names)), 'Duplicate plugin identifiers'
for entry in plugins:
    source = entry['source']
    assert source['source'] == 'git-subdir'
    url = urlsplit(source['url'])
    assert url.scheme == 'https' and url.hostname == 'github.com'
    assert not url.username and not url.password and not url.query and not url.fragment
    assert re.fullmatch(r'/[^/]+/[^/]+', url.path), source['url']
    assert re.fullmatch(r'[0-9a-f]{40}', source['sha']), 'Use a full commit SHA'
    assert 'ref' not in source, 'Floating refs must not override a reviewed commit'
    path = Path(source['path'])
    assert source['path'].startswith('./') and '..' not in path.parts
    assert not path.is_absolute() and len(path.parts) >= 2
    assert entry['policy']['installation'] == 'AVAILABLE'
    assert entry['policy']['authentication'] == 'ON_INSTALL'
    assert entry['category'] == 'Productivity'
    assert source['sha'] in (root / 'README.md').read_text(), 'Document each pin'
for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', (root / 'README.md').read_text()):
    if not target.startswith(('https://', '#')):
        assert (root / target).exists(), target
assert (root / 'LICENSE').read_text().startswith('MIT License')
print(f'PASS: {len(plugins)} unique plugins, pinned GitHub sources, policies, README pins and license')
