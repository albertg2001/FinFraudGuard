from fastapi import APIRouter
from pydantic import BaseModel
from app.fraud_detector import detect_fraud_risk

router = APIRouter()

class Transaction(BaseModel):
    text: str

@router.post(\"/detect\")
async def detect(transaction: Transaction):
    risk_level = detect_fraud_risk(transaction.text)
    return {\"risk_level\": risk_level}  # 0: normal, 1: suspicious, 2: high-risk
