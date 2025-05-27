
from shopify_agent import push_live_products

sample_product = {
    "title": "Organic Bio Herbal Tea",
    "body_html": "<strong>Boost immunity with herbal wellness</strong>",
    "vendor": "ProfitBot",
    "product_type": "Tea",
    "tags": ["bio", "health", "organic", "tea"],
    "variants": [
        {
            "price": "12.99",
            "sku": "BIO-TEA-001"
        }
    ]
}

push_live_products([sample_product])
