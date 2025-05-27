
from flask import Flask, jsonify
from campaign_engine import run_campaign

app = Flask(__name__)

@app.route('/')
def index():
    return "Profit Bot Live - Connected"

@app.route('/run')
def run():
    try:
        result = run_campaign()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
