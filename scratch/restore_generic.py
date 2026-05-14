import sys

if len(sys.argv) < 2:
    print("Usage: python restore.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Restore teamdesk URLs
content = content.replace('github.com/rustdesk/', 'github.com/rustdesk/')
content = content.replace('github.com/rustdesk-org/', 'github.com/rustdesk-org/')
content = content.replace('uses: teamdesk/', 'uses: teamdesk/')
content = content.replace('uses: teamdesk-org/', 'uses: teamdesk-org/')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
