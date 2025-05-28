from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is working 🚀"}

@app.get("/status")
async def status():
    return {"status": "Service live ✅"}
