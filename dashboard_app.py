def create_dashboard(products):
    html = "<h1>ProfitBot v6.4 Dashboard</h1><table border='1'><tr><th>Title</th><th>Price</th></tr>"
    for p in products:
        html += f"<tr><td>{p['title']}</td><td>{p['price']}</td></tr>"
    html += "</table>"
    return html