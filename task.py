from fastapi import APIRouter
from utils.planner_engine import generate_plan

task_router = APIRouter()

@task_router.post("/plan")
def plan_task(goal: str):
    steps = generate_plan(goal)
    return {"goal": goal, "steps": steps}
