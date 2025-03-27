# core/mutation_rater.py

from core.intelligence_score import score_python_code

def rate_mutations(mutation_list):
    """
    Accepts a list of code mutations and returns them ranked by final score.
    Each mutation should be a dict: { "id": str, "code": str }
    """
    scored = []

    for mutation in mutation_list:
        result = score_python_code(mutation["code"])
        scored.append({
            "id": mutation["id"],
            "score": result.get("final_score", 0),
            "details": result
        })

    # Sort descending by score
    return sorted(scored, key=lambda x: x["score"], reverse=True)

def top_mutation(mutation_list):
    """
    Returns only the top-rated mutation's full record
    """
    ranked = rate_mutations(mutation_list)
    return ranked[0] if ranked else None
