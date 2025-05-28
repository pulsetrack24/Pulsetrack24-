import os
import openai
import json

# Setup OpenRouter API credentials
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def optimize_products(products):
    prompt = f"Optimize this list of products for a Shopify dropshipping store:\n\n{products}"

    response = openai.ChatCompletion.create(
        model="openrouter/mistralai/mixtral-8x7b",
        messages=[
            {"role": "system", "content": "You are an e-commerce optimization expert."},
            {"role": "user", "content": prompt}
        ]
    )

    try:
        return json.loads(response["choices"][0]["message"]["content"])
    except (KeyError, json.JSONDecodeError):
        print("Invalid response or JSON formatting error.")
        return []
