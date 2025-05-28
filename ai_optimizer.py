import os
from openai import OpenAI

# Set up OpenAI client with OpenRouter base URL and API key from environment variable
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def optimize_products(products):
    messages = [
        {
            "role": "system",
            "content": "You are an expert in e-commerce product optimization."
        },
        {
            "role": "user",
            "content": f"Optimize the following products for SEO and conversions:\n{products}"
        }
    ]

    response = client.chat.completions.create(
        model="openrouter/mistralai/mistral-7b-instruct",  # ✅ FREE model
        messages=messages,
    )

    return response.choices[0].message.content
