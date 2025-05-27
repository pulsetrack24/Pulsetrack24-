import requests
from settings import KLAVIYO_API_KEY

def send_klaviyo_campaign(products):
    sent = []
    for p in products:
        email = {
            "subject": f"Check out {p['title']}",
            "body": p["description"]
        }
        sent.append(email)
    return sent