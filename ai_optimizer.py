def optimize_products(products):
    result = []
    for p in products:
        if (p["price"] - p["cost"]) / p["cost"] > 0.5:
            p["description"] = f"AI-Optimized: {p['title']} boosts wellness."
            p["tags"] = ["bio", "health", "ai-optimized"]
            result.append(p)
    return result