
import openai
import os

# Configure OpenRouter endpoint
openai.api_key = os.getenv("OPENROUTER_API_KEY", "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")
openai.api_base = "https://openrouter.ai/api/v1"

def optimize_products(products):
    try:
        prompt = f"Optimize this list of products for best e-commerce performance: {products}"
        response = openai.ChatCompletion.create(
            model="openrouter/mistralai/mixtral-8x7b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        if 'choices' in response and response['choices']:
            return response['choices'][0]['message']['content']
        else:
            return "Error: Model response was empty or malformed."
    except Exception as e:
        return f"AI Optimization failed: {str(e)}"
