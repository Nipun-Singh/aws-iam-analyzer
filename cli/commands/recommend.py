import json
from app.recommender.least_privilege import generate_policy

def recommend_policy():
    # Mock used permissions (later from CloudTrail)
    used_actions = [
        "s3:GetObject",
        "s3:ListBucket"
    ]

    policy = generate_policy(used_actions)

    print("Least-Privilege Policy Recommendation:\n")
    print(json.dumps(policy, indent=2))
