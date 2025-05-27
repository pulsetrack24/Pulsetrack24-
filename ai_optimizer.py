def smart_optimize(products):
    # Filter by profit margin and apply AI targeting
    filtered = [p for p in products if (p["price"] - p["cost"]) / p["cost"] > 0.5]
    for p in filtered:
        p["description"] = f"AI-Optimized: {p['title']} improves wellness naturally."
        p["tags"] = ["ai", "health", "bio", "campaign"]
        p["keywords"] = ["wellness", "bio tracker", "detox", "boost"]
    return filtered