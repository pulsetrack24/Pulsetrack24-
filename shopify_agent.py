
import requests

SHOP_URL = "https://yourshop.myshopify.com"
ACCESS_TOKEN = "your_shopify_access_token"

def push_live_products(products):
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }

    for product in products:
        product_data = {
            "product": {
                "title": product.get("title", "Untitled Product"),
                "body_html": product.get("description", ""),
                "vendor": "AutoDS",
                "product_type": "Bio Health",
                "variants": [
                    {
                        "price": product.get("price", "0.00"),
                        "sku": product.get("gtin", "N/A")
                    }
                ]
            }
        }

        response = requests.post(f"{SHOP_URL}/admin/api/2023-10/products.json", 
                                 json=product_data, headers=headers)

        if response.status_code == 201:
            print("Product uploaded successfully.")
        else:
            print(f"Failed to upload product: {response.text}")
