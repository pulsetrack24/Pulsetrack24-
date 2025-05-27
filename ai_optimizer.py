def optimize_products(products):
    final = []
    for p in products:
        try:
            if (p["price"] - p["cost"]) / p["cost"] > 0.5:
                final.append(p)
        except:
            continue
    return final
