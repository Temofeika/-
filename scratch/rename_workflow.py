import sys

file_path = '.github/workflows/flutter-build.yml'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace teamdesk with teamdesk in specific contexts
# Artifact names
content = content.replace('name: teamdesk-', 'name: teamdesk-')
content = content.replace('name: teamdesk_', 'name: teamdesk_')
# Binary names in paths
content = content.replace('/teamdesk', '/teamdesk')
content = content.replace('teamdesk.exe', 'teamdesk.exe')
content = content.replace('teamdesk.deb', 'teamdesk.deb')
content = content.replace('teamdesk.rpm', 'teamdesk.rpm')
content = content.replace('teamdesk.AppImage', 'teamdesk.AppImage')
content = content.replace('teamdesk.apk', 'teamdesk.apk')
content = content.replace('teamdesk.dmg', 'teamdesk.dmg')
content = content.replace('teamdesk.msi', 'teamdesk.msi')
content = content.replace('libteamdesk', 'libteamdesk')
# Step names
content = content.replace('Build teamdesk', 'Build teamdesk')
content = content.replace('Rename teamdesk', 'Rename teamdesk')
content = content.replace('Sign teamdesk', 'Sign teamdesk')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
