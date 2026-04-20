import os
BASE = 'projects'

def write_project_files(sid, text):
    root = os.path.join(BASE, sid)
    os.makedirs(root, exist_ok=True)
    for part in text.split('filename:')[1:]:
        name, code = part.strip().split('\n', 1)
        if '..' in name:
            continue
        path = os.path.join(root, name.strip())
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(code.strip())
    return root