from flask import Flask, render_template_string
import json, os

app = Flask(__name__)
LOG_FILE = "product_log.json"

@app.route("/")
def dashboard():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            data = json.load(f)
    else:
        data = []

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head><title>PulseTrack AI</title></head>
    <body>
        <h1>God Mode Dashboard</h1>
        <table border=1>
            <tr><th>Title</th><th>GTIN</th><th>Price</th></tr>
            {% for product in data %}
                <tr><td>{{ product['title'] }}</td><td>{{ product['gtin'] }}</td><td>{{ product['price'] }}</td></tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """, data=data)
