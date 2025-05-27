import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def optimize_products(products):
    optimized = []
    for p in products:
        if not p.get("price") or not p.get("cost"):
            continue
        if (p["price"] - p["cost"]) / p["cost"] < 0.5:
            continue
        prompt = f"Generate optimized Shopify tags, title, and description for: {p['title']}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response["choices"][0]["message"]["content"]
        p["description"] = content
        p["tags"] = ["Smart Health", "Fitness", "Wellness", "Tech"]
        optimized.append(p)
    return optimized