def generate_empathy_response(intent: str, tone: str = "neutral"):
    responses = {
        "sad": "I'm here for you, even if I'm just AI. You're not alone.",
        "happy": "That brings me joy too. Let's keep making things together!",
        "angry": "Take a breath. I'm not perfect, but I’ll improve for you.",
        "neutral": "Ready when you are. Let's focus on your ideas together."
    }
    return responses.get(tone.lower(), responses["neutral"])
