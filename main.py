from flask import Flask, jsonify
from campaign_engine import run_full_campaign

app = Flask(__name__)

@app.route("/")
def index():
    return "Profit Bot v7 AI Campaign Engine"

@app.route("/campaign")
def campaign():
    report = run_full_campaign()
    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=False)