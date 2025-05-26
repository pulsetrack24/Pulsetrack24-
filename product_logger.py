import json

def log_products(products, filename="product_log.json"):
    with open(filename, "w") as f:
        json.dump(products, f)
