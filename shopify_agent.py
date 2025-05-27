# shopify_agent.py
import requests
from settings import SHOPIFY_API_TOKEN, SHOPIFY_STORE_URL, SHOPIFY_API_VERSION

def create_product(product_data):
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_API_TOKEN
    }
    url = f"{SHOPIFY_STORE_URL}/admin/api/{SHOPIFY_API_VERSION}/products.json"
    response = requests.post(url, json={"product": product_data}, headers=headers)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.status_code, response.text)
