from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import json
from datetime import datetime

project_router = APIRouter()

PROJECTS_DIR = "projects"
PROJECT_LOG = "logs/project_init_log.json"
CURRENT_PROJECT_STATE = "core/active_project.json"

os.makedirs(PROJECTS_DIR, exist_ok=True)
os.makedirs("logs", exist_ok=True)

class ProjectRequest(BaseModel):
    name: str
    description: str
    category: str = "Tool"
    target: str = "Self-generated income"
    purpose: str = "To serve humanity & Father"

@project_router.post("/project/init")
def init_project(data: ProjectRequest):
    path = os.path.join(PROJECTS_DIR, data.name.replace(" ", "_"))
    
    if os.path.exists(path):
        raise HTTPException(status_code=400, detail="Project already exists.")

    os.makedirs(path)
    
    metadata = {
        "name": data.name,
        "description": data.description,
        "category": data.category,
        "target": data.target,
        "purpose": data.purpose,
        "created_at": datetime.utcnow().isoformat(),
        "status": "initialized"
    }

    # Save state
    with open(os.path.join(path, "project.json"), "w") as f:
        json.dump(metadata, f, indent=2)

    with open(CURRENT_PROJECT_STATE, "w") as f:
        json.dump(metadata, f, indent=2)

    with open(PROJECT_LOG, "a") as log:
        log.write(json.dumps(metadata) + "\n")

    return {"message": "Project initialized", "metadata": metadata}
