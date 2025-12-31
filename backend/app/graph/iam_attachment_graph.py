def build_iam_attachment_graph(policies: list[dict]):
    """
    Builds IAM graph (users/roles/groups -> policies)
    """

    nodes = []
    edges = []

    node_ids = set()

    def add_node(node_id, label, node_type):
        if node_id not in node_ids:
            nodes.append({
                "id": node_id,
                "label": label,
                "type": node_type
            })
            node_ids.add(node_id)

    for policy in policies:
        policy_id = f"policy:{policy['policy_name']}"
        add_node(policy_id, policy["policy_name"], "policy")

        attachments = policy.get("attachments", {})

        # Users
        for user in attachments.get("users", []):
            user_id = f"user:{user}"
            add_node(user_id, user, "user")
            edges.append({
                "from": user_id,
                "to": policy_id
            })

        # Roles
        for role in attachments.get("roles", []):
            role_id = f"role:{role}"
            add_node(role_id, role, "role")
            edges.append({
                "from": role_id,
                "to": policy_id
            })

        # Groups
        for group in attachments.get("groups", []):
            group_id = f"group:{group}"
            add_node(group_id, group, "group")
            edges.append({
                "from": group_id,
                "to": policy_id
            })

    return {
        "nodes": nodes,
        "edges": edges
    }
