import os
import json
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def optimize_products(products):
    messages = [
        {"role": "system", "content": "You are an expert e-commerce assistant."},
        {"role": "user", "content": f"Optimize these products for online selling: {products}"}
    ]

    response = client.chat.completions.create(
        model="openrouter/autoai/gpt-3.5-turbo",  # ✅ This one is free
        messages=messages,
    )

    # Parse the string content into JSON list of dicts
    return json.loads(response.choices[0].message.content)
