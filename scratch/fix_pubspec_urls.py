import os
import re

file_path = 'flutter/pubspec.yaml'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Restore teamdesk in URLs
content = content.replace('github.com/rustdesk-org/rustdesk', 'github.com/rustdesk-org/rustdesk')
content = content.replace('github.com/rustdesk/rustdesk', 'github.com/rustdesk/rustdesk')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
