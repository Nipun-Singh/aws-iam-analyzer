import { useEffect, useState } from "react";
import { fetchFullRiskReport } from "../services/api";
import IamGraph from "./IamGraph";

function RiskReport() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchFullRiskReport()
      .then(setData)
      .catch(err => setError(err.message));
  }, []);

  if (error) return <p>Error: {error}</p>;
  if (!data) return <p>Loading risk report...</p>;

  return (
    <div>
      <h2>Account Risk Index</h2>
      <p>
        Score: <b>{data.account_risk.account_risk_index}</b> |
        Severity: <b>{data.account_risk.severity}</b>
      </p>

      <br />
      <IamGraph graph={data.iam_graph} />

      <hr />

      <h2>Risky Policies</h2>

      {/*data.policies.map((policy, idx) => (
        <div key={idx} style={{ marginBottom: "20px" }}>
          <h3>{policy.policy_name}</h3>
          <p>
            Risk Score: <b>{policy.risk_score}</b> |
            Severity: <b>{policy.severity}</b>
          </p>

          <p>Findings:</p>
          <ul>
            {policy.findings.map((f, i) => (
              <li key={i}>{f}</li>
            ))}
          </ul>
        </div>
      ))*/}
      {data.policies.map((policy, idx) => (
  <div key={idx} style={{ marginBottom: "30px", borderBottom: "1px solid #ccc" }}>
    <h3>{policy.policy_name}</h3>
    <p>
      <b>Attached to:</b>
      <br />
      Users: {policy.attachments.users.length > 0
        ? policy.attachments.users.join(", ")
        : "None"}
      <br />
      Roles: {policy.attachments.roles.length > 0
        ? policy.attachments.roles.join(", ")
        : "None"}
      <br />
      Groups: {policy.attachments.groups.length > 0
        ? policy.attachments.groups.join(", ")
       : "None"}
    </p>

    <p>
      Risk Score: <b>{policy.risk_score}</b> |
      Severity: <b>{policy.severity}</b>
    </p>

    <p>Findings:</p>
    <ul>
      {policy.findings.map((f, i) => (
        <li key={i}>{f}</li>
      ))}
    </ul>

    <details>
      <summary>View Policy JSON Diff</summary>

      <pre style={{ background: "#111", color: "#ddd", padding: "10px", overflowX: "auto" }}>
        {policy.policy_diff.map((line, i) => {
          let color = "#ddd";
          if (line.startsWith("+") && !line.startsWith("+++")) color = "#4CAF50";
          if (line.startsWith("-") && !line.startsWith("---")) color = "#F44336";

          return (
            <div key={i} style={{ color }}>
              {line}
            </div>
          );
        })}
      </pre>
    </details>
  </div>
))}

      
    </div>

    
  );
}

export default RiskReport;
