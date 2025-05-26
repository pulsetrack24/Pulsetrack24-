# Placeholder for AutoDS API interaction logic
def get_autods_products():
    return [
        {"title": f"Health Ring {i} Pro", "gtin": f"TEST000{i}", "price": 19.99 + i*3}
        for i in range(1, 6)
    ]
