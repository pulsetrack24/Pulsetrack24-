import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def optimize_products(products):
    try:
        print(f"📦 Received Products: {products}")

        # Prepare prompt
        prompt = f"You're an expert Shopify strategist. Optimize pricing, headlines, and keywords for this product list:\n\n{products}"

        # Make API call using OpenAI SDK v1.x format
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # or any free, valid OpenRouter-compatible model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # ✅ Safely extract content
        optimized_content = response.choices[0].message.content
        print("✅ Optimized Content:", optimized_content)
        return optimized_content

    except Exception as e:
        print("🔥 Optimization Error:", e)
        return str(e)
