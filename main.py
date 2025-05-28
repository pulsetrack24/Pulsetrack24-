from flask import Flask, request, jsonify
from campaign_engine import run_campaign

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize():
    try:
        data = request.get_json()
        prompt = data.get("prompt")
        if not prompt:
            return jsonify({"message": "Missing 'prompt' in request", "status": "error"}), 400

        result = run_campaign(prompt)
        return jsonify({"message": result, "status": "success"})

    except Exception as e:
        return jsonify({"message": f"Optimization failed: {str(e)}", "status": "error"}), 500
