# ai_optimizer.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ✅ Initialize OpenAI client correctly (no proxies)
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# ✅ Sample function for product optimization
def optimize_products(product_list):
    optimized = []
    for product in product_list:
        prompt = f"Improve this product title and description for higher conversions:\n\nTitle: {product['title']}\nDescription: {product['description']}"
        
        try:
            response = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct",  # ✅ Free OpenRouter-compatible model
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            content = response.choices[0].message.content.strip()
            optimized.append({
                "original": product,
                "optimized": content
            })
        except Exception as e:
            optimized.append({
                "original": product,
                "optimized": f"Error: {str(e)}"
            })

    return optimized
