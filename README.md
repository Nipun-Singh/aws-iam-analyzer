# AWS IAM Analyzer & Policy Recommendation Tool

## Overview
The AWS IAM Analyzer is a full-stack security analysis tool that evaluates AWS IAM policies for over-privileged access, assigns risk scores, generates least-privilege recommendations, and visualizes IAM relationships.

The tool supports **real AWS IAM accounts**, accepts user-provided project configuration, and produces an account-level security posture report through a web dashboard.

---

## Key Features

- Static IAM policy risk analysis
- Detection of risky permissions:
  - Wildcard actions (`*`, `service:*`)
  - Wildcard resources (`Resource: "*"`)
- Policy risk scoring with severity levels:
  - Low, Moderate, High, Critical
- Account Risk Index aggregation
- Least-privilege policy recommendation
- Policy JSON diff (current vs recommended)
- Role / User / Group attachment visibility
- IAM relationship graph (attachments-based)
- Real AWS IAM integration via boto3
- React dashboard for visualization

---

## Tech Stack

### Backend
- Python
- FastAPI
- boto3 (AWS SDK)
- Pydantic

### Frontend
- React
- Vite

### Cloud
- AWS IAM (Read-only access)

---

## Architecture Summary

- The backend fetches IAM policies and attachments from AWS
- Policies are analyzed for risky patterns
- Risk scores are calculated and aggregated
- Least-privilege recommendations are generated
- IAM relationships are converted into a graph structure
- A single API endpoint exposes the full report
- The frontend triggers scans and visualizes results

---

## Project Structure

aws-iam-analyzer/
├── backend/
│ └── app/
│ ├── aws/
│ ├── analyzer/
│ ├── recommender/
│ ├── graph/
│ ├── utils/
│ ├── api/
│ └── main.py
│
├── frontend/
│ └── src/
│ ├── components/
│ ├── App.jsx
│ └── main.jsx
│
├── cli/ # optional
├── .env # user-provided (not committed)
└── README.md


---

## Setup Instructions

### 1. Backend Setup

Create virtual environment and install dependencies:

```bash
cd backend
pip install -r requirements.txt


#Create .env file (do NOT commit):

'''AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_SESSION_TOKEN=optional
AWS_REGION=us-east-1'''

#Run backend:

uvicorn app.main:app --reload

### 2. Frontend Setup

```In Powershell:
cd frontend
npm install
npm run dev

```Open browser:
http://localhost:5173


