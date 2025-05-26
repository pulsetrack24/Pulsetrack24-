import requests

SHOPIFY_ACCESS_TOKEN = "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"
SHOPIFY_DOMAIN = "pulsetrack24.myshopify.com"

def push_product_to_shopify(product):
    url = f"https://{SHOPIFY_DOMAIN}/admin/api/2023-01/products.json"
    headers = {"X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN}
    payload = {
        "product": {
            "title": product["title"],
            "body_html": "<strong>Bio Health Tracker</strong>",
            "vendor": "QSTAR AI",
            "product_type": "Bio Health",
            "variants": [{
                "price": product["price"],
                "sku": product["gtin"]
            }]
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.ok
