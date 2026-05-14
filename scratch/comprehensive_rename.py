import os
import re
import sys

if len(sys.argv) > 1:
    files_to_process = sys.argv[1:]
else:
    files_to_process = [
        '.github/workflows/flutter-build.yml',
        '.github/workflows/ci.yml',
        '.github/workflows/flutter-tag.yml',
        '.github/workflows/fdroid.yml',
        '.github/workflows/playground.yml',
        '.github/workflows/third-party-TeamDeskTempTopMostWindow.yml',
        'build.py',
        'Cargo.toml',
        'libs/hbb_common/src/config.rs',
        'flutter/pubspec.yaml',
        'flutter/lib/models/native_model.dart',
        'flutter/lib/common.dart',
        'res/PKGBUILD',
        'res/rpm.spec',
        'res/rpm-suse.spec',
        'res/teamdesk.service',
        'res/teamdesk.desktop',
        'res/teamdesk-link.desktop',
        'res/pam.d/teamdesk.debian',
        'res/pacman_install',
        'libs/portable/generate.py',
        'libs/portable/Cargo.toml'
    ]

def replace_teamdesk(content):
    def replacer(match):
        word = match.group(0)
        if word == 'TeamDesk': return 'TeamDesk'
        if word == 'teamdesk': return 'teamdesk'
        if word == 'RUSTDESK': return 'TEAMDESK'
        return word

    new_content = re.sub(r'\b[Rr]ust[Dd]esk\b', replacer, content)
    new_content = re.sub(r'teamdesk', 'teamdesk', new_content)
    new_content = re.sub(r'TeamDesk', 'TeamDesk', new_content)
    
    new_content = new_content.replace('github.com/rustdesk/rustdesk', 'github.com/rustdesk/rustdesk')
    new_content = new_content.replace('github.com/rustdesk/', 'github.com/rustdesk/')
    new_content = new_content.replace('github.com/rustdesk-org/', 'github.com/rustdesk-org/')
    
    return new_content

for file_path in files_to_process:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = replace_teamdesk(content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Processed {file_path}")
