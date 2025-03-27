# File: utils/emotion_utils.py

import json
import os

def get_current_emotion():
    path = "core/emotion_state.json"
    if not os.path.exists(path):
        return "neutral"
    with open(path, "r") as f:
        state = json.load(f)
    emotions = state.get("emotions", {})
    if not emotions:
        return "neutral"
    return max(emotions, key=emotions.get)
