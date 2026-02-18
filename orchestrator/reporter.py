from .llm_client import call_llm

def format_output(result: dict):
    joined = "\n".join(result["results"])

    prompt = f"""
Generate a clean, professional final report based on the execution results.

Results:
{joined}
"""

    report = call_llm(prompt)

    return f"""
AI Multi-Agent Execution Report
--------------------------------
Query  : {result['query']}
Status : {'SUCCESS' if result['verified'] else 'NEEDS REVIEW'}

{report}
""".strip()
