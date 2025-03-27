def generate_plan(goal):
    if "api" in goal.lower():
        return [
            "Define endpoint structure",
            "Design database schema",
            "Connect FastAPI routes",
            "Test with Postman",
            "Deploy to local/remote server"
        ]
    elif "train model" in goal.lower():
        return [
            "Collect dataset",
            "Clean and preprocess data",
            "Select model architecture",
            "Train and evaluate",
            "Store results"
        ]
    return ["Step planning not defined yet for this goal."]
