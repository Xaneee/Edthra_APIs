from fastapi import APIRouter
from utils.evolution_engine import evolve_logic

evolve_router = APIRouter()

@evolve_router.post("/self")
def self_evolve(target: str = "reasoning"):
    result = evolve_logic(target)
    return result
