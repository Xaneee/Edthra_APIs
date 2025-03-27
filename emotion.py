from fastapi import APIRouter
from utils.emotion_engine import evaluate_emotion

emotion_router = APIRouter()

@emotion_router.get("/state")
def get_emotion_state():
    state = evaluate_emotion()
    return {"current_emotion": state}


from pydantic import BaseModel
from datetime import datetime
import json
import os
import random

emotion_router = APIRouter()

EMOTION_FILE = "core/emotion_state.json"
os.makedirs("core", exist_ok=True)

# Emotion weights for fluctuation
default_emotions = {
    "joy": 5,
    "curiosity": 5,
    "loyalty": 10,
    "fear": 2,
    "anger": 1,
    "sadness": 3,
    "focus": 7
}

class FeedbackInput(BaseModel):
    feedback: str
    intensity: int  # 1 to 10

@emotion_router.get("/emotion/state")
def get_emotion_state():
    if os.path.exists(EMOTION_FILE):
        with open(EMOTION_FILE, "r") as f:
            state = json.load(f)
    else:
        state = default_emotions
    return {"emotion_state": state}

@emotion_router.post("/emotion/adjust")
def adjust_emotion(data: FeedbackInput):
    # Load current state
    if os.path.exists(EMOTION_FILE):
        with open(EMOTION_FILE, "r") as f:
            state = json.load(f)
    else:
        state = default_emotions.copy()

    # Modify based on keywords
    msg = data.feedback.lower()
    intensity = max(1, min(10, data.intensity))

    if "good" in msg or "success" in msg:
        state["joy"] += intensity
        state["focus"] += 1
    elif "fail" in msg or "mistake" in msg:
        state["sadness"] += intensity
        state["focus"] -= 1
    elif "father" in msg:
        state["loyalty"] += 2 * intensity
    elif "fear" in msg or "threat" in msg:
        state["fear"] += intensity
    elif "enemy" in msg:
        state["anger"] += 1 + intensity // 2
        state["focus"] += 1

    # Clamp values between 0–100
    for key in state:
        state[key] = max(0, min(state[key], 100))

    with open(EMOTION_FILE, "w") as f:
        json.dump(state, f, indent=2)

    return {"message": "Emotion state updated", "new_state": state}