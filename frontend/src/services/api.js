{/*export async function fetchIamGraph() {
  const res = await fetch("http://127.0.0.1:8000/graph/iam");
  if (!res.ok) {
    throw new Error("uyi amma");
  }
  return res.json();
}

export async function fetchExcessPermissions() {
  const res = await fetch(
    "http://127.0.0.1:8000/analysis/excess-permissions"
  );

  if (!res.ok) {
    throw new Error("Failed to fetch excess permissions");
  }

  return res.json();
}

export async function fetchFullRiskReport() {
  const res = await fetch(
    "http://127.0.0.1:8000/analysis/full-risk-report"
  );

  if (!res.ok) {
    throw new Error("Failed to fetch risk report");
  }

  return res.json();
}*/}

const runScan = async (config) => {
  const res = await fetch(
    "http://127.0.0.1:8000/analysis/full-risk-report",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(config)
    }
  );
  setData(await res.json());
};
