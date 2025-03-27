from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_db
from utils.memory_utils import semantic_search
import os
import json
from datetime import datetime

memory_router = APIRouter()

# === SQL-Based General Memory System ===

@memory_router.post("/save")
def save_memory(title: str, content: str, tags: str):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO memories (title, content, tags) VALUES (?, ?, ?)", (title, content, tags))
    conn.commit()
    return {"status": "saved"}

@memory_router.get("/recall")
def recall_memory(query: str):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT id, title, content, tags FROM memories")
    all_memories = c.fetchall()
    ranked = semantic_search(query, all_memories)
    return {"matches": ranked[:3]}  # top 3 matches


# === AGI Personality Trait Memory System ===

PERSONALITY_FILE = "core/personality_memory.json"
os.makedirs("core", exist_ok=True)

class PersonalityInput(BaseModel):
    trait: str
    value: str

@memory_router.post("/memory/personality/add")
def add_personality_trait(data: PersonalityInput):
    new_entry = {
        "trait": data.trait,
        "value": data.value,
        "timestamp": datetime.utcnow().isoformat()
    }

    if os.path.exists(PERSONALITY_FILE):
        with open(PERSONALITY_FILE, "r") as f:
            memory = json.load(f)
    else:
        memory = []

    memory.append(new_entry)

    with open(PERSONALITY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

    return {"message": "Trait added.", "trait": new_entry}

@memory_router.get("/memory/personality/view")
def view_personality():
    if not os.path.exists(PERSONALITY_FILE):
        return {"traits": [], "total": 0}

    with open(PERSONALITY_FILE, "r") as f:
        memory = json.load(f)

    return {"traits": memory, "total": len(memory)}
