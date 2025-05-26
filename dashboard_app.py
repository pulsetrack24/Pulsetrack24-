from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)
LOG_FILE = "product_log.json"

@app.route("/dashboard")
def dashboard():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            data = json.load(f)
    else:
        data = []
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head><title>QSTAR AI Dashboard</title></head>
    <body>
    <h1>Live Product Intelligence</h1>
    <table border="1">
        <tr><th>Title</th><th>GTIN</th><th>Price</th><th>Status</th><th>Source</th></tr>
        {% for p in data %}
        <tr>
            <td>{{ p['title'] }}</td>
            <td>{{ p['gtin'] }}</td>
            <td>{{ p['price'] }}</td>
            <td>{{ p['status'] }}</td>
            <td>{{ p['source'] }}</td>
        </tr>
        {% endfor %}
    </table>
    </body>
    </html>
    """, data=data)
