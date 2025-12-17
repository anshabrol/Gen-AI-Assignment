import google.generativeai as genai

genai.configure(api_key="Gemini_Api_key")

def generate_seo_keywords(product_name):
    """
    Generates 3–4 SEO keywords for the product
    """

    try:
        model = genai.GenerativeModel("models/gemini-flash-latest")

        prompt = f"""
Generate 4 SEO keywords for a blog about this product:
{product_name}

Rules:
- Short keywords
- High buying intent
- Comma separated
"""

        response = model.generate_content(prompt)

        keywords = response.text.strip().split(",")
        return [k.strip() for k in keywords][:4]

    except:
        # Fallback
        base = product_name.lower().split()[:3]
        return [
            "best " + " ".join(base),
            "buy " + " ".join(base),
            "top " + " ".join(base)
        ]
