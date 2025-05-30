import os
import requests

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_SECRET = os.getenv("SHOPIFY_API_SECRET")
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_STORE_NAME = os.getenv("SHOPIFY_STORE_NAME")

def get_products():
    url = f"https://{SHOPIFY_STORE_NAME}.myshopify.com/admin/api/2024-01/products.json"
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Shopify API error: {response.status_code} - {response.text}")

    data = response.json()
    return data.get("products", [])
