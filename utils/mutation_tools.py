# File: utils/mutation_tools.py

import os
import shutil
from datetime import datetime

def backup_main():
    src = "core/main.py"
    dst = f"backups/main_backup_{datetime.utcnow().isoformat().replace(':', '_')}.py"
    shutil.copyfile(src, dst)

def apply_safe_mutation(file_path: str, code: str) -> str:
    try:
        with open(file_path, "a") as f:
            f.write(f"\n\n# Mutation ({datetime.utcnow().isoformat()}):\n{code}\n")
        return "Mutation appended successfully."
    except Exception as e:
        return f"Failed to mutate: {str(e)}"

def backup_main():
    src = "core/main.py"
    if not os.path.exists(src):
        return  # Skip backup if file doesn't exist yet

    dst = f"backups/main_backup_{datetime.utcnow().isoformat().replace(':', '_')}.py"
    shutil.copyfile(src, dst)
