from ai_optimizer import optimize_products

def fetch_smart_health_products():
    return [{"title": "Smartwatch 1.85 HD", "price": 79.99, "cost": 30.00}]

def run_campaign():
    raw_products = fetch_smart_health_products()
    optimized = optimize_products(raw_products)
    return {
        "optimized": optimized,
        "status": "success"
    }
