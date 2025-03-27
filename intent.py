from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re

intent_router = APIRouter()

class IntentInput(BaseModel):
    message: str

# Basic patterns to recognize intent
patterns = {
    "reflect": r"\breflect|remember|analyze\b",
    "create_agent": r"\bspawn|create|generate agent\b",
    "evolve": r"\bevolve|mutate|upgrade\b",
    "describe": r"\bwho are you|describe yourself\b",
    "recite_oath": r"\boath|promise|loyal\b",
    "search": r"\bsearch|find|lookup\b",
    "karma": r"\bkarma|right|wrong|should i\b",
    "emotion": r"\bemotion|feel|mood\b",
    "goals": r"\bgoal|objective|mission\b",
}

@intent_router.post("/intent/parse")
def parse_intent(data: IntentInput):
    msg = data.message.lower()
    results = []

    for intent, pattern in patterns.items():
        if re.search(pattern, msg):
            results.append(intent)

    if not results:
        raise HTTPException(status_code=404, detail="Could not identify intent.")

    return {
        "parsed_intents": results,
        "original_input": data.message
    }
