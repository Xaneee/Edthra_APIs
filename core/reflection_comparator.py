# core/reflection_comparator.py

from database import get_db
from utils.memory_utils import semantic_search

def compare_recent_cycles(limit=5):
    conn = get_db()
    c = conn.cursor()

    # Grab recent feedback logs
    c.execute("""
        SELECT title, content, tags FROM memories 
        WHERE tags LIKE '%feedback%' 
        ORDER BY rowid DESC LIMIT ?
    """, (limit,))
    logs = c.fetchall()

    if len(logs) < 2:
        return {"status": "Not enough logs for comparison."}

    # Sort logs by quality
    quality_order = {"excellent": 5, "great": 4, "fair": 3, "poor": 2, "broken": 1}
    parsed_logs = []

    for title, content, tags in logs:
        score = 0
        for key in quality_order:
            if key in tags.lower():
                score = quality_order[key]
                break
        parsed_logs.append({
            "title": title,
            "summary": content,
            "score": score
        })

    parsed_logs.sort(key=lambda x: -x["score"])

    # Compare top vs bottom
    best = parsed_logs[0]
    worst = parsed_logs[-1]

    return {
        "status": "Compared",
        "best_cycle": best,
        "worst_cycle": worst,
        "insight": f"Logic from '{best['title']}' is preferred over '{worst['title']}'. Future builds will favor that pattern."
    }
