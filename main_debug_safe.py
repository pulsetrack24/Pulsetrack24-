from flask import Flask
from shopify_agent import push_live_products
from ai_learner import analyze_and_optimize

app = Flask(__name__)

@app.route("/")
def run_bot():
    try:
        analyze_and_optimize()
        push_live_products()
        return "✅ Profit Bot v6: Live sync complete."
    except Exception as e:
        return f"❌ Error during sync: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
