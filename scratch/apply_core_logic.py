import os
import re

# 1. Session limit in src/server/connection.rs
path = 'src/server/connection.rs'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'std::time::Instant' not in content:
        content = 'use std::time::{Instant, Duration};\n' + content
    # Add session limit logic
    insertion = """
        if !self.authorized && self.start_time.elapsed() > Duration::from_secs(120) {
            log::warn!("Unauthorized session timeout for {}", self.id);
            return Ok(());
        }
    """
    if 'let mut sessions = SESSIONS.write().unwrap();' in content:
        content = content.replace('let mut sessions = SESSIONS.write().unwrap();', 'let mut sessions = SESSIONS.write().unwrap();' + insertion)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated connection.rs")

# 2. Rendezvous server in libs/hbb_common/src/config.rs
path = 'libs/hbb_common/src/config.rs'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'pub const RENDEZVOUS_SERVERS: &\[&str\] = &\[\".*?\"\];', 'pub const RENDEZVOUS_SERVERS: &[&str] = &["teamdesk.example.com"];', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated config.rs")

# 3. UI Colors in flutter/lib/common.dart
path = 'flutter/lib/common.dart'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('Colors.blue', 'Colors.indigo')
    content = content.replace('Colors.blueAccent', 'Colors.deepPurpleAccent')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated common.dart")
