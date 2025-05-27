import requests
from settings import AUTODS_API_KEY

def fetch_real_autods():
    headers = {
        "X-AUTH-TOKEN": AUTODS_API_KEY
    }
    url = "https://api.autods.com/v1/products"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return [{
            "title": p["title"],
            "price": float(p["price"]["selling_price"]),
            "cost": float(p["price"]["cost_price"]),
            "gtin": p.get("gtin", "SKU-AUTO")
        } for p in data.get("data", [])[:5]]
    except Exception as e:
        print("AutoDS Fetch Error:", e)
        return []