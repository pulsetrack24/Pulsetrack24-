import requests

SHOPIFY_TOKEN = "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"
SHOPIFY_URL = "https://pulsetrack24.myshopify.com/admin/api/2023-10/products.json"

def upload_to_shopify(product):
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_TOKEN
    }
    data = {
        "product": {
            "title": product["title"],
            "body_html": product["description"],
            "vendor": "PulseTrack",
            "tags": "smart, wellness, tech",
            "variants": [{
                "price": str(product["price"]),
                "sku": product.get("gtin", "SMART-WELLNESS-001")
            }]
        }
    }
    try:
        response = requests.post(SHOPIFY_URL, json=data, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
