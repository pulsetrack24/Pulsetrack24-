import requests
from settings import SHOPIFY_ACCESS_TOKEN, SHOPIFY_STORE_URL

def push_to_shopify(products):
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
    }
    result = []
    for p in products:
        payload = {
            "product": {
                "title": p["title"],
                "body_html": p["description"],
                "tags": ",".join(p["tags"]),
                "variants": [{
                    "price": str(p["price"]),
                    "sku": p["gtin"]
                }]
            }
        }
        url = f"{SHOPIFY_STORE_URL}/admin/api/2023-10/products.json"
        res = requests.post(url, json=payload, headers=headers)
        result.append(res.json() if res.ok else res.text)
    return result