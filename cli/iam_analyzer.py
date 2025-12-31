import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

import argparse
from commands.scan import scan_permissions
from commands.graph import export_graph
from commands.recommend import recommend_policy

parser = argparse.ArgumentParser(description="AWS IAM Analyzer CLI")

parser.add_argument(
    "command",
    choices=["scan", "graph", "recommend"],
    help="Command to execute"
)

args = parser.parse_args()

if args.command == "scan":
    scan_permissions()

elif args.command == "graph":
    export_graph()

elif args.command == "recommend":
    recommend_policy()
