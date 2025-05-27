from autods_agent import fetch_autods_products
from ai_optimizer import optimize_products
from shopify_agent import push_to_shopify
from klaviyo_agent import send_klaviyo_campaign

def run_campaign():
    raw = fetch_autods_products()
    optimized = optimize_products(raw)
    shopify_result = push_to_shopify(optimized)
    klaviyo_result = send_klaviyo_campaign(optimized)
    return {"shopify_sync": shopify_result, "klaviyo_emails": klaviyo_result}