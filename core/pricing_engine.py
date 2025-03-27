def suggest_price(app_description: str, features: int = 3, complexity: str = "medium"):
    base = 10
    if complexity == "high":
        base += 15
    elif complexity == "low":
        base -= 5
    price = base + features * 5
    return f"${price} USD"
