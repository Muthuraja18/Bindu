from .planner import plan_task
from .executor import execute_steps
from .verifier import verify_result
from .reporter import format_output


def run_task(query: str):
    plan = plan_task(query)
    execution = execute_steps(plan)
    verified = verify_result(execution)
    final_output = format_output(verified)

    return final_output
