from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template_string("""
<!DOCTYPE html>
<html><head><title>Live Dashboard</title></head>
<body>
<h2>Live Product Feed</h2>
<table border="1"><tr><th>Title</th><th>GTIN</th><th>Price</th><th>Status</th><th>Source</th></tr>
<tr><td>Urbal Tea</td><td>1234567890123</td><td>$19.99</td><td>Synced</td><td>AutoDS</td></tr>
</table>
</body></html>
""")
