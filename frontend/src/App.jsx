import GraphView from "./components/GraphView";
import ExcessPermissionsTable from "./components/TableView";
import RiskReport from "./components/RiskReport";

function App() {
  return (
    <div>
      <h1>AWS IAM Analyzer Dashboard</h1>
      <GraphView />
      <hr />
      <ExcessPermissionsTable />
      <hr />
      <RiskReport />
    </div>
  );
}

export default App;
