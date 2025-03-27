from utils.planner_engine import generate_plan
from utils.reasoning_engine import generate_reasoning
from utils.code_mutator import safely_mutate_code
from database import get_db
from datetime import datetime

def spawn_agent(name, goal):
    plan = generate_plan(goal)
    reason = generate_reasoning(goal)

    log = f"[{datetime.now()}] AGENT: {name} | GOAL: {goal}\nREASONING: {reason}\nPLAN: {plan}"

    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO logs (timestamp, message, reason) VALUES (?, ?, ?)", (datetime.now().isoformat(), log, "agent"))
    conn.commit()

    # Bonus: execute a dummy mutation if goal says 'mutate'
    if "mutate" in goal.lower():
        safely_mutate_code("main.py", "from auth import auth_router", "# from auth import auth_router")

    return {
        "agent_name": name,
        "goal": goal,
        "status": "executed",
        "plan": plan,
        "reasoning": reason
    }
