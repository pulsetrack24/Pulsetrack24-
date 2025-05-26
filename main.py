from flask import Flask
from shopify_agent import sync_with_shopify
from autods_agent import fetch_and_push_products

app = Flask(__name__)

@app.route('/')
def index():
    fetch_and_push_products()
    sync_with_shopify()
    return "Live sync initiated."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
