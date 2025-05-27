def generate_tiktok_ads(products):
    ads = []
    for p in products:
        ad_script = f"Check out {p['title']} — {p['description'][:50]}... #health #bio #smartgear"
        ads.append({
            "product": p["title"],
            "script": ad_script,
            "hashtags": ["#health", "#bio", "#smartgear"]
        })
    return ads