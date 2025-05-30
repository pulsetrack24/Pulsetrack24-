
import requests
import os

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_PASSWORD = os.getenv("SHOPIFY_PASSWORD")
SHOPIFY_STORE_NAME = os.getenv("SHOPIFY_STORE_NAME")
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")

BASE_URL = f"https://{SHOPIFY_STORE_NAME}.myshopify.com/admin/api/2023-10"

HEADERS = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
}

def get_products():
    url = f"{BASE_URL}/products.json"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def create_product(product_data):
    url = f"{BASE_URL}/products.json"
    response = requests.post(url, json={"product": product_data}, headers=HEADERS)
    return response.json()

def update_product(product_id, updated_data):
    url = f"{BASE_URL}/products/{product_id}.json"
    response = requests.put(url, json={"product": updated_data}, headers=HEADERS)
    return response.json()

def delete_product(product_id):
    url = f"{BASE_URL}/products/{product_id}.json"
    response = requests.delete(url, headers=HEADERS)
    return response.status_code == 200

def list_orders():
    url = f"{BASE_URL}/orders.json"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_order(order_id):
    url = f"{BASE_URL}/orders/{order_id}.json"
    response = requests.get(url, headers=HEADERS)
    return response.json()
