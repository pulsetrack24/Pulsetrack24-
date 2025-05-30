import os
import requests

SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_STORE_NAME = os.getenv("SHOPIFY_STORE_NAME")
SHOPIFY_API_VERSION = os.getenv("SHOPIFY_API_VERSION", "2024-04")

BASE_URL = f"https://{SHOPIFY_STORE_NAME}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}"

HEADERS = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
}

def get_products():
    url = f"{BASE_URL}/products.json"
    response = requests.get(url, headers=HEADERS)
    return response.json()
