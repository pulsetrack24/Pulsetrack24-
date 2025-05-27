import requests
from settings import AUTODS_API_KEY

def fetch_autods_products():
    headers = {"X-AUTH-TOKEN": AUTODS_API_KEY}
    url = "https://api.autods.com/v1/products"
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        data = res.json().get("data", [])
        result = []
        for p in data:
            price = p.get("price", {})
            result.append({
                "title": p.get("title", "No Title"),
                "price": float(price.get("selling_price", 0)),
                "cost": float(price.get("cost_price", 0)),
                "gtin": p.get("gtin", ""),
                "image_url": p.get("image_url", "")
            })
        return result
    except Exception as e:
        print(f"[!] Failed to fetch AutoDS products: {e}")
        return []