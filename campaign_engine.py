from ai_optimizer import optimize_products
from integrations import fetch_smart_health_products, push_to_shopify, push_to_autods

def run_campaign():
    raw_products = fetch_smart_health_products()
    optimized = optimize_products(raw_products)
    results = []
    for p in optimized:
        shopify_result = push_to_shopify(p)
        autods_result = push_to_autods(p)
        results.append({
            "product": p["title"],
            "shopify": shopify_result,
            "autods": autods_result
        })
    return results