import json
import os
from datetime import datetime

EMOTION_FILE = "core/emotion_state.json"
DECAY_RATE = 0.05  # 5% decay per cycle

def decay_emotions():
    if not os.path.exists(EMOTION_FILE):
        return

    with open(EMOTION_FILE, "r") as f:
        state = json.load(f)

    emotions = state.get("emotions", {})
    new_emotions = {}

    for emotion, value in emotions.items():
        decayed = round(max(0.0, value - DECAY_RATE), 2)
        if decayed > 0:
            new_emotions[emotion] = decayed

    state["emotions"] = new_emotions
    state["last_decay"] = datetime.utcnow().isoformat()

    with open(EMOTION_FILE, "w") as f:
        json.dump(state, f, indent=2)

    print("[🧘‍♀️] Emotions decayed. Current state:", new_emotions)
