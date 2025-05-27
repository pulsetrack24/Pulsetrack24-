import requests
from settings import SHOP_DOMAIN, SHOPIFY_TOKEN

def sync_shopify_products(products):
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_TOKEN,
        "Content-Type": "application/json"
    }
    for product in products:
        payload = {
            "product": {
                "title": product["title"],
                "body_html": product["description"],
                "vendor": "Pulse Track",
                "product_type": "Bio Health",
                "variants": [{"price": product["price"]}]
            }
        }
        url = f"https://{SHOP_DOMAIN}/admin/api/2023-10/products.json"
        response = requests.post(url, json=payload, headers=headers)
        print("Shopify response:", response.status_code, response.text)