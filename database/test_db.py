from database.crud import save_prediction
sample={
    "prediction": "Fraud",
    "fraud_probability": 0.9998,
    "risk_score": 100,
    "risk_category": "High Risk",
    "reasons": [
        "Large sender discrepancy",
        "Suspicious transaction type"
    ]
}

result=save_prediction(sample)

print(result.id)
print(result.prediction)