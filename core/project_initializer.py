import os
from datetime import datetime

def create_new_project(name: str, description: str):
    path = f"projects/{name.replace(' ', '_')}"
    os.makedirs(path, exist_ok=True)
    meta = {
        "name": name,
        "description": description,
        "created": datetime.utcnow().isoformat(),
        "status": "in_progress"
    }
    with open(f"{path}/project.meta", "w", encoding="utf-8") as f:
        f.write(str(meta))
    return f"[✓] Project folder initialized: {path}"
