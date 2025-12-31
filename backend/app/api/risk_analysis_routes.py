from fastapi import APIRouter
from app.analyzer.policy_risk_detector import analyze_policy_risks
from app.analyzer.risk_scoring import calculate_risk_score
from app.analyzer.account_risk_index import calculate_account_risk_index
from app.recommender.recommendation_generator import generate_least_privilege_policy
from app.utils.policy_diff import generate_policy_diff
from app.graph.iam_attachment_graph import build_iam_attachment_graph
from app.aws.session import get_aws_session
from app.aws.iam_fetcher import fetch_iam_policies
from app.models import ProjectConfig

router = APIRouter()

@router.post("/analysis/full-risk-report")
def full_risk_report(config: ProjectConfig):
    # Mock policies (later replaced with real IAM data)
    '''policies = [
    {
        "name": "PowerUser-Deprecated",
        "policy": {
            "Statement": [{
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }]
        },
        "used_actions": ["s3:GetObject"],
        "attachments": {
            "users": ["alice"],
            "roles": ["ci-runner"],
            "groups": []
        }
    },
    {
        "name": "S3-ReadWrite-AllBuckets",
        "policy": {
            "Statement": [{
                "Effect": "Allow",
                "Action": ["s3:GetObject", "s3:PutObject"],
                "Resource": "*"
            }]
        },
        "used_actions": ["s3:GetObject"],
        "attachments": {
            "users": [],
            "roles": [],
            "groups": ["devs"]
        }
    }
]'''
    session = get_aws_session()

    policies = fetch_iam_policies(session)

    report = []
    policy_scores = []

    for p in policies:
        findings = analyze_policy_risks(p["policy"])
        risk = calculate_risk_score(findings)
        recommendation = generate_least_privilege_policy(used_actions=["sts:GetCallerIdentity"]  # placeholder
)

        policy_scores.append(risk["score"])
        
        diff = generate_policy_diff(p["policy"], recommendation)

        report.append({
            "policy_name": p["name"],
            "findings": findings,
            "risk_score": risk["score"],
            "severity": risk["severity"],
            "attachments": p["attachments"],
            "current_policy": p["policy"],
            "recommended_policy": recommendation,
            "policy_diff": diff
        })


    account_risk = calculate_account_risk_index(policy_scores)
    graph = build_iam_attachment_graph(report)

    return {
        "project": config.project_name,
        "region": config.aws_region,
        "account_risk": account_risk,
        "policies": report,
        "iam_graph": graph
    }

