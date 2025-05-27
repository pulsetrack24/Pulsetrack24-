from tiktok_ads import generate_tiktok_ads
from klaviyo_engine import run_klaviyo_campaign
from ai_optimizer import smart_optimize
from autods_agent import fetch_real_autods
from shopify_agent import sync_to_shopify

def run_full_campaign():
    raw_products = fetch_real_autods()
    optimized = smart_optimize(raw_products)
    shopify_result = sync_to_shopify(optimized)
    tiktok_ads = generate_tiktok_ads(optimized)
    klaviyo_status = run_klaviyo_campaign(optimized)
    return {
        "shopify": shopify_result,
        "tiktok_ads": tiktok_ads,
        "klaviyo": klaviyo_status
    }