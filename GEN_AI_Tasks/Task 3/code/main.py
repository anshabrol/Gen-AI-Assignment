import google.generativeai as genai
from analyzer import analyze_requirement
from module_generator import generate_modules
from schema_generator import generate_schema
from api_generator import generate_apis
from pseudocode_gen import generate_pseudocode
import os

genai.configure(api_key="Gemini API Key")

BUSINESS_REQUIREMENT = """
Build a food delivery application where users can browse restaurants,
place orders, make payments, and track delivery in real time.
"""

def save_output(requirement, modules, schema, apis, pseudocode):
    os.makedirs("../outputs", exist_ok=True)

    with open("../outputs/technical_spec.md", "w", encoding="utf-8") as f:
        f.write("# Low-Level Technical Specification\n\n")

        f.write("## Business Requirement\n")
        f.write(requirement + "\n\n")

        f.write("## System Modules\n")
        for m in modules:
            f.write(f"- {m}\n")

        f.write("\n## Database Schema\n")
        for s in schema:
            f.write(f"- {s}\n")

        f.write("\n## API Endpoints\n")
        for a in apis:
            f.write(f"- {a}\n")

        f.write("\n## Pseudocode\n")
        f.write("```\n" + pseudocode + "\n```")

    print("✅ Technical specification generated: outputs/technical_spec.md")


if __name__ == "__main__":
    req = analyze_requirement(BUSINESS_REQUIREMENT)
    modules = generate_modules(req)
    schema = generate_schema(modules)
    apis = generate_apis(modules)
    pseudocode = generate_pseudocode(req)

    save_output(req, modules, schema, apis, pseudocode)
