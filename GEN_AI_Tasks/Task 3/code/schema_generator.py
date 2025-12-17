import google.generativeai as genai

def generate_schema(modules: list) -> list:
    model = genai.GenerativeModel("models/gemini-flash-latest")

    prompt = f"""
Design a simple database schema.

Modules:
{', '.join(modules)}

Rules:
- Use table format
- table_name(field1, field2, field3)
- One table per line
"""

    response = model.generate_content(prompt)

    schema = [
        line.strip()
        for line in response.text.split("\n")
        if line.strip()
    ]

    return schema
