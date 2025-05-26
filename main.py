from flask import Flask
from shopify_agent import push_live_products
from ai_learner import analyze_and_optimize
from ai_writer import generate_description

app = Flask(__name__)

@app.route("/")
def run_bot():
    analyze_and_optimize()
    push_live_products()
    return "Profit Bot v6: Live sync, learning, and publishing."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
