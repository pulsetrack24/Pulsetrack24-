import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def optimize_products(products):
    messages = [
        {"role": "system", "content": "You are an e-commerce product optimizer."},
        {"role": "user", "content": f"Optimize these products for better sales:\n{products}"}
    ]

    try:
        response = client.chat.completions.create(
            model="openrouter/openai/gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Optimization failed: {str(e)}"
