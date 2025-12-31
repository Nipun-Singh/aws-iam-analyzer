RISK_WEIGHTS = {
    "Wildcard Action": 50,
    "Wildcard Resource": 40,
    "Privilege Escalation Risk": 30,
    "Broad Service Permission": 25
}

def calculate_risk_score(findings: list[str]) -> dict:
    """
    Converts policy findings into a numeric risk score and severity.
    """

    score = 0
    for finding in findings:
        score += RISK_WEIGHTS.get(finding, 0)

    # Cap score at 100
    score = min(score, 100)

    # Severity classification
    if score >= 85:
        severity = "Critical"
    elif score >= 65:
        severity = "High"
    elif score >= 40:
        severity = "Moderate"
    else:
        severity = "Low"

    return {
        "score": score,
        "severity": severity
    }


'''findings = ["Wildcard Action", "Wildcard Resource"]
print(calculate_risk_score(findings))
'''