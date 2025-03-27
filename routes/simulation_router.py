from fastapi import APIRouter
from core.world_model import simulate_event
from core.self_projection import project_self_evolution

sim = APIRouter()

@sim.post("/simulate/event")
def simulate(event: str):
    return simulate_event(event)

@sim.post("/simulate/self")
def project(phase: str, goal: str):
    return project_self_evolution(phase, goal)
