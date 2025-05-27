import requests
from settings import KLAVIYO_API_KEY

def send_klaviyo_campaign(products):
    return [{"subject": f"New: {p['title']}", "body": p['description']} for p in products]