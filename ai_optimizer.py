
def optimize_products(products):
    return [
        {
            **p,
            "title": p["title"].title(),
            "description": p["description"],
            "tags": p.get("tags", []),
            "profit_margin": round((p["price"] - p["cost"]) / p["cost"], 2)
        }
        for p in products if "price" in p and "cost" in p
    ]
