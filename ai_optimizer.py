import os
from openai import OpenAI

# Safely load API key from environment
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
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
