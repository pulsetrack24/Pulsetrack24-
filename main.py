from flask import Flask, jsonify
from campaign_engine import run_campaign

app = Flask(__name__)

@app.route("/")
def index():
    return "Profit Bot V6 is live."

@app.route("/run")
def run():
    result = run_campaign()
    return jsonify(result)