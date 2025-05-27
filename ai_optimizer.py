import requests

def optimize_products(raw_products):
    headers = {
        "Authorization": f"Bearer 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",  # replace with your key
        "Content-Type": "application/json"
    }

    prompt = f"Optimize these products for ecommerce:\n{raw_products}"

    data = {
        "model": "mistralai/mixtral-8x7b",  # or try 'meta-llama/llama-3-70b-instruct'
        "messages": [
            {"role": "system", "content": "You are a Shopify product optimizer."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    result = response.json()
    return result['choices'][0]['message']['content']
