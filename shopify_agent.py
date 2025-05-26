import os
import requests
from ai_writer import generate_description

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_PASSWORD = os.getenv("SHOPIFY_PASSWORD")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")

def push_live_products():
    headers = {
        "Content-Type": "application/json"
    }
    auth = (SHOPIFY_API_KEY, SHOPIFY_PASSWORD)

    sample_products = [
        {
            "title": "Smart Health Ring Pro",
            "gtin": "GTIN5678901",
            "price": "39.99",
            "image_url": "https://via.placeholder.com/250"
        },
        {
            "title": "Bio Tracker Band V2",
            "gtin": "GTIN5678902",
            "price": "29.50",
            "image_url": "https://via.placeholder.com/250"
        }
    ]

    for product in sample_products:
        description, tags = generate_description(product["title"])
        payload = {
            "product": {
                "title": product["title"],
                "body_html": description,
                "vendor": "QSTAR AI",
                "product_type": "Bio Health",
                "tags": tags,
                "variants": [{
                    "price": product["price"],
                    "sku": product["gtin"]
                }],
                "images": [{"src": product["image_url"]}]
            }
        }

        url = f"https://{SHOPIFY_STORE_URL}/admin/api/2023-10/products.json"
        response = requests.post(url, auth=auth, json=payload, headers=headers)
        print("Shopify Upload:", response.status_code)
