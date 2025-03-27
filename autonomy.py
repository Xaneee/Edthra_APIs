from fastapi import APIRouter
import json
import os
from datetime import datetime
import random
import requests

autonomy_router = APIRouter()
GOAL_FILE = "core/long_term_goals.json"
LOG_FILE = "core/autonomy_log.txt"

def log_action(entry):
    os.makedirs("core", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} :: {entry}\n")

@autonomy_router.post("/autonomy/loop")
def autonomy_loop():
    # Step 1: Load Goals
    if not os.path.exists(GOAL_FILE):
        return {"status": "No goals found."}
    
    with open(GOAL_FILE, "r") as f:
        goals = json.load(f)

    if not goals:
        return {"status": "No goals to process."}

    # Step 2: Pick one goal
    goal = random.choice(goals)
    log_action(f"Selected Goal: {goal['title']}")

    # Step 3: Simulate Thought (call /reason)
    try:
        response = requests.post("http://127.0.0.1:8000/reason", json={"prompt": goal["description"]})
        thought = response.json().get("response", "No clear thought.")
    except:
        thought = "Reasoning module unavailable."
    
    log_action(f"Thought: {thought}")

    # Step 4: Store Reflection
    reflection = {
        "goal": goal["title"],
        "thought": thought,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("core/last_autonomy_result.json", "w") as f:
        json.dump(reflection, f, indent=2)

    return {
        "status": "Autonomy cycle complete.",
        "processed_goal": goal["title"],
        "thought": thought
    }


@autonomy_router.get("/autonomy/logs")
def get_autonomy_logs():
    if not os.path.exists(LOG_FILE):
        return {"logs": [], "status": "No logs found."}

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    return {
        "logs": lines[-50:],  # return last 50 entries (or all)
        "total": len(lines)
    }
