
import openai
import os
import ast

# Configure OpenRouter endpoint
api_key = os.getenv("OPENROUTER_API_KEY", "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")
openai.api_key = api_key
openai.api_base = "https://openrouter.ai/api/v1"

def optimize_products(products):
    prompt = f"Optimize this list of products for sales:\n\n{products}\n\nReturn a clean Python list of dictionaries with 'title' keys only."

    response = openai.ChatCompletion.create(
        model="openrouter/mistralai/mixtral-8x7b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response['choices'][0]['message']['content']

    try:
        return ast.literal_eval(content)
    except Exception as e:
        print("Parsing failed:", e)
        return []
