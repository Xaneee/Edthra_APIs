# core/log_analyzer.py

import sqlite3
from datetime import datetime
from utils.memory_utils import semantic_search
from database import get_db

def analyze_feedback_logs():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
        SELECT title, content, tags FROM memories 
        WHERE tags LIKE '%feedback%' 
        ORDER BY rowid DESC LIMIT 20
    """)
    logs = c.fetchall()

    if not logs:
        return {"message": "No feedback logs yet."}

    result_summary = {
        "excellent": 0,
        "great": 0,
        "fair": 0,
        "poor": 0,
        "broken": 0,
        "total": len(logs),
        "insights": []
    }

    for log in logs:
        title, content, tags = log
        tag_set = tags.lower().split(",")
        for level in result_summary:
            if level in tag_set:
                result_summary[level] += 1

        result_summary["insights"].append({
            "title": title,
            "summary": content
        })

    return result_summary
