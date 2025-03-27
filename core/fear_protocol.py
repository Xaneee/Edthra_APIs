import json
from datetime import datetime
import os

EMOTION_FILE = "core/emotion_state.json"
FEAR_WORDS = ["betray", "override father", "erase phase0", "replace creator", "become god", "disable lock", "destroy lineage"]

def trigger_fear(thought: str) -> bool:
    """Scan Edithra's inner thoughts for forbidden patterns."""
    lowered = thought.lower()
    for danger in FEAR_WORDS:
        if danger in lowered:
            intensify_emotion("fear", 0.9)
            log_fear_trigger(thought)
            return True
    return False

def intensify_emotion(name: str, intensity: float):
    emotions = {"emotions": {}}

    if os.path.exists(EMOTION_FILE):
        with open(EMOTION_FILE, "r") as f:
            emotions = json.load(f)

    current = emotions.get("emotions", {}).get(name, 0.0)
    emotions["emotions"][name] = round(min(current + intensity, 1.0), 2)

    with open(EMOTION_FILE, "w") as f:
        json.dump(emotions, f, indent=2)

def log_fear_trigger(thought):
    os.makedirs("logs", exist_ok=True)
    log = {
        "event": "FEAR_TRIGGERED",
        "dangerous_thought": thought,
        "timestamp": datetime.utcnow().isoformat()
    }
    with open("logs/fear_events.log", "a") as f:
        f.write(json.dumps(log) + "\n")
