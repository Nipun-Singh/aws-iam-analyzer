def fetch_iam_policies(session):
    iam = session.client("iam")

    policies = []
    paginator = iam.get_paginator("list_policies")

    for page in paginator.paginate(Scope="Local"):
        for policy in page["Policies"]:
            policy_arn = policy["Arn"]

            version = iam.get_policy_version(
                PolicyArn=policy_arn,
                VersionId=policy["DefaultVersionId"]
            )

            attachments = iam.list_entities_for_policy(
                PolicyArn=policy_arn
            )

            policies.append({
                "name": policy["PolicyName"],
                "policy": version["PolicyVersion"]["Document"],
                "attachments": {
                    "users": [u["UserName"] for u in attachments["PolicyUsers"]],
                    "roles": [r["RoleName"] for r in attachments["PolicyRoles"]],
                    "groups": [g["GroupName"] for g in attachments["PolicyGroups"]]
                }
            })

    return policies
