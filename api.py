from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Shopify Churn Prediction API")

class CustomerData(BaseModel):
    tenure_months: int
    total_orders: int
    total_spent: float
    days_since_last_order: int
    avg_order_value: float

@app.get("/")
def home():
    return {"message": "Shopify Churn API Live - Go to /docs for testing"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    # Dummy logic for demo - replace with your model.pkl later
    risk_score = 0.0
    if data.days_since_last_order > 30:
        risk_score += 0.4
    if data.tenure_months < 3:
        risk_score += 0.3
    if data.total_orders < 3:
        risk_score += 0.2
    
    risk_score = min(risk_score, 0.95)
    
    label = "LOW"
    if risk_score > 0.7:
        label = "HIGH"
    elif risk_score > 0.4:
        label = "MEDIUM"
    
    return {
        "churn_probability": round(risk_score, 2),
        "risk_label": label,
        "action": "Send 15% coupon" if label == "HIGH" else "Keep monitoring"
    }
