import sys

file_path = 'build.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace rustdesk with teamdesk in build.py
content = content.replace("'rustdesk'", "'teamdesk'")
content = content.replace('"rustdesk"', '"teamdesk"')
content = content.replace('/rustdesk', '/teamdesk')
content = content.replace('rustdesk.deb', 'teamdesk.deb')
content = content.replace('rustdesk.exe', 'teamdesk.exe')
content = content.replace('rustdesk.dll', 'teamdesk.dll')
content = content.replace('librustdesk', 'libteamdesk')
content = content.replace('RustDesk.app', 'TeamDesk.app')
content = content.replace('rustdesk.service', 'teamdesk.service')
content = content.replace('rustdesk.desktop', 'teamdesk.desktop')
content = content.replace('rustdesk.png', 'teamdesk.png')
content = content.replace('rustdesk.svg', 'teamdesk.svg')
content = content.replace('Package: rustdesk', 'Package: teamdesk')
content = content.replace('Maintainer: rustdesk', 'Maintainer: teamdesk')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
