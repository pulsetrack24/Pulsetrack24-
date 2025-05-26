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
    <head><title>Live Product Feed</title></head>
    <body>
        <h2>Live Product Feed</h2>
        <table border="1">
            <tr><th>Title</th><th>GTIN</th><th>Price</th><th>Status</th><th>Source</th></tr>
            {% for product in data %}
            <tr>
                <td>{{ product.title }}</td>
                <td>{{ product.gtin }}</td>
                <td>{{ product.price }}</td>
                <td>{{ product.status }}</td>
                <td>{{ product.source }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """, data=data)