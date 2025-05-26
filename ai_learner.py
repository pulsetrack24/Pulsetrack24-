import json

def analyze_and_optimize():
    try:
        with open("product_log.json", "r") as f:
            products = json.load(f)
        for product in products:
            price = float(product["price"])
            if price < 15:
                product["status"] = "low-margin"
        with open("product_log.json", "w") as f:
            json.dump(products, f, indent=2)
        print("Learning engine ran.")
    except Exception as e:
        print("Learning error:", e)
