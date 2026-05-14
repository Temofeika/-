import os
import re

workflow_files = [
    '.github/workflows/flutter-build.yml',
    '.github/workflows/ci.yml',
    '.github/workflows/flutter-tag.yml',
    '.github/workflows/bridge.yml'
]

def update_workflow(content):
    # 1. Permissions
    if 'permissions:' not in content:
        content = content.replace('name:', 'permissions:\n  contents: write\n\nname:', 1)
    
    # 2. action-gh-release@v2
    content = content.replace('softprops/action-gh-release@v1', 'softprops/action-gh-release@v2')
    
    # 3. Targeted rename (avoiding URLs)
    # Replace rustdesk with teamdesk in artifact names and paths
    # We will look for lines that are NOT URLs
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if 'https://' in line or 'http://' in line:
            # Keep URLs as is, but maybe fix some specific ones if they are local
            new_lines.append(line)
        else:
            # Replace rustdesk/RustDesk
            new_line = line.replace('rustdesk', 'teamdesk').replace('RustDesk', 'TeamDesk')
            new_lines.append(new_line)
    
    return '\n'.join(new_lines)

for file_path in workflow_files:
    if not os.path.exists(file_path): continue
    with open(file_path, 'r', encoding='utf-8') as f: content = f.read()
    new_content = update_workflow(content)
    with open(file_path, 'w', encoding='utf-8') as f: f.write(new_content)
    print(f"Updated {file_path}")
