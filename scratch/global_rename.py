import os
import re

# Directories to exclude
exclude_dirs = {'.git', 'target', 'build', 'node_modules', '.idea', '.vscode', 'vendor'}
# Extensions to include (text files only)
include_extensions = {'.rs', '.dart', '.yml', '.yaml', '.toml', '.py', '.tis', '.html', '.css', '.js', '.sh', '.bat', '.ps1', '.json', '.txt', '.md', '.spec', 'PKGBUILD', 'pacman_install'}

def replace_teamdesk(content):
    def replacer(match):
        word = match.group(0)
        if word == 'TeamDesk': return 'TeamDesk'
        if word == 'teamdesk': return 'teamdesk'
        if word == 'RUSTDESK': return 'TEAMDESK'
        return word

    new_content = re.sub(r'\b[Rr]ust[Dd]esk\b', replacer, content)
    new_content = re.sub(r'teamdesk', 'teamdesk', new_content)
    new_content = re.sub(r'TeamDesk', 'TeamDesk', new_content)
    
    # Restore URLs
    new_content = new_content.replace('github.com/rustdesk/rustdesk', 'github.com/rustdesk/rustdesk')
    new_content = new_content.replace('github.com/rustdesk/', 'github.com/rustdesk/')
    new_content = new_content.replace('github.com/rustdesk-org/', 'github.com/rustdesk-org/')
    new_content = new_content.replace('github.com/rustdesk-org/rustdesk', 'github.com/rustdesk-org/rustdesk') # Restore sub-repos
    
    return new_content

for root, dirs, files in os.walk('.'):
    # Prune excluded directories
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    for file in files:
        _, ext = os.path.splitext(file)
        if ext in include_extensions or file in include_extensions:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                new_content = replace_teamdesk(content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Processed {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
