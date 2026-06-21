import json

from database.db import SessionLocal
from database.models import Prediction

def save_prediction(result):
    db=SessionLocal()
    prediction=Prediction(
        prediction=result["prediction"],
        fraud_probability=result["fraud_probability"],
        risk_score=result["risk_score"],
        risk_category=result["risk_category"],
        reasons=json.dumps(result["reasons"])
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    db.close()
    return prediction

def get_predictions():
    db=SessionLocal()
    predictions=db.query(Prediction).all()
    db.close()
    return predictions


def get_predictions_by_id(prediction_id):
    db=SessionLocal()
    prediction=db.query(Prediction).filter(Prediction.id==prediction_id).first()
    db.close()
    return prediction