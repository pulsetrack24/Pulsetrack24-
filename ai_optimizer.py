def optimize_products(products):
    enriched = []
    for p in products:
        if "price" in p and "cost" in p:
            if (p["price"] - p["cost"]) / p["cost"] > 0.5:
                p["description"] = f"<strong>{p['title']}</strong> is one of the best herbal wellness products this season. Ideal for boosting vitality and balance."
                p["tags"] = ["herbal", "wellness", "tea", "bio", "health"]
                p["image_url"] = p.get("image_url", "https://cdn.pixabay.com/photo/2016/08/04/23/35/herbal-tea-1570072_1280.jpg")
                enriched.append(p)
    return enriched