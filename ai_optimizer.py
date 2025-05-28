import requests

def optimize_products(products):
    try:
        input_text = f"Optimize these products for profitability: {products}"
        headers = {
            "Authorization": "Bearer YOUR_OPENROUTER_API_KEY",  # Replace with your OpenRouter key
            "HTTP-Referer": "https://yourdomain.com",  # Or your Replit project
            "X-Title": "ProfitBot"
        }

        payload = {
            "model": "openrouter/cinematika-7b",  # Free OpenRouter model
            "messages": [
                {"role": "system", "content": "You are a profit optimization assistant."},
                {"role": "user", "content": input_text}
            ]
        }

        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        result = res.json()

        return result["choices"][0]["message"]["content"]
    except Exception as e:
        raise Exception(f"Optimization failed: {str(e)}")
