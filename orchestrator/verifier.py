from .llm_client import call_llm

def verify_result(execution_result: dict):
    joined = "\n".join(execution_result["results"])

    prompt = f"""
Verify whether the following results correctly satisfy the task.

Results:
{joined}

Answer only YES or NO.
"""

    verdict = call_llm(prompt).upper()

    execution_result["verified"] = "YES" in verdict
    return execution_result
