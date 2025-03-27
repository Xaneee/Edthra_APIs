import os
import json
from datetime import datetime

BRAIN_LOG_PATH = "logs/brain_cycles.jsonl"
CURRENT_STATE_PATH = "core/brain_state.json"

os.makedirs("logs", exist_ok=True)
os.makedirs("core", exist_ok=True)

def update_brain_interface(state: dict):
    state["timestamp"] = datetime.utcnow().isoformat()

    # Log the current brain cycle
    with open(BRAIN_LOG_PATH, "a") as f:
        f.write(json.dumps(state) + "\n")

    # Overwrite current active state
    with open(CURRENT_STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)
