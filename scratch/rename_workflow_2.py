import sys

file_path = '.github/workflows/flutter-build.yml'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Comprehensive renaming
content = content.replace('TeamDesk.app', 'TeamDesk.app')
content = content.replace('teamdesk.json', 'teamdesk.json')
content = content.replace('teamdesk.keychain', 'teamdesk.keychain')
content = content.replace('teamdesk-${{ env.VERSION }}', 'teamdesk-${{ env.VERSION }}')
content = content.replace('teamdesk_portable.exe', 'teamdesk_portable.exe')
content = content.replace('teamdesk-lib-cache', 'teamdesk-lib-cache')
# Fix some missed artifacts
content = content.replace('name: teamdesk', 'name: teamdesk')
# Fix missed step names
content = content.replace('Build teamdesk', 'Build teamdesk')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
