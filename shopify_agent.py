
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
