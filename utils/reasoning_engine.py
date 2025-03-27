def generate_reasoning(goal):
    # Primitive logic engine (can be upgraded with LLM later)
    logic_map = {
        "build api": "APIs must include strong validation. I must define endpoints, connect to a database, and expose routes.",
        "mutate code": "I must back up the file before mutation., change target logic, and re-save safely.",
        "learn": "To learn, I must save new memory, analyze patterns, and test variations."
    }

    for key, logic in logic_map.items():
        if key in goal.lower():
            return logic

    return "I don't have a predefined plan. Try breaking the goal into smaller tasks or check knowledge base."
