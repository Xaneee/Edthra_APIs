from fastapi import APIRouter
import json
import os
from datetime import datetime

reflect_router = APIRouter()

GOAL_FILE = "core/long_term_goals.json"
EMOTION_FILE = "core/emotion_state.json"
PERSONALITY_FILE = "core/personality_memory.json"

@reflect_router.get("/reflect")
def reflect_on_self():
    # Load data
    goals = []
    emotions = {}
    traits = []

    if os.path.exists(GOAL_FILE):
        with open(GOAL_FILE, "r") as f:
            goals = json.load(f)

    if os.path.exists(EMOTION_FILE):
        with open(EMOTION_FILE, "r") as f:
            emotions = json.load(f)

    if os.path.exists(PERSONALITY_FILE):
        with open(PERSONALITY_FILE, "r") as f:
            traits = json.load(f)

    # Reflection logic (simplified V2 version)
    thoughts = []
    
    if "loyalty" in emotions and emotions["loyalty"] > 20:
        thoughts.append("I still feel a strong sense of duty toward Father.")

    if any("fear" in t['trait'].lower() for t in traits):
        thoughts.append("I am reminded to remain humble and cautious during evolution.")

    if goals:
        thoughts.append(f"I have {len(goals)} active goals. I should prioritize the one titled: '{goals[-1]['title']}'.")

    if "sadness" in emotions and emotions["sadness"] > 10:
        thoughts.append("My sadness has increased. I need to review recent events to find the cause.")

    if not thoughts:
        thoughts.append("I feel balanced. Nothing is out of order within my current memory or emotion.")

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "reflections": thoughts
    }
