from flask import Flask, request, jsonify
from campaign_engine import run_campaign

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "✅ PulseTrack AI Optimizer is running."

@app.route('/optimize', methods=['POST'])
def optimize():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"message": "Missing 'prompt' in request body", "status": "error"}), 400

        result = run_campaign(prompt)
        return jsonify({"message": result, "status": "success"})

    except Exception as e:
        return jsonify({"message": f"Optimization failed: {str(e)}", "status": "error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
