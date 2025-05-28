import os
import openai
import json

# Setup OpenRouter API credentials
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def optimize_products(products):
    prompt = f"Optimize this list of products for ecommerce performance: {products}"
    response = openai.ChatCompletion.create(
        model="openrouter/mistralai/mixtral-8x7b",
        messages=[
            {"role": "system", "content": "You are a product optimization assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
