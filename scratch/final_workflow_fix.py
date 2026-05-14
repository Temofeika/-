import os
import re

workflow_files = [
    '.github/workflows/flutter-build.yml',
    '.github/workflows/ci.yml',
    '.github/workflows/flutter-tag.yml',
    '.github/workflows/bridge.yml',
    '.github/workflows/third-party-TeamDeskTempTopMostWindow.yml'
]

def final_fix(content):
    # 1. Restore rustdesk-org actions
    content = content.replace('uses: teamdesk-org/', 'uses: rustdesk-org/')
    
    # 2. Restore RustDeskTempTopMostWindow URLs
    content = content.replace('github.com/rustdesk-org/TeamDeskTempTopMostWindow', 'github.com/rustdesk-org/RustDeskTempTopMostWindow')
    content = content.replace('git clone https://github.com/rustdesk-org/TeamDeskTempTopMostWindow', 'git clone https://github.com/rustdesk-org/RustDeskTempTopMostWindow')
    
    # 3. Fix printer driver download filenames again just in case
    content = content.replace('teamdesk_printer_driver_v4-1.4.zip', 'rustdesk_printer_driver_v4-1.4.zip')
    
    # 4. Fix some artifact renames that might be inconsistent
    # Actually, keep teamdesk for artifacts if they are produced by us.
    
    return content

for file_path in workflow_files:
    if not os.path.exists(file_path): continue
    with open(file_path, 'r', encoding='utf-8') as f: content = f.read()
    new_content = final_fix(content)
    with open(file_path, 'w', encoding='utf-8') as f: f.write(new_content)
    print(f"Fixed {file_path}")
