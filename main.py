from flask import Flask, jsonify
from campaign_engine import run_campaign

app = Flask(__name__)

@app.route("/")
def index():
    return "ProfitBot v9.6 Smart Wellness AI – LIVE"

@app.route("/run")
def run():
    result = run_campaign()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
