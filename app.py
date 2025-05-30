from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html", status="Live", synced_products=5, error_logs=[])

if __name__ == "__main__":
    app.run(debug=True)
