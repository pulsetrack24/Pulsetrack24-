from flask import Flask, render_template, jsonify
from dashboard_app import create_dashboard
from settings import SHOP_DOMAIN, SHOPIFY_TOKEN
from shopify_agent import sync_shopify_products
from autods_agent import sync_autods_products
from ai_writer import generate_product_data
from ai_learner import learn_and_adapt

app = Flask(__name__)

@app.route('/')
def index():
    try:
        product_data = generate_product_data()
        sync_shopify_products(product_data)
        sync_autods_products(product_data)
        learn_and_adapt(product_data)
        return create_dashboard(product_data)
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)