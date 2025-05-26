from flask import Flask, render_template_string
import json
import os

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
    <head><title>Q-STAR Dropship Dashboard</title></head>
    <body>
    <h1>Live Product Feed</h1>
    <table border="1">
        <tr><th>Title</th><th>GTIN</th><th>Price</th><th>Status</th><th>Source</th></tr>
        {% for item in data %}
        <tr>
            <td>{{ item['title'] }}</td>
            <td>{{ item['gtin'] }}</td>
            <td>{{ item['price'] }}</td>
            <td>{{ item['status'] }}</td>
            <td>{{ item['source'] }}</td>
        </tr>
        {% endfor %}
    </table>
    </body>
    </html>
    """, data=data)
