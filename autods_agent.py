import requests
from settings import AUTODS_API_KEY

def fetch_autods_products():
    headers = {
        "X-AUTH-TOKEN": AUTODS_API_KEY
    }
    url = "https://api.autods.com/v1/products"
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        data = res.json().get("data", [])
        return [{
            "title": p["title"],
            "price": float(p["price"]["selling_price"]),
            "cost": float(p["price"]["cost_price"]),
            "gtin": p.get("gtin", "SKU")
        } for p in data[:5]]
    except Exception as e:
        return [{"error": str(e)}]