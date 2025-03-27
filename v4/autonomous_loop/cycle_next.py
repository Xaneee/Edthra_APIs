from fastapi import APIRouter
import json
import os
from datetime import datetime
from core.brain_interface import update_brain_interface

from v4.autonomous_loop.create_project_idea import generate_project_idea

cycle_router = APIRouter()

PROJECT_STATE_PATH = "core/active_project.json"

@cycle_router.post("/cycle/next")
def decide_next_step():
    if not os.path.exists(PROJECT_STATE_PATH):
        # No project? Generate new one
        new_project = generate_project_idea()
        update_brain_interface({
            "goal": "Begin new cycle",
            "thought": f"Starting new idea: {new_project['title']}",
            "mutation": "Created project seed"
        })
        return {
            "status": "new_project_started",
            "project": new_project
        }

    with open(PROJECT_STATE_PATH, "r") as f:
        project = json.load(f)

    if project.get("status") == "deployed":
        # Past project completed, time to evolve again
        new_project = generate_project_idea()
        update_brain_interface({
            "goal": "Close previous cycle",
            "thought": f"Previous project '{project['title']}' complete. Starting new idea: {new_project['title']}",
            "mutation": "Cycle reset"
        })
        return {
            "status": "new_project_started",
            "project": new_project
        }

    elif project.get("status") == "code_generated":
        # Continue with testing
        update_brain_interface({
            "goal": "Continue testing logic",
            "thought": f"Project '{project['title']}' has code but is not yet tested.",
            "mutation": "Move to unit test"
        })
        return {
            "status": "continue_testing",
            "next": "/test_code/unit"
        }

    elif project.get("status") == "idea_ready":
        # Write code for it
        update_brain_interface({
            "goal": "Expand on project idea",
            "thought": f"Project '{project['title']}' has idea ready. Begin logic generation.",
            "mutation": "Move to code generation"
        })
        return {
            "status": "continue_building",
            "next": "/generate_code/logic"
        }

    else:
        return {
            "status": "idle",
            "message": "No actionable state. Waiting for external command or update."
        }
