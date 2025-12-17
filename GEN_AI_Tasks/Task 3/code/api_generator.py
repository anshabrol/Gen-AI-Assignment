import google.generativeai as genai

def generate_apis(modules: list) -> list:
    model = genai.GenerativeModel("models/gemini-flash-latest")

    prompt = f"""
Generate REST API endpoints.

Modules:
{', '.join(modules)}

Rules:
- Format: METHOD /endpoint
- One API per line
"""

    response = model.generate_content(prompt)

    apis = [
        line.strip()
        for line in response.text.split("\n")
        if line.strip()
    ]

    return apis
