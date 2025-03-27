# core/feedback_engine.py

import random
from datetime import datetime
from utils.memory_utils import save_memory

# Cognitive score mapping
score_levels = {
    "excellent": (90, 100),
    "great": (75, 89),
    "fair": (60, 74),
    "poor": (40, 59),
    "broken": (0, 39)
}

def score_logic_quality(code: str) -> dict:
    """
    Very basic scoring simulation (later this will use real testing / AI review).
    """
    if "import" in code and "def " in code:
        base_score = random.randint(70, 95)
    elif "def " in code:
        base_score = random.randint(50, 70)
    else:
        base_score = random.randint(20, 50)

    level = next(name for name, (low, high) in score_levels.items() if low <= base_score <= high)
    return {
        "score": base_score,
        "rating": level
    }

def save_feedback(file: str, score: int, rating: str, context: str = ""):
    log = f"[{datetime.utcnow().isoformat()}] File: {file} scored {score} ({rating}) | {context}"
    save_memory(
        title=f"Score for {file}",
        content=log,
        tags=f"feedback,{rating},{context}"
    )
