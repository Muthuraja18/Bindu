from .llm_client import call_llm

def execute_steps(plan: dict):
    outputs = []

    for step in plan["steps"]:
        prompt = f"""
Execute the following step and return a concise result.

Step: {step}
"""
        result = call_llm(prompt)
        outputs.append(f"{step}: {result}")

    return {
        "query": plan["query"],
        "results": outputs
    }
