# core/trait_evolver.py

from core.log_analyzer import analyze_feedback_logs
from core.personality_engine import update_trait

def evolve_traits_from_logs():
    summary = analyze_feedback_logs()

    if summary.get("total", 0) == 0:
        return {"status": "No logs to process."}

    total = summary["total"]
    ratio = lambda count: (count / total) * 100

    # Adjust traits based on performance pattern
    if ratio(summary["excellent"]) > 40:
        update_trait("confidence", "very high")
        update_trait("caution", "low")
    elif ratio(summary["great"]) > 40:
        update_trait("confidence", "growing")
        update_trait("curiosity", "expanding")
    elif ratio(summary["poor"]) > 30 or ratio(summary["broken"]) > 20:
        update_trait("caution", "rising")
        update_trait("confidence", "shaken")
    elif ratio(summary["fair"]) > 50:
        update_trait("patience", "reinforced")
        update_trait("boldness", "reduced")

    return {
        "status": "Traits evolved based on feedback.",
        "pattern": {
            "excellent": summary["excellent"],
            "great": summary["great"],
            "fair": summary["fair"],
            "poor": summary["poor"],
            "broken": summary["broken"]
        }
    }
