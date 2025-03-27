# core/logic_memory.py

import json
import os
from datetime import datetime

COMPRESSED_FILE = "core/logic_memory.json"
os.makedirs("core", exist_ok=True)

def compress_logic(name: str, description: str, code: str):
    """
    Saves a logic snippet with description for later use.
    """
    compressed = {
        "name": name,
        "description": description,
        "code": code.strip(),
        "timestamp": datetime.utcnow().isoformat()
    }

    memory = []
    if os.path.exists(COMPRESSED_FILE):
        with open(COMPRESSED_FILE, "r") as f:
            memory = json.load(f)

    memory.append(compressed)

    with open(COMPRESSED_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def retrieve_logic(keyword: str):
    """
    Returns compressed logic by description keyword match.
    """
    if not os.path.exists(COMPRESSED_FILE):
        return []

    with open(COMPRESSED_FILE, "r") as f:
        memory = json.load(f)

    return [
        entry for entry in memory if keyword.lower() in entry["description"].lower()
    ]
