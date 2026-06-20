import joblib
import pandas as pd
from pathlib import Path

ROOT_DIR=Path(__file__).resolve().parents[2]

rf=joblib.load(ROOT_DIR/"models"/"random_forest.pkl")
print("Model loaded Successfully")

test_df=pd.read_csv(ROOT_DIR/"data"/"processed"/"test_df.csv")
print(test_df.shape)

X_test=test_df.drop(columns=["isFraud"])
y_test=test_df["isFraud"]
print(X_test.shape)

sample_transaction=X_test.iloc[[0]]
# Double bracket keeps it as a DF
print(sample_transaction)

import shap
explainer=shap.TreeExplainer(rf)
print("Explainer Created")

shap_values=explainer.shap_values(sample_transaction)
print("SHAP values generated")

print(type(shap_values))
print(len(shap_values))
print(shap_values.shape)

# (1,13,2)->1 sample
# 13 features
# 2 classes (Non-Fraud, Fraud)

shap_df = pd.DataFrame({
    "Feature": X_test.columns,
    "SHAP_Value": shap_values[0, :, 1]
})

shap_df = shap_df.sort_values(
    by="SHAP_Value",
    ascending=False
)

print(shap_df)
# +ve SHAP->Increase fraud probability
#  -ve SHAP->Decrease fraud probability

prediction=rf.predict(sample_transaction)[0]
probability=rf.predict_proba(sample_transaction)[0][1]
print("Prediction:", prediction)
print("Fraud Probability:", probability)

from explanation_engine import explain_transaction

reasons=explain_transaction(shap_df)

print("\nExplanation:")

for r in reasons:
    print("-", r)

import matplotlib.pyplot as plt

top5=shap_df.head(5)
plt.figure(figsize=(8,5))
plt.barh(
    top5["Feature"],
    top5["SHAP_Value"]
)
plt.title(
    "Top Fraud Contributing Features"
)
plt.tight_layout()
plt.show()

fraud_index=y_test[y_test==1].index[0]
sample_transaction=X_test.loc[[fraud_index]]
prediction=rf.predict(sample_transaction)[0]
probability=rf.predict_proba(sample_transaction)[0][1]

print("Prediction:", prediction)
print("Fraud Probability:", probability)
shap_values = explainer.shap_values(sample_transaction)

shap_df = pd.DataFrame({
    "Feature": X_test.columns,
    "SHAP_Value": shap_values[0,:,1]
})

shap_df = shap_df.sort_values(
    by="SHAP_Value",
    ascending=False
)

print(shap_df)

sample_data = X_test.sample(
    1000,
    random_state=42
)

shap_values = explainer.shap_values(
    sample_data
)

fraud_shap = shap_values[:,:,1]
shap.summary_plot(
    fraud_shap,
    sample_data
)

from risk_engine import (
    calculate_risk_score,
    get_risk_category
)

risk_score = calculate_risk_score(
    probability
)

risk_category = get_risk_category(
    risk_score
)

print("\nRisk Score:", risk_score)
print("Risk Category:", risk_category)

result = {
    "prediction": (
        "Fraud"
        if prediction == 1
        else "Non-Fraud"
    ),
    "fraud_probability": float(
        round(probability,4)
    ),
    "risk_score": risk_score,
    "risk_category": risk_category,
    "reasons": reasons
}

print(result)