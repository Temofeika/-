import sys

file_path = '.github/workflows/flutter-build.yml'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Restore teamdesk URLs
content = content.replace('github.com/rustdesk/', 'github.com/rustdesk/')
content = content.replace('github.com/rustdesk-org/', 'github.com/rustdesk-org/')
# Also restore some custom actions if they were renamed
content = content.replace('uses: teamdesk/', 'uses: teamdesk/')
content = content.replace('uses: teamdesk-org/', 'uses: teamdesk-org/')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
