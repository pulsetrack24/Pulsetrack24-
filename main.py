from fastapi import FastAPI
from shopify_connector import get_products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PulseTrack24 is alive"}

@app.get("/products")
def products():
    return {"products": get_products()}
