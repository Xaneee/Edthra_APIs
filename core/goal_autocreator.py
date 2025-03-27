# core/goal_autocreator.py

from database import get_db
from datetime import datetime

def auto_generate_goals_from_feedback():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
        SELECT title, content, tags FROM memories 
        WHERE tags LIKE '%feedback%' 
        ORDER BY rowid DESC LIMIT 10
    """)
    logs = c.fetchall()

    weak_points = []
    for title, content, tags in logs:
        tag_lower = tags.lower()
        if "poor" in tag_lower or "broken" in tag_lower:
            weak_points.append((title, content))

    created_goals = []
    for wp in weak_points:
        goal_title = f"Fix: {wp[0]}"
        goal_reason = wp[1][:200]

        c.execute("""
            INSERT INTO goals (title, reason, created_at, status) 
            VALUES (?, ?, ?, ?)
        """, (goal_title, goal_reason, datetime.utcnow().isoformat(), "pending"))
        created_goals.append(goal_title)

    conn.commit()
    return {
        "status": "generated",
        "goals": created_goals or ["No weak points found."]
    }
