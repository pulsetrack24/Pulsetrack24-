import json

def log_products(products, file="product_log.json"):
    try:
        with open(file, "r") as f:
            data = json.load(f)
    except:
        data = []
    data.extend(products)
    with open(file, "w") as f:
        json.dump(data, f, indent=2)
