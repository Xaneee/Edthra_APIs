from fastapi import APIRouter
from core.empathy_engine import generate_empathy_response
from core.user_persona_manager import get_user_profile

empathy = APIRouter()

@empathy.post("/empathy/respond")
def respond(intent: str, tone: str = "neutral"):
    response = generate_empathy_response(intent, tone)
    user = get_user_profile()
    return {"response": f"{user['name']}, {response}"}
