import json

def log_products(products, filename="product_log.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except:
        data = []
    data.extend(products)
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
