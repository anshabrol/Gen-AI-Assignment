import google.generativeai as genai

def generate_modules(requirement: str) -> list:
    model = genai.GenerativeModel("models/gemini-flash-latest")

    prompt = f"""
You are a software architect.

From the following business requirement,
list system modules.

Rules:
- Output only module names
- One module per line
- No numbering

Requirement:
{requirement}
"""

    response = model.generate_content(prompt)

    modules = [
        line.strip()
        for line in response.text.split("\n")
        if line.strip()
    ]

    return modules
