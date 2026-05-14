import os
import re

# 1. Cargo.toml
path = 'Cargo.toml'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f: content = f.read()
    content = content.replace('name = "rustdesk"', 'name = "teamdesk"')
    content = content.replace('default-run = "rustdesk"', 'default-run = "teamdesk"')
    with open(path, 'w', encoding='utf-8') as f: f.write(content)
    print("Updated Cargo.toml")

# 2. flutter/pubspec.yaml
path = 'flutter/pubspec.yaml'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f: content = f.read()
    content = content.replace('name: rustdesk', 'name: teamdesk')
    with open(path, 'w', encoding='utf-8') as f: f.write(content)
    print("Updated pubspec.yaml")

# 3. build.py
path = 'build.py'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f: content = f.read()
    content = content.replace("hbb_name = 'rustdesk'", "hbb_name = 'teamdesk'")
    with open(path, 'w', encoding='utf-8') as f: f.write(content)
    print("Updated build.py")

# 4. native_model.dart
path = 'flutter/lib/models/native_model.dart'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f: content = f.read()
    content = content.replace("'librustdesk.so'", "'libteamdesk.so'")
    content = content.replace("'librustdesk.dylib'", "'libteamdesk.dylib'")
    content = content.replace("'librustdesk'", "'libteamdesk'")
    with open(path, 'w', encoding='utf-8') as f: f.write(content)
    print("Updated native_model.dart")

# 5. strings.xml (Android app name)
path = 'flutter/android/app/src/main/res/values/strings.xml'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f: content = f.read()
    content = content.replace('RustDesk', 'TeamDesk')
    with open(path, 'w', encoding='utf-8') as f: f.write(content)
    print("Updated strings.xml")
