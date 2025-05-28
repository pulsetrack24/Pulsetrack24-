import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def optimize_products(products):
    try:
        response = client.chat.completions.create(
            model="openrouter/autoai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an ecommerce product optimizer."},
                {"role": "user", "content": f"Optimize the following product: {products}"}
            ]
        )
        if hasattr(response, "choices") and response.choices:
            return response.choices[0].message.content
        else:
            print("⚠️ Response missing 'choices':", response)
            return {"message": "Optimization failed: no choices", "status": "error"}

    except Exception as e:
        print("🔥 Optimization Exception:", e)
        return {"message": f"Optimization failed: {str(e)}", "status": "error"}
