import sys
import os

# Add project root directory to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from orchestrator.orchestrator import run_task

query = "Analyze monthly sales data and generate insights"

result = run_task(query)

print("\n--- MULTI AGENT SYSTEM OUTPUT ---\n")
print(result)
