import google.generativeai as genai

genai.configure(api_key="Gemini_Api_key")

def generate_blog(product, keywords):
    """
    Generates SEO blog content
    """

    model = genai.GenerativeModel("models/gemini-flash-latest")

    prompt = f"""
Write a 150-200 word SEO blog post.

Product Name: {product['name']}
Category: {product['category']}
Keywords: {", ".join(keywords)}

Rules:
- Natural tone
- No keyword stuffing
- Promotional but informative
"""

    response = model.generate_content(prompt)

    return response.text.strip()
