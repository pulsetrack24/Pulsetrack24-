import os
from openai import OpenAI
import json

# Correct client initialization for OpenRouter
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def optimize_products(products):
    try:
        prompt = f"""
        You are an AI ecommerce product optimizer. Review the following product list and select the top 3 most profitable and trending ones. Return a JSON array with each product's optimized title and Shopify-style ad description.

        Example Output:
        [
            {{
                "title": "Optimized Product 1",
                "description": "Eye-catching, benefit-focused ad copy"
            }},
            ...
        ]

        Product List:
        {json.dumps(products)}
        """

        response = client.chat.completions.create(
            model="openrouter/openai/gpt-3.5-turbo",  # Use a valid OpenRouter-compatible model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        result = response.choices[0].message.content
        return json.loads(result)

    except Exception as e:
        print("🔥 AI Optimization Error:", e)
        return [{"title": "Error", "description": str(e)}]
