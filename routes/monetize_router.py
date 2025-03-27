from fastapi import APIRouter
from core.monetization_planner import plan_monetization

monetize = APIRouter()

@monetize.post("/monetize/plan")
def generate_monetization(app_name: str, desc: str, features: int = 4):
    return plan_monetization(app_name, desc, features)
