from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an e-commerce product optimization expert."},
        {"role": "user", "content": "Optimize the product listing with SEO, tags, and competitive edge."}
    ],
    temperature=0.7
)
