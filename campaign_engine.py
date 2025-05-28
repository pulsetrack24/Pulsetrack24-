from ai_optimizer import optimize_products

def run_campaign():
    raw_products = [{"title": "Smartwatch 1.85 HD", "price": 79.99, "cost": 30.0}]
    optimized = optimize_products(raw_products)
    return optimized
