import requests
from settings import SHOPIFY_STORE_URL, SHOPIFY_ACCESS_TOKEN

def sync_to_shopify(products):
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
                "vendor": "ProfitBot AI",
                "product_type": "Health AI",
                "tags": ",".join(p.get("tags", [])),
                "variants": [{
                    "price": str(p["price"]),
                    "sku": p["gtin"]
                }]
            }
        }
        r = requests.post(f"{SHOPIFY_STORE_URL}/admin/api/2023-10/products.json",
                          json=payload, headers=headers)
        result.append({
            "title": p["title"],
            "status": r.status_code,
            "response": r.json() if r.status_code == 201 else r.text
        })
    return result