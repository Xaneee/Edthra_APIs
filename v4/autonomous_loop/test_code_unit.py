from fastapi import APIRouter, HTTPException
import subprocess
import os
import json
from datetime import datetime
from core.brain_interface import update_brain_interface

code_tester_router = APIRouter()

PROJECT_STATE_PATH = "core/active_project.json"
LOG_PATH = "logs/test_output_log.jsonl"

def run_python_script(path: str):
    try:
        result = subprocess.run(
            ["python", path],
            capture_output=True,
            text=True,
            timeout=20
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "exit_code": result.returncode
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "exit_code": -1
        }

@code_tester_router.post("/test_code/unit")
def test_code():
    if not os.path.exists(PROJECT_STATE_PATH):
        raise HTTPException(status_code=404, detail="No active project found.")

    with open(PROJECT_STATE_PATH, "r") as f:
        idea = json.load(f)

    title = idea["title"].replace(" ", "_")
    code_path = f"projects/{title}/main.py"

    if not os.path.exists(code_path):
        raise HTTPException(status_code=404, detail="No code file found to test.")

    result = run_python_script(code_path)

    # Update brain interface
    update_brain_interface({
        "goal": f"Test project: {idea['title']}",
        "thought": "Running self-generated logic to verify correctness.",
        "project": idea['title'],
        "mutation": f"Test {'passed' if result['success'] else 'failed'}",
        "error": result['stderr'] if not result['success'] else None
    })

    # Log test result
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as f:
        result["timestamp"] = datetime.utcnow().isoformat()
        result["project"] = idea['title']
        f.write(json.dumps(result) + "\n")

    return {
        "message": "Code tested.",
        "success": result["success"],
        "output": result["stdout"],
        "error": result["stderr"],
        "exit_code": result["exit_code"]
    }
