function ProjectConfigForm({ onSubmit }) {
  const [projectName, setProjectName] = useState("");
  const [region, setRegion] = useState("us-east-1");

  const handleSubmit = () => {
    onSubmit({
      project_name: projectName,
      aws_region: region
    });
  };

  return (
    <div>
      <h2>Project Configuration</h2>
      <input
        placeholder="Project Name"
        value={projectName}
        onChange={e => setProjectName(e.target.value)}
      />
      <input
        placeholder="AWS Region"
        value={region}
        onChange={e => setRegion(e.target.value)}
      />
      <button onClick={handleSubmit}>Run IAM Scan</button>
    </div>
  );
}

export default ProjectConfigForm;
