import os
import openai
import json

# Configure OpenRouter
openai.api_key = os.getenv("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)
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
        content = response["choices"][0]["message"]["content"]
        return json.loads(content)  # This must return a list of dicts
    except (KeyError, json.JSONDecodeError):
        print("Invalid response or formatting error")
        return []
