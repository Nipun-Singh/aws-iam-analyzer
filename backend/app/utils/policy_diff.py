import json
import difflib

def generate_policy_diff(current_policy: dict, recommended_policy: dict):
    """
    Generates a unified diff between two IAM policy JSONs.
    """

    current_json = json.dumps(current_policy, indent=2, sort_keys=True).splitlines()
    recommended_json = json.dumps(recommended_policy, indent=2, sort_keys=True).splitlines()

    diff = difflib.unified_diff(
        current_json,
        recommended_json,
        fromfile="Current Policy",
        tofile="Recommended Policy",
        lineterm=""
    )

    return list(diff)
