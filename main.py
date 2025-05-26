from flask import Flask
from shopify_agent import sync_with_shopify
from autods_agent import fetch_and_push_products
from ai_learner import analyze_and_optimize

app = Flask(__name__)

@app.route("/")
def index():
    analyze_and_optimize()
    fetch_and_push_products()
    sync_with_shopify()
    return "Live sync + AI optimization initiated."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
