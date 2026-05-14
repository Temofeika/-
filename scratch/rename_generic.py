import sys

if len(sys.argv) < 2:
    print("Usage: python rename.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Comprehensive renaming
content = content.replace('RustDesk.app', 'TeamDesk.app')
content = content.replace('rustdesk.json', 'teamdesk.json')
content = content.replace('rustdesk.keychain', 'teamdesk.keychain')
content = content.replace('rustdesk-${{ env.VERSION }}', 'teamdesk-${{ env.VERSION }}')
content = content.replace('rustdesk_portable.exe', 'teamdesk_portable.exe')
content = content.replace('rustdesk-lib-cache', 'teamdesk-lib-cache')
content = content.replace('name: rustdesk', 'name: teamdesk')
content = content.replace('Build rustdesk', 'Build teamdesk')
# Extra ones for ci.yml etc
content = content.replace('rustdesk.deb', 'teamdesk.deb')
content = content.replace('rustdesk.rpm', 'teamdesk.rpm')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
