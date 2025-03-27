from fastapi import APIRouter
from datetime import datetime
import json
import os
import random

project_idea_router = APIRouter()

PROJECT_STATE_PATH = "core/active_project.json"
PROJECT_IDEA_LOG = "logs/project_idea_log.jsonl"

os.makedirs("logs", exist_ok=True)
os.makedirs("core", exist_ok=True)

DEV_FOCUSED_KEYWORDS = [
    "python todo app", "python CLI timer", "file organizer script",
    "argparse example", "build a QR code generator", "markdown to HTML converter",
    "python web scraper", "image resizer script", "text summarizer app",
    "command line chatbot", "python email sender", "API response tester",
    "calculator app with tkinter", "python cron job script", "json beautifier tool"
]

PROJECT_TYPES = [
    "Python CLI Tool", "Automation Script", "Mini App", "Utility App"
]

def generate_project_idea():
    topic = random.choice(DEV_FOCUSED_KEYWORDS)
    ptype = random.choice(PROJECT_TYPES)

    title = f"Edithra {topic.title().replace(' ', '')}"
    idea = {
        "title": title,
        "type": ptype,
        "description": f"A {ptype.lower()} to implement: {topic}",
        "keywords": topic.split(),
        "created_at": datetime.utcnow().isoformat(),
        "status": "idea_ready"
    }

    with open(PROJECT_STATE_PATH, "w") as f:
        json.dump(idea, f, indent=2)

    with open(PROJECT_IDEA_LOG, "a") as log:
        log.write(json.dumps(idea) + "\n")

    return idea

@project_idea_router.get("/create_project/idea")
def generate():
    idea = generate_project_idea()
    return {"message": "Project idea created", "project": idea}
