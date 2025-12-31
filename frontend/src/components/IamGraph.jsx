function IamGraph({ graph }) {
  if (!graph) return null;

  const nodesByType = graph.nodes.reduce((acc, node) => {
    acc[node.type] = acc[node.type] || [];
    acc[node.type].push(node);
    return acc;
  }, {});

  return (
    <div>
      <h2>IAM Attachment Graph</h2>

      <h3>Nodes</h3>
      {Object.entries(nodesByType).map(([type, nodes]) => (
        <div key={type}>
          <b>{type.toUpperCase()}</b>
          <ul>
            {nodes.map(n => (
              <li key={n.id}>{n.label}</li>
            ))}
          </ul>
        </div>
      ))}

      <h3>Relationships</h3>
      <ul>
        {graph.edges.map((edge, idx) => (
          <li key={idx}>
            {edge.from} → {edge.to}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default IamGraph;
