
import requests

AUTO_DS_TOKEN = "your-autods-api-key"

def push_to_autods(product):
    headers = {
        "Authorization": f"Bearer {AUTO_DS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "title": product["title"],
        "description": product["description"],
        "tags": product.get("tags", []),
        "price": product["price"]
    }
    url = "https://api.autods.com/v1/products"
    response = requests.post(url, json=data, headers=headers)
    print("AutoDS response:", response.status_code, response.text)
