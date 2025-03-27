# core/intelligence_score.py

import ast

def score_python_code(code: str) -> dict:
    """
    Gives Edithra a score for logic quality, readability, structure, and optimization
    """
    score = {
        "structure": 0,
        "readability": 0,
        "functionality": 0,
        "length": len(code),
        "final_score": 0
    }

    try:
        tree = ast.parse(code)

        score["structure"] = len([node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.ClassDef))])
        score["readability"] = code.count("\n")  # crude but improves with indentation and spacing
        score["functionality"] = code.count("return") + code.count("import")

        score["final_score"] = (
            score["structure"] * 3 +
            score["readability"] * 1 +
            score["functionality"] * 2
        )

    except Exception as e:
        score["error"] = str(e)
        score["final_score"] = 0

    return score
