from openai import OpenAI
import os

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)
