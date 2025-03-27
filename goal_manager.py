from fastapi import APIRouter
from pydantic import BaseModel
import json
import os
from datetime import datetime

goal_router = APIRouter()

GOAL_FILE = "core/long_term_goals.json"
os.makedirs("core", exist_ok=True)

class GoalInput(BaseModel):
    title: str
    description: str

@goal_router.post("/goal_manager/set")
def set_goal(goal: GoalInput):
    data = {
        "title": goal.title,
        "description": goal.description,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Create or append goal
    if os.path.exists(GOAL_FILE):
        with open(GOAL_FILE, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(data)

    with open(GOAL_FILE, "w") as f:
        json.dump(existing, f, indent=2)

    return {"message": "Goal added successfully.", "goal": data}


@goal_router.get("/goal_manager/list")
def list_goals():
    if not os.path.exists(GOAL_FILE):
        return {"goals": []}

    with open(GOAL_FILE, "r") as f:
        goals = json.load(f)

    return {"goals": goals, "total": len(goals)}
