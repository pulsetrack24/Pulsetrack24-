import os
from openai import OpenAI
import json

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def optimize_products(products):
    try:
        prompt = f"""
        You're an expert ecommerce AI. Analyze these products and return a JSON array of the top 3 products to advertise, each with an optimized title and short description for Shopify ads. Example format:
        [
            {{"title": "...", "description": "..."}},
            ...
        ]

        Products:
        {json.dumps(products)}
        """

        response = client.chat.completions.create(
            model="openrouter/openai/gpt-3.5-turbo",  # Use a valid OpenRouter model here
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        result = response.choices[0].message.content
        return json.loads(result)

    except Exception as e:
        print("🔥 Optimization Error:", e)
        return [{"title": "Optimization failed", "description": str(e)}]
