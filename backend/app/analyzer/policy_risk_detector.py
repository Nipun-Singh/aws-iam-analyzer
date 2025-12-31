def analyze_policy_risks(policy: dict):
    """
    Analyzes an IAM policy JSON and returns detected risks.
    """

    findings = []

    statements = policy.get("Statement", [])
    if not isinstance(statements, list):
        statements = [statements]

    for stmt in statements:
        actions = stmt.get("Action", [])
        resources = stmt.get("Resource", [])

        if isinstance(actions, str):
            actions = [actions]
        if isinstance(resources, str):
            resources = [resources]

        # Detect wildcard actions
        for action in actions:
            if action == "*" or action.endswith(":*"):
                findings.append("Wildcard Action")

        # Detect wildcard resources
        for resource in resources:
            if resource == "*":
                findings.append("Wildcard Resource")

    return list(set(findings))

'''sample_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}

risks = analyze_policy_risks(sample_policy)
print(risks)'''