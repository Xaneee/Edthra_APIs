# core/logic_reinforcer.py

from database import get_db
from collections import defaultdict

def build_logic_patterns():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
        SELECT title, content, tags FROM memories 
        WHERE tags LIKE '%feedback%' 
        ORDER BY rowid DESC LIMIT 30
    """)
    logs = c.fetchall()

    pattern_counts = defaultdict(int)
    success_signatures = defaultdict(int)
    failure_signatures = defaultdict(int)

    for title, content, tags in logs:
        lines = content.split("\n")
        for line in lines:
            if "def " in line or "import" in line or "class " in line:
                signature = line.strip()
                pattern_counts[signature] += 1

                if "excellent" in tags.lower() or "great" in tags.lower():
                    success_signatures[signature] += 1
                elif "poor" in tags.lower() or "broken" in tags.lower():
                    failure_signatures[signature] += 1

    # Scoring logic preference
    trusted_logic = []
    risky_logic = []

    for sig, total in pattern_counts.items():
        success_rate = success_signatures[sig] / total if total > 0 else 0
        if success_rate > 0.7 and total >= 2:
            trusted_logic.append(sig)
        elif failure_signatures[sig] > success_signatures[sig]:
            risky_logic.append(sig)

    return {
        "trusted_patterns": trusted_logic or ["No strong logic pattern found."],
        "risky_patterns": risky_logic or ["No obvious risky logic found."]
    }
