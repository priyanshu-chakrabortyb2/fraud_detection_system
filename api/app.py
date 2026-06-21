from fastapi import FastAPI
from api.schemas import TransactionInput
from api.predictor import predict_transaction
from database.crud import save_prediction
from database.crud import get_predictions
from database.crud import get_predictions_by_id

app = FastAPI(title="Fraud Detection API", version="1.0")


@app.get("/")
def root():
    return {"message": "Fraud Detection API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(transaction: TransactionInput):
    try:
        result = predict_transaction(
            transaction.model_dump()
        )
        save_prediction(result)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/metrics")
def metrics():
    return{
        "model":"Random Forest",
        "precision":0.99695,
        "recall":0.99574,
        "f1_score":0.99635,
        "roc_auc":0.99906,
        "pr_auc":0.99756
    }

@app.get("/history")
def history():
    predictions = get_predictions()
    results = []
    for p in predictions:
        results.append(
            {
                "id": p.id,
                "prediction": p.prediction,
                "fraud_probability": p.fraud_probability,
                "risk_score": p.risk_score,
                "risk_category": p.risk_category
            }
        )

    return results

@app.get("/history/{prediction_id}")
def history_by_id(prediction_id: int):

    prediction = get_predictions_by_id(
        prediction_id
    )

    if prediction is None:
        return {
            "message": "Not Found"
        }

    return {
        "id": prediction.id,
        "prediction": prediction.prediction,
        "fraud_probability": prediction.fraud_probability,
        "risk_score": prediction.risk_score,
        "risk_category": prediction.risk_category,
        "reasons": prediction.reasons
    }