from pydantic import BaseModel

class ProjectConfig(BaseModel):
    project_name: str
    aws_region: str = "us-east-1"
