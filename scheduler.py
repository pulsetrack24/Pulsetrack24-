import time
from autods_api import get_autods_products
from product_logger import log_products
from shopify_agent import push_to_shopify

def run_scheduler():
    while True:
        products = get_autods_products()
        log_products(products)
        for product in products:
            push_to_shopify(product)
        time.sleep(3600)
