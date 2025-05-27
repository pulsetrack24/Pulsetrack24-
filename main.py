from flask import Flask, jsonify
from shopify_agent import push_live_products
from product_logger import get_products

app = Flask(__name__)

@app.route("/")
def home():
    try:
        products = get_products()
        result = push_live_products(products)
        return jsonify({"status": "Live sync complete", "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)