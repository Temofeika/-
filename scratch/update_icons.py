import os
import re
import sys

files_to_process = [
    '.github/workflows/flutter-build.yml',
    '.github/workflows/ci.yml',
    '.github/workflows/flutter-tag.yml',
    '.github/workflows/fdroid.yml',
    '.github/workflows/playground.yml',
    '.github/workflows/third-party-TeamDeskTempTopMostWindow.yml',
    'build.py',
    'res/PKGBUILD',
    'res/rpm.spec',
    'res/rpm-suse.spec',
    'res/pacman_install'
]

for file_path in files_to_process:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = content.replace('res/128x128@2x.png', 'res/teamdesk.png')
    new_content = new_content.replace('res/scalable.svg', 'res/teamdesk.svg')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Processed {file_path}")
