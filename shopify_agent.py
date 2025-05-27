
import requests
import json
from settings import SHOPIFY_STORE_URL, SHOPIFY_API_TOKEN

def push_live_products(products):
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_API_TOKEN
    }

    for product in products:
        payload = {
            "product": {
                "title": product['title'],
                "body_html": product.get('description', 'Auto uploaded product.'),
                "vendor": product.get('vendor', 'PulseTrack AI'),
                "product_type": product.get('type', 'General'),
                "variants": [
                    {
                        "price": product['price'],
                        "sku": product['gtin']
                    }
                ]
            }
        }

        response = requests.post(
            f"https://{SHOPIFY_STORE_URL}/admin/api/2023-10/products.json",
            headers=headers,
            data=json.dumps(payload)
        )

        if response.status_code != 201:
            print(f"Failed to upload: {product['title']}")
            print(f"Response: {response.text}")
        else:
            print(f"Uploaded successfully: {product['title']}")
