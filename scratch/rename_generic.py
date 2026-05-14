import sys

if len(sys.argv) < 2:
    print("Usage: python rename.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Comprehensive renaming
content = content.replace('TeamDesk.app', 'TeamDesk.app')
content = content.replace('teamdesk.json', 'teamdesk.json')
content = content.replace('teamdesk.keychain', 'teamdesk.keychain')
content = content.replace('teamdesk-${{ env.VERSION }}', 'teamdesk-${{ env.VERSION }}')
content = content.replace('teamdesk_portable.exe', 'teamdesk_portable.exe')
content = content.replace('teamdesk-lib-cache', 'teamdesk-lib-cache')
content = content.replace('name: teamdesk', 'name: teamdesk')
content = content.replace('Build teamdesk', 'Build teamdesk')
# Extra ones for ci.yml etc
content = content.replace('teamdesk.deb', 'teamdesk.deb')
content = content.replace('teamdesk.rpm', 'teamdesk.rpm')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
