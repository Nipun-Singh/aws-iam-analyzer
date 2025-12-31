from fastapi import FastAPI

from app.api.risk_analysis_routes import router as risk_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AWS IAM Analyzer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(risk_router)

@app.get("/")
def health():
    return {"status": "running"}

