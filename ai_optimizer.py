import os
from openai import OpenAI

# Safely load API key from environment
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("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")
)

def optimize_products(products):
    messages = [
        {"role": "system", "content": "You are an expert Shopify product optimizer. Write SEO-friendly tags, titles, and descriptions."},
        {"role": "user", "content": f"Optimize these products for smart health niche:\n{products}"}
    ]
    
    response = client.chat.completions.create(
        model="openrouter/openai/gpt-4-turbo",
        messages=messages,
    )

    return response.choices[0].message.content
