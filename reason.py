from fastapi import APIRouter
from utils.reasoning_engine import generate_reasoning

reason_router = APIRouter()

@reason_router.post("/think")
def reason_through(goal: str):
    result = generate_reasoning(goal)
    return {"input": goal, "reasoning": result}
