import os
import re

files_to_process = [
    '.github/workflows/flutter-build.yml',
    '.github/workflows/ci.yml',
    '.github/workflows/flutter-tag.yml',
    '.github/workflows/fdroid.yml',
    '.github/workflows/playground.yml',
    '.github/workflows/third-party-TeamDeskTempTopMostWindow.yml'
]

def restore_urls(content):
    # Restore specific repository names that were incorrectly renamed
    new_content = content.replace('github.com/rustdesk-org/TeamDeskTempTopMostWindow', 'github.com/rustdesk-org/TeamDeskTempTopMostWindow')
    new_content = new_content.replace('github.com/rustdesk/TeamDesk', 'github.com/rustdesk/rustdesk') # Just in case
    return new_content

for file_path in files_to_process:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = restore_urls(content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Restored URLs in {file_path}")
