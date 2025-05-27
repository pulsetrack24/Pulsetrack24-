
import requests

SHOP_URL = "your-store.myshopify.com"
ACCESS_TOKEN = "your-shopify-access-token"

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
