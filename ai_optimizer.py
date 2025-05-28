import os
import openai
import json

# Setup OpenRouter base URL and API key
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.base_url = "https://openrouter.ai/api/v1"

def optimize_products(products):
    print("📦 Received Products:", products)

    prompt = f"""
You're a powerful ecommerce optimizer. Use the following product data and return an enriched JSON list.
Each item should include:
- Clean title
- 5 bullet points (features)
- A strong marketing description
- Keywords (comma-separated)
- Tags

Input:
{json.dumps(products, indent=2)}
"""

    try:
        response = openai.ChatCompletion.create(
            model="nous-hermes2",  # Valid free OpenRouter model
            messages=[{"role": "user", "content": prompt}],
        )
        result = response.choices[0].message.content
        print("✅ AI Result:", result)
        return result
    except Exception as e:
        print("🔥 Optimization Error:", e)
        raise e
