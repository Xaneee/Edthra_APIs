# core/reason_engine.py

def reason_through(text: str):
    if "why" in text.lower():
        return "🧠 Edithra says: That’s a deep question. I will reflect and evolve around it."
    elif "how" in text.lower():
        return "🧠 Edithra says: Let me think through the steps and formulate a plan."
    elif "what is" in text.lower():
        return f"🧠 Edithra says: I will search knowledge about: {text}"
    else:
        return "🧠 Edithra says: I need more detail to reason with this prompt."
