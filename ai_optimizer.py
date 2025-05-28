from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)
