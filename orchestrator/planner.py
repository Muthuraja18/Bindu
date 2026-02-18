from .llm_client import call_llm

def plan_task(query: str):
    prompt = f"""
You are a professional AI planning agent.

Your task is to break the given user query into clear, logical, and well-structured execution steps.

Task:
{query}

Formatting Rules:
- Provide a neat and clean output.
- Do NOT use star symbols or special characters.
- Use simple numbering or bullet points.
- Keep steps short, clear, and actionable.
- Include a simple "Table of Contents" style structure.
- Do NOT include explanations or extra commentary.

Return only the structured execution steps.
"""

    steps_text = call_llm(prompt)

    steps = [s.strip("- ").strip() for s in steps_text.split("\n") if s.strip()]

    return {
        "query": query,
        "steps": steps
    }
