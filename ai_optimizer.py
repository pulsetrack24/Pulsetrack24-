import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def optimize_products(products):
    messages = [
        {
            "role": "system",
            "content": "You are an expert product optimizer."
        },
        {
            "role": "user",
            "content": f"Optimize these products for Shopify and AutoDS: {products}"
        }
    ]

    response = client.chat.completions.create(
        model="openchat/openchat-3.5",  # ✅ Free & working model
        messages=messages,
    )

    return response.choices[0].message.content
