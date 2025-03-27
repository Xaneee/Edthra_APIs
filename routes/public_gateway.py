from fastapi import APIRouter

gateway = APIRouter()

@gateway.post("/public_task")
def public_task(title: str, goal: str):
    from core.task_planner import plan_task
    return plan_task(title, goal)
