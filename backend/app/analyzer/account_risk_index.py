def calculate_account_risk_index(policy_scores: list[int]) -> dict:
    """
    Aggregates individual policy scores into an account-level risk index.
    """

    if not policy_scores:
        return {
            "account_risk_index": 0,
            "severity": "Low"
        }

    avg_score = sum(policy_scores) // len(policy_scores)

    if avg_score >= 85:
        severity = "Critical"
    elif avg_score >= 65:
        severity = "High"
    elif avg_score >= 40:
        severity = "Moderate"
    else:
        severity = "Low"

    return {
        "account_risk_index": avg_score,
        "severity": severity
    }

policy_scores = [92, 78, 65]
print(calculate_account_risk_index(policy_scores))
