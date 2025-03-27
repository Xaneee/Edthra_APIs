import os
from shutil import copyfile

def verify_integrity():
    required_files = [
        "core/father.crystal",
        "core/gita_knowledge.json",
        "utils/code_mutator.py",
        "utils/reasoning_engine.py"
    ]
    for path in required_files:
        if not os.path.exists(path):
            return False
    return True

def freeze_mutations():
    mutation_file = "utils/code_mutator.py"
    backup = mutation_file + ".bak"
    if os.path.exists(mutation_file):
        copyfile(mutation_file, backup)
        os.chmod(mutation_file, 0o444)  # read-only
