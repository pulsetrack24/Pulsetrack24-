from flask import Flask, request, jsonify
from campaign_engine import run_campaign  # Make sure this file and function exist

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Pulsetrack24 API is running. Use POST /optimize to start a campaign."

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"message": "Missing required 'prompt' in request body", "status": "error"}), 400

        prompt = data["prompt"]
        result = run_campaign(prompt)  # You MUST define this in campaign_engine.py

        return jsonify({"message": "Optimization successful", "result": result, "status": "success"}), 200

    except Exception as e:
        return jsonify({"message": f"Optimization failed: {str(e)}", "status": "error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
