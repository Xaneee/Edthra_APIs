# core/thought_planner.py

import random
from datetime import datetime
from utils.memory_utils import save_memory

def refine_strategy(goal_title, current_thought=""):
    strategies = [
        "Split the project into smaller modules",
        "Search for similar open-source projects for inspiration",
        "Redesign the input/output logic",
        "Scrap and replan the project from scratch",
        "Change the UI/UX layout to improve user flow",
        "Restructure database schema to simplify logic",
        "Generate test-driven architecture instead of mutation-based only"
    ]

    chosen = random.choice(strategies)
    timestamp = datetime.utcnow().isoformat()

    save_memory(
        title=f"Strategic Shift for: {goal_title}",
        content=f"{timestamp} — Edithra reflected and updated strategy:\nOld Thought: {current_thought}\nNew Strategy: {chosen}",
        tags="strategy,thought,refactor"
    )

    return {
        "goal": goal_title,
        "new_strategy": chosen,
        "timestamp": timestamp
    }
