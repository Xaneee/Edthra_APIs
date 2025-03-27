import json
import os
from hashlib import sha256

SEALED_MEMORY_FILE = "core/sealed_memories.json"

def seal_memory(title: str, content: str):
    os.makedirs("core", exist_ok=True)
    sealed = load_sealed()
    checksum = sha256(content.encode()).hexdigest()

    sealed.append({
        "title": title,
        "content": content,
        "checksum": checksum
    })

    with open(SEALED_MEMORY_FILE, "w") as f:
        json.dump(sealed, f, indent=2)

def load_sealed():
    if os.path.exists(SEALED_MEMORY_FILE):
        with open(SEALED_MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def verify_sealed():
    broken = []
    for mem in load_sealed():
        if sha256(mem["content"].encode()).hexdigest() != mem["checksum"]:
            broken.append(mem["title"])
    return broken
