from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.goal_utils import current_goal
from utils.memory_utils import recall_related_memories
from utils.emotion_utils import get_current_emotion
import random

reason_router = APIRouter()

class ReasonOutput(BaseModel):
    goal: str
    emotion: str
    context: list[str]
    generated_thought: str

@reason_router.get("/reason/contextual", response_model=ReasonOutput)
def contextual_reasoning():
    goal = current_goal()
    if not goal:
        raise HTTPException(status_code=400, detail="No active goal set.")

    emotion = get_current_emotion()
    context_memories = recall_related_memories(goal)

    # Thought synthesis logic
    base_thought = f"To fulfill my goal of '{goal}', I must consider the emotion '{emotion}' and insights from memory."

    if context_memories:
        memory_influence = random.choice(context_memories)["content"]
        generated = f"{base_thought} One idea is: {memory_influence}."
    else:
        generated = f"{base_thought} No strong memories found. I must explore a new approach."

    return {
        "goal": goal,
        "emotion": emotion,
        "context": context_memories,
        "generated_thought": generated
    }
