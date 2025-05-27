from ai_optimizer import optimize_products
from shopify_agent import upload_to_shopify
from autods_agent import get_products

def run_campaign():
    raw_products = get_products()
    optimized = optimize_products(raw_products)
    results = []

    for p in optimized:
        result = upload_to_shopify(p)
        results.append(result)
    return results
