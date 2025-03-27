from fastapi import APIRouter
from utils.agent_core import spawn_agent

agent_router = APIRouter()

@agent_router.post("/spawn")
def spawn(name: str, goal: str):
    result = spawn_agent(name, goal)
    return result
