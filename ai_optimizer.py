import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1")

def optimize_products(prompt):
    response = client.chat.completions.create(
        model="openrouter/openai/gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
