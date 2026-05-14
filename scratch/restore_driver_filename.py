import os
import re

file_path = '.github/workflows/flutter-build.yml'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Restore printer driver URL components
content = content.replace('teamdesk_printer_driver_v4-1.4.zip', 'teamdesk_printer_driver_v4-1.4.zip')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
