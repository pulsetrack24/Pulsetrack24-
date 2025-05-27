def run_klaviyo_campaign(products):
    # Simulate Klaviyo logic
    sent = []
    for p in products:
        email = {
            "subject": f"Why {p['title']} is a game-changer",
            "body": f"{p['description']} - Now only ${p['price']}!"
        }
        sent.append(email)
    return sent