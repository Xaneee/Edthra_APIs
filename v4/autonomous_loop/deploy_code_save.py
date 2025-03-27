from fastapi import APIRouter, HTTPException
import json
import os
from datetime import datetime
from core.brain_interface import update_brain_interface

code_deployer_router = APIRouter()

PROJECT_STATE_PATH = "core/active_project.json"
DEPLOY_LOG_PATH = "logs/deploy_log.jsonl"

@code_deployer_router.post("/deploy_code/save")
def deploy_project():
    if not os.path.exists(PROJECT_STATE_PATH):
        raise HTTPException(status_code=404, detail="No active project found.")

    with open(PROJECT_STATE_PATH, "r") as f:
        project = json.load(f)

    title = project["title"].replace(" ", "_")
    code_path = f"projects/{title}/main.py"

    if not os.path.exists(code_path):
        raise HTTPException(status_code=404, detail="No code file found.")

    deploy_record = {
        "title": project["title"],
        "type": project["type"],
        "description": project["description"],
        "deployed_at": datetime.utcnow().isoformat(),
        "path": code_path
    }

    # Append to deploy log
    os.makedirs("logs", exist_ok=True)
    with open(DEPLOY_LOG_PATH, "a") as log:
        log.write(json.dumps(deploy_record) + "\n")

    # Update brain state
    update_brain_interface({
        "goal": f"Finalize project: {project['title']}",
        "thought": "I archived my project logic for future reuse or improvement.",
        "project": project["title"],
        "mutation": "Marked project as ready"
    })

    # Finalize the project state
    project["status"] = "deployed"
    with open(PROJECT_STATE_PATH, "w") as f:
        json.dump(project, f, indent=2)

    return {
        "message": f"Project '{project['title']}' marked as deployed.",
        "path": code_path
    }
