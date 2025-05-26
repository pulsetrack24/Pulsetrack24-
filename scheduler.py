import time
from autods_api import fetch_top_bio_health_products
from product_logger import log_products
from shopify_agent import push_product_to_shopify

def run_scheduler():
    while True:
        products = fetch_top_bio_health_products()
        log_products(products)
        for product in products:
            push_product_to_shopify(product)
        time.sleep(7200)

if __name__ == "__main__":
    run_scheduler()
