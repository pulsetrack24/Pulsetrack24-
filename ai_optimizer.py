import os
import json
import openai

# Correct OpenRouter base and key
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.base_url = "https://openrouter.ai/api/v1"

def optimize_products(products):
    print("📦 Received Products:", products)

    prompt = f"""
You're an eCommerce AI assistant. For each product below, return:
- Clean product title
- 5 bullet points
- A sales description
- Keyword list
- Tags

Products:
{json.dumps(products, indent=2)}
"""

    try:
        response = openai.chat.completions.create(
            model="nous-hermes2",  # Free & valid OpenRouter model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content
        print("✅ Response:", content)
        return json.loads(content)
    except Exception as e:
        print("🔥 Optimization Error:", e)
        raise
