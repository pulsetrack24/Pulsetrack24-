import requests

SHOPIFY_ACCESS_TOKEN = "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"
SHOP_URL = "pulsetrack24.myshopify.com"

def push_product_to_shopify(product):
    endpoint = f"https://{SHOP_URL}/admin/api/2023-01/products.json"
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "product": {
            "title": product["title"],
            "body_html": "<strong>Top Bio Health Product</strong>",
            "vendor": "QSTAR AI",
            "product_type": "Health",
            "variants": [
                {
                    "price": product["price"],
                    "sku": product["gtin"]
                }
            ]
        }
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.status_code == 201
