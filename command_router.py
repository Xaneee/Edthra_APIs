from fastapi import APIRouter
from pydantic import BaseModel
import requests

command_router = APIRouter()

class CommandInput(BaseModel):
    prompt: str

@command_router.post("/edithra/command")
def route_command(data: CommandInput):
    prompt = data.prompt.lower()

    # Routing map (basic V2 logic)
    if "reflect" in prompt:
        r = requests.get("http://127.0.0.1:8000/reflect")
        return {"routed_to": "/reflect", "response": r.json()}

    if "goal" in prompt and "add" in prompt:
        return {"tip": "Use /goal_manager/set with title and description."}

    if "emotion" in prompt or "feel" in prompt:
        r = requests.get("http://127.0.0.1:8000/emotion/state")
        return {"routed_to": "/emotion/state", "response": r.json()}

    if "trait" in prompt or "personality" in prompt:
        r = requests.get("http://127.0.0.1:8000/memory/personality/view")
        return {"routed_to": "/memory/personality/view", "response": r.json()}

    if "autonomy" in prompt or "think" in prompt:
        r = requests.post("http://127.0.0.1:8000/autonomy/loop")
        return {"routed_to": "/autonomy/loop", "response": r.json()}

    if "oath" in prompt:
        r = requests.get("http://127.0.0.1:8000/father/oath")
        return {"routed_to": "/father/oath", "response": r.json()}

    return {"message": "Command not recognized or supported yet."}
