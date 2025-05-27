from flask import Blueprint

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def home():
    return "<h1>Profit Bot v9.5 Dashboard</h1><p>Status: Live</p>"