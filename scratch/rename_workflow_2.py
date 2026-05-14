import sys

file_path = '.github/workflows/flutter-build.yml'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Comprehensive renaming
content = content.replace('RustDesk.app', 'TeamDesk.app')
content = content.replace('rustdesk.json', 'teamdesk.json')
content = content.replace('rustdesk.keychain', 'teamdesk.keychain')
content = content.replace('rustdesk-${{ env.VERSION }}', 'teamdesk-${{ env.VERSION }}')
content = content.replace('rustdesk_portable.exe', 'teamdesk_portable.exe')
content = content.replace('rustdesk-lib-cache', 'teamdesk-lib-cache')
# Fix some missed artifacts
content = content.replace('name: rustdesk', 'name: teamdesk')
# Fix missed step names
content = content.replace('Build rustdesk', 'Build teamdesk')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
