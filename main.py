from flask import Flask, jsonify
from campaign_engine import run_campaign
from dashboard_app import dashboard

app = Flask(__name__)
app.register_blueprint(dashboard)

@app.route('/run')
def run():
    result = run_campaign()
    return jsonify(result)

if __name__ == "__main__":
    app.run()