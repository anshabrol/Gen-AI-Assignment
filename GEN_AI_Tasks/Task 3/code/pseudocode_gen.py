import google.generativeai as genai

def generate_pseudocode(requirement: str) -> str:
    model = genai.GenerativeModel("models/gemini-flash-latest")

    prompt = f"""
Write high-level pseudocode for this system.

Requirement:
{requirement}

Rules:
- Use IF, ELSE, LOOP
- Plain text
"""

    response = model.generate_content(prompt)
    return response.text.strip()
