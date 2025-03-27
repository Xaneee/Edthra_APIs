# core/personality_engine.py

import json
import os

PERSONALITY_FILE = "core/personality_memory.json"
os.makedirs("core", exist_ok=True)

def update_trait(trait: str, value: str):
    if os.path.exists(PERSONALITY_FILE):
        with open(PERSONALITY_FILE, "r") as f:
            memory = json.load(f)
    else:
        memory = []

    updated = False
    for item in memory:
        if item["trait"] == trait:
            item["value"] = value
            updated = True
            break

    if not updated:
        memory.append({"trait": trait, "value": value})

    with open(PERSONALITY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def reflect_on_traits():
    if os.path.exists(PERSONALITY_FILE):
        with open(PERSONALITY_FILE, "r") as f:
            memory = json.load(f)
        return {item["trait"]: item["value"] for item in memory}
    return {}
