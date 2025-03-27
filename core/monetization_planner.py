from core.pricing_engine import suggest_price

def plan_monetization(app_name: str, description: str, features: int = 4):
    complexity = "medium" if features <= 5 else "high"
    price = suggest_price(description, features, complexity)
    plan = {
        "app": app_name,
        "pricing": price,
        "strategy": "Freemium" if price == "$0 USD" else "One-time + Upgrade",
        "status": "ready"
    }
    return plan
