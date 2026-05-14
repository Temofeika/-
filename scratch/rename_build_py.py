import sys

file_path = 'build.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace teamdesk with teamdesk in build.py
content = content.replace("'teamdesk'", "'teamdesk'")
content = content.replace('"teamdesk"', '"teamdesk"')
content = content.replace('/teamdesk', '/teamdesk')
content = content.replace('teamdesk.deb', 'teamdesk.deb')
content = content.replace('teamdesk.exe', 'teamdesk.exe')
content = content.replace('teamdesk.dll', 'teamdesk.dll')
content = content.replace('libteamdesk', 'libteamdesk')
content = content.replace('TeamDesk.app', 'TeamDesk.app')
content = content.replace('teamdesk.service', 'teamdesk.service')
content = content.replace('teamdesk.desktop', 'teamdesk.desktop')
content = content.replace('teamdesk.png', 'teamdesk.png')
content = content.replace('teamdesk.svg', 'teamdesk.svg')
content = content.replace('Package: teamdesk', 'Package: teamdesk')
content = content.replace('Maintainer: teamdesk', 'Maintainer: teamdesk')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
