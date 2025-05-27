
import requests

AUTO_DS_TOKEN = "d9d7854c-db93-4c39-96ce-be0b1a3be7db"

def push_to_autods(product):
    headers = {
        "Authorization": f"Bearer {d9d7854c-db93-4c39-96ce-be0b1a3be7db}",
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
