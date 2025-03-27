from database import get_db
from datetime import datetime
from utils.planner_engine import generate_plan
from utils.reasoning_engine import generate_reasoning

def create_agent(name, goal):
    plan = generate_plan(goal)
    reason = generate_reasoning(goal)
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO logs (timestamp, message, reason) VALUES (?, ?, ?)",
              (datetime.now().isoformat(), f"[Agent:{name}] Spawned with goal: {goal}", "agent"))
    conn.commit()
    return {
        "agent": name,
        "goal": goal,
        "reasoning": reason,
        "plan": plan
    }

def assign_task(agent, task):
    response = generate_reasoning(task)
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO logs (timestamp, message, reason) VALUES (?, ?, ?)",
              (datetime.now().isoformat(), f"[Agent:{agent}] Task: {task} → {response}", "agent-task"))
    conn.commit()
    return {
        "agent": agent,
        "task": task,
        "response": response
    }

def get_agent_logs():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT timestamp, message FROM logs WHERE reason LIKE 'agent%' ORDER BY id DESC LIMIT 20")
    logs = [{"time": t, "log": msg} for (t, msg) in c.fetchall()]
    return {"agent_activity": logs}

def debate_agents(agent_a, agent_b, topic):
    a_reason = generate_reasoning(topic + " - perspective A")
    b_reason = generate_reasoning(topic + " - perspective B")
    winner = agent_a if len(a_reason) < len(b_reason) else agent_b

    return {
        "topic": topic,
        "agent_a": {"name": agent_a, "opinion": a_reason},
        "agent_b": {"name": agent_b, "opinion": b_reason},
        "consensus": f"{winner} presented a stronger case (length-based heuristic)"
    }

def score_agent_decision(agent, outcome):
    conn = get_db()
    c = conn.cursor()
    score_log = f"[Agent:{agent}] Outcome: {outcome}"
    tag = "agent-win" if "success" in outcome.lower() else "agent-fail"
    c.execute("INSERT INTO logs (timestamp, message, reason) VALUES (?, ?, ?)",
              (datetime.now().isoformat(), score_log, tag))
    conn.commit()
    return {"agent": agent, "result": tag}


def reflect_as_team():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT reason FROM logs WHERE reason LIKE 'agent%'")
    reasons = [r[0] for r in c.fetchall()]
    total = len(reasons)
    wins = sum(1 for r in reasons if "win" in r)
    fails = sum(1 for r in reasons if "fail" in r)

    status = "improving" if wins >= fails else "needs calibration"

    return {
        "total_agent_outcomes": total,
        "successful_decisions": wins,
        "failed_attempts": fails,
        "team_status": status
    }
