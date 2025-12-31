def generate_least_privilege_policy(used_actions: list[str], resources: list[str] | None = None):
    """
    Generates a least-privilege IAM policy from used actions.
    """

    if not resources:
        resources = ["*"]

    return {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": sorted(set(used_actions)),
                "Resource": resources
            }
        ]
    }

'''used = ["s3:GetObject", "logs:PutLogEvents"]
policy = generate_least_privilege_policy(used)
print(policy)'''
