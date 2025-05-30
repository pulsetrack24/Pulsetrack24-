
import requests

SHOP_URL = "3rr0n5-0u.myshopify.com"
ACCESS_TOKEN = "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"

def push_to_shopify(product):
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }
    data = {
        "product": {
            "title": product["title"],
            "body_html": product["description"],
            "tags": ", ".join(product["tags"]),
            "images": [{"src": src} for src in product.get("images", [])],
            "variants": [{
                "price": product["price"]
            }]
        }
    }
    url = f"https://{SHOP_URL}/admin/api/2023-10/products.json"
    response = requests.post(url, json=data, headers=headers)
    print("Shopify response:", response.status_code, response.text)
