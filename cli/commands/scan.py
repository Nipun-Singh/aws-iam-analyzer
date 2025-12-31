from app.analyzer.excess_permissions import find_excess_permissions

def scan_permissions():
    allowed = [
        "s3:GetObject",
        "s3:PutObject",
        "ec2:StartInstances"
    ]
    used = ["s3:GetObject"]

    excess = find_excess_permissions(allowed, used)

    print("Unused / Excess Permissions:")
    for perm in excess:
        print(f"- {perm}")
