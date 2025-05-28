from openai import OpenAI

client = OpenAI()

def optimize_products(products: list) -> str:
    prompt = f"""
    Optimize the following list of product titles for better performance in digital marketing campaigns.
    Ensure they are clear, engaging, and keyword-rich. Keep the format as a list.

    Products:
    {products}
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
