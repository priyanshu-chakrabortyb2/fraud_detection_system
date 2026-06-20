import joblib
import sys
from pathlib import Path
import shap

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

MODEL_PATH = ROOT_DIR / "models" / "random_forest.pkl"
model = joblib.load(MODEL_PATH)
print("Random Forest Loaded")
explainer=shap.TreeExplainer(model)
print("SHAP Explainer Loaded")

import pandas as pd
from src.explainability.risk_engine import calculate_risk_score, get_risk_category
from src.explainability.explanation_engine import explain_transaction



def predict_transaction(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    shap_values = explainer.shap_values(df)
    fraud_shap = shap_values[:, :, 1]
    shap_df = pd.DataFrame(
        {
            "Feature": df.columns,
            "SHAP_Value": fraud_shap[0]
        }
    )
    reasons = explain_transaction(
        shap_df
    )
    risk_score = calculate_risk_score(probability)
    risk_category = get_risk_category(risk_score)
    return {
        "prediction": ("Fraud" if prediction == 1 else "Non-Fraud"),
        "fraud_probability": float(round(probability, 4)),
        "risk_score": risk_score,
        "risk_category": risk_category,
        "reasons":reasons
    }


sample = {
    "step": 300,
    "type": 4,
    "amount": 890577.21,
    "oldbalanceOrg": 890577.21,
    "newbalanceOrig": 0,
    "oldbalanceDest": 0,
    "newbalanceDest": 890577.21,
    "balance_diff_orig": 890577.21,
    "balance_diff_dest": -890577.21,
    "amount_to_balance_ratio": 1.0,
    "is_zero_balance_org": 0,
    "is_zero_balance_dest": 1,
    "hour_of_day": 12,
}

result = predict_transaction(sample)
print(result)




