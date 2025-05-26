import json
import random

sample_data = [
    {"title": "BioHealth Probiotic", "gtin": "1234567890123", "price": "$19.99", "status": "Top Seller", "source": "AutoDS"},
    {"title": "Organic Immunity Boost", "gtin": "2345678901234", "price": "$24.99", "status": "Top Seller", "source": "Shopify"},
]

with open("product_log.json", "w") as f:
    json.dump(sample_data, f)