from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(
    title=\"FinFraudGuard - Cross-Border Fraud Detection API\",
    description=\"An NLP-driven anti-fraud detection system for cross-border transactions.\",
    version=\"1.0.0\"
)

app.include_router(api_router)

@app.get(\"/\")
async def read_root():
    return {\"message\": \"Welcome to FinFraudGuard!\"}
