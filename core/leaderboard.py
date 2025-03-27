# core/leaderboard.py

import json
import os
from datetime import datetime

LEADERBOARD_FILE = "core/mutation_leaderboard.json"
os.makedirs("core", exist_ok=True)

def record_top_mutation(code_id: str, score: int, logic: str, notes: str = ""):
    entry = {
        "id": code_id,
        "score": score,
        "notes": notes,
        "timestamp": datetime.utcnow().isoformat(),
        "code": logic.strip()
    }

    leaderboard = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            leaderboard = json.load(f)

    leaderboard.append(entry)
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)[:10]  # Keep top 10 only

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f, indent=2)

def get_top_mutations():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []
