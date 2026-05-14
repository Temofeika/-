import sys

file_path = '.github/workflows/flutter-build.yml'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace rustdesk with teamdesk in specific contexts
# Artifact names
content = content.replace('name: rustdesk-', 'name: teamdesk-')
content = content.replace('name: rustdesk_', 'name: teamdesk_')
# Binary names in paths
content = content.replace('/rustdesk', '/teamdesk')
content = content.replace('rustdesk.exe', 'teamdesk.exe')
content = content.replace('rustdesk.deb', 'teamdesk.deb')
content = content.replace('rustdesk.rpm', 'teamdesk.rpm')
content = content.replace('rustdesk.AppImage', 'teamdesk.AppImage')
content = content.replace('rustdesk.apk', 'teamdesk.apk')
content = content.replace('rustdesk.dmg', 'teamdesk.dmg')
content = content.replace('rustdesk.msi', 'teamdesk.msi')
content = content.replace('librustdesk', 'libteamdesk')
# Step names
content = content.replace('Build rustdesk', 'Build teamdesk')
content = content.replace('Rename rustdesk', 'Rename teamdesk')
content = content.replace('Sign rustdesk', 'Sign teamdesk')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
