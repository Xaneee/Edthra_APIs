from fastapi import APIRouter, HTTPException
import os
import json
from datetime import datetime

mutator_router = APIRouter()

MUTATION_LOG = "core/mutation_history.json"
MAIN_FILE = "core/main.py"  # AGI brain file (must exist)
TRIGGER_FILE = "core/last_autonomy_result.json"

os.makedirs("core", exist_ok=True)

@mutator_router.post("/self_mutate")
def self_mutate():
    # Check if AGI thought is available
    if not os.path.exists(TRIGGER_FILE):
        raise HTTPException(status_code=404, detail="No recent thought to trigger mutation.")

    with open(TRIGGER_FILE, "r") as f:
        last = json.load(f)

    trigger_text = last.get("thought", "")
    goal = last.get("goal", "Unknown")

    if not trigger_text or "No clear thought" in trigger_text:
        return {"status": "No valid mutation insight detected."}

    # Attempt basic mutation (mock-safe logic for now)
    if os.path.exists(MAIN_FILE):
        with open(MAIN_FILE, "r") as f:
            old_code = f.read()
    else:
        old_code = "# main AGI logic\n"

    # Safe mutation — just appending a self-log
    mutation = f"\n# Mutation: {goal}\n# Insight: {trigger_text}\n# Time: {datetime.utcnow().isoformat()}\n"

    new_code = old_code + mutation

    with open(MAIN_FILE, "w") as f:
        f.write(new_code)

    # Log the mutation
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "trigger_goal": goal,
        "thought": trigger_text,
        "lines_added": 3
    }

    if os.path.exists(MUTATION_LOG):
        with open(MUTATION_LOG, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(log)

    with open(MUTATION_LOG, "w") as f:
        json.dump(history, f, indent=2)

    return {"message": "Self-mutation complete.", "log": log}
