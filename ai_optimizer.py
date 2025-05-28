import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")  # Make sure this matches your Render dashboard env var
)

def optimize_products(products):
    messages = [
        {"role": "system", "content": "You are an AI Shopify product optimizer."},
        {"role": "user", "content": f"Optimize these products: {products}"}
    ]

    response = client.chat.completions.create(
        model="openrouter/openai/gpt-4-turbo",
        messages=messages,
    )

    return response.choices[0].message.content
