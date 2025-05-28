import os
from openai import OpenAI
import json

# ✅ Create the OpenAI client with only supported arguments
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),  # Set in Render's environment variables
    base_url="https://openrouter.ai/api/v1"
)

def optimize_products(products):
    try:
        prompt = f"""
        You are an AI Shopify product optimizer. Pick the top 3 most profitable trending products from this list. 
        Return a JSON array of product objects with optimized titles and short ad-style descriptions.

        Products:
        {json.dumps(products)}
        """

        response = client.chat.completions.create(
            model="openrouter/openai/gpt-3.5-turbo",  # ✅ valid free model
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        result = response.choices[0].message.content
        return json.loads(result)

    except Exception as e:
        print("❌ AI Optimizer Error:", e)
        return [{"title": "Error", "description": str(e)}]
