
import requests
from settings import SHOPIFY_STORE_DOMAIN, SHOPIFY_ACCESS_TOKEN

def push_live_products(products):
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
    }
    for product in products:
        response = requests.post(
            f"https://{SHOPIFY_STORE_DOMAIN}/admin/api/2023-10/products.json",
            json={"product": product},
            headers=headers
        )
        print("Shopify Response Code:", response.status_code)
        print("Response Body:", response.text)
