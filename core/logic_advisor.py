# core/logic_advisor.py

from core.intelligence_score import score_python_code
from utils.memory_utils import semantic_score

def choose_best_direction(prompt: str, code_options: list):
    """
    Analyzes code options against the prompt.
    Returns the best candidate with reasoning.
    Each option must be: { "id": str, "code": str }
    """
    decisions = []

    for option in code_options:
        logic_score = score_python_code(option["code"])
        relevance = semantic_score(prompt, option["code"])
        combined = (logic_score["final_score"] * 0.7) + (relevance * 0.3)

        decisions.append({
            "id": option["id"],
            "score": logic_score["final_score"],
            "relevance": relevance,
            "combined": combined,
            "code": option["code"]
        })

    best = max(decisions, key=lambda x: x["combined"])
    return {
        "best_id": best["id"],
        "reasoning": f"High logic score ({best['score']}) + relevance ({best['relevance']})",
        "code": best["code"]
    }
