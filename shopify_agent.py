import requests
import json
from settings import SHOPIFY_DOMAIN, SHOPIFY_ACCESS_TOKEN

def push_live_products(products):
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
    }
    endpoint = f"https://{SHOPIFY_DOMAIN}/admin/api/2023-10/products.json"

    for product in products:
        payload = {
            "product": {
                "title": product["title"],
                "body_html": product.get("description", "High quality product."),
                "vendor": product.get("vendor", "BioHealth"),
                "product_type": product.get("type", "Health"),
                "variants": [{
                    "price": product["price"],
                    "sku": product.get("gtin", "SKU0001")
                }]
            }
        }
        response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
        if not response.ok:
            raise Exception(f"Shopify API error: {response.text}")
    return "All products pushed successfully."