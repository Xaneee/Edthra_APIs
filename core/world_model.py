from datetime import datetime

def simulate_event(event: str):
    timeline = {
        "initial_state": "neutral",
        "event": event,
        "simulated_outcome": f"Event '{event}' triggered reflection.",
        "world_shift": "minimal",
        "timestamp": datetime.utcnow().isoformat()
    }
    return timeline
