
from ai_optimizer import optimize_products
from shopify_agent import push_to_shopify
from autodds_agent import push_to_autods

def run_campaign():
    # Dummy product with full data for testing
    raw_products = [{
        "title": "Ultra Smart Health Watch",
        "description": "Advanced AI-generated product",
        "tags": ["health", "wearable", "fitness"],
        "price": 49.99,
        "cost": 19.99,
        "images": ["https://example.com/smartwatch.jpg"]
    }]
    optimized = optimize_products(raw_products)
    for product in optimized:
        push_to_shopify(product)
        push_to_autods(product)
    return {"status": "Live sync complete", "products_synced": optimized}
