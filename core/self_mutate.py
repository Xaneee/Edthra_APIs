# core/self_mutate.py

import os

def apply_self_mutation(file_path: str):
    if not os.path.exists(file_path):
        return "[✗] File does not exist."

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    if "# Mutation:" in code:
        code += "\n\n# Mutation: AI added nothing new this cycle."
    else:
        code += "\n\n# Mutation: Initial AI comment block inserted."

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

    return "[✓] Self-mutation applied."
