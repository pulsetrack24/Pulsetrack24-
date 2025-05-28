from flask import Flask, jsonify
from campaign_engine import run_campaign

app = Flask(__name__)

@app.route("/")
def home():
    return "🟢 Bot is live"

@app.route("/run")
def run():
    try:
        result = run_campaign()
        return jsonify(result)
    except Exception as e:
        return jsonify({"message": f"Optimization failed: {str(e)}", "status": "error"})
