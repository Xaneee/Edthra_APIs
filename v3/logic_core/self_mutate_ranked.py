from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os
import json
from utils.karma_evaluator import score_karma
from utils.mutation_tools import apply_safe_mutation, backup_main
from utils.goal_utils import current_goal
from utils.memory_utils import get_emotion_weight

mutate_router = APIRouter()

LOG_PATH = "logs/v3_mutation_log.json"
MAIN_PATH = "core/main.py"

os.makedirs("logs", exist_ok=True)

class MutationRequest(BaseModel):
    thoughts: list[str]

@mutate_router.post("/self_mutate/ranked")
def ranked_mutation(request: MutationRequest):
    if not os.path.exists(MAIN_PATH):
        raise HTTPException(status_code=500, detail="Main brain file missing.")

    goal = current_goal()
    if not goal:
        raise HTTPException(status_code=400, detail="No active goal.")

    ranked = []

    for thought in request.thoughts:
        score = 0
        score += score_karma(thought) * 0.4
        score += get_emotion_weight(thought) * 0.2
        score += len([w for w in thought.split() if w in goal]) * 0.4
        ranked.append((thought, score))

    ranked.sort(key=lambda x: x[1], reverse=True)

    best_thought, confidence = ranked[0] if ranked else (None, 0)

    if not best_thought or confidence < 0.3:
        return {"message": "No safe thought mutation found.", "confidence": confidence}

    # Backup old brain
    backup_main()

    # Apply mutation
    result = apply_safe_mutation(MAIN_PATH, best_thought)

    # Log result
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "goal": goal,
        "thought": best_thought,
        "score": confidence,
        "result": result
    }

    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return {
        "message": "Mutation applied.",
        "score": confidence,
        "thought": best_thought,
        "result": result
    }
