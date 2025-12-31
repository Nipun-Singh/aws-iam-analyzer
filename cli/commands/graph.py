import json
from app.graph.iam_graph import build_iam_graph

def export_graph():
    graph = build_iam_graph()
    with open("iam_graph.json", "w") as f:
        json.dump(graph, f, indent=2)
    '''pretty_json_string = json.dumps(graph, indent=2)
    print(pretty_json_string)'''
    print("IAM graph exported to iam_graph.json")
