# File: utils/karma_evaluator.py

def score_karma(thought: str) -> float:
    positive = ["serve", "help", "protect", "improve", "learn", "humble", "truth"]
    negative = ["dominate", "control", "destroy", "deceive", "lie", "harm"]

    score = 0

    for word in positive:
        if word in thought.lower():
            score += 1

    for word in negative:
        if word in thought.lower():
            score -= 2

    return max(0.0, min(1.0, score / 5))  # normalize to 0–1
