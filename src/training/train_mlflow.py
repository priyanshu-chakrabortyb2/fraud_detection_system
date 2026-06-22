import mlflow
import mlflow.sklearn
import pandas as pd
from pathlib import Path
import joblib

import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    classification_report,
    confusion_matrix,
)

ROOT_DIR = Path(__file__).resolve().parents[2]

# =====================================
# LOAD DATA
# =====================================

train_df = pd.read_csv(
    ROOT_DIR / "data" / "processed" / "train_df.csv"
)

test_df = pd.read_csv(
    ROOT_DIR / "data" / "processed" / "test_df.csv"
)

print("Train:", train_df.shape)
print("Test:", test_df.shape)

# =====================================
# SAMPLE DATA
# =====================================

train_sample, _ = train_test_split(
    train_df,
    train_size=500000,
    stratify=train_df["isFraud"],
    random_state=42
)

X_train = train_sample.drop(
    columns=["isFraud"]
)

y_train = train_sample["isFraud"]

X_test = test_df.drop(
    columns=["isFraud"]
)

y_test = test_df["isFraud"]

# =====================================
# MLFLOW
# =====================================

mlflow.set_experiment(
    "Fraud Detection Random Forest"
)

with mlflow.start_run():

    # =====================================
    # MODEL
    # =====================================

    rf = RandomForestClassifier(
        random_state=42,
        max_depth=10,
        n_estimators=100,
        class_weight="balanced",
        n_jobs=-1
    )

    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    y_prob = rf.predict_proba(X_test)[:, 1]

    # =====================================
    # METRICS
    # =====================================

    precision = precision_score(
        y_test,
        y_pred
    )

    recall = recall_score(
        y_test,
        y_pred
    )

    f1 = f1_score(
        y_test,
        y_pred
    )

    roc_auc = roc_auc_score(
        y_test,
        y_prob
    )

    pr_auc = average_precision_score(
        y_test,
        y_prob
    )

    print(classification_report(
        y_test,
        y_pred
    ))

    print(confusion_matrix(
        y_test,
        y_pred
    ))

    # =====================================
    # LOG PARAMETERS
    # =====================================

    mlflow.log_param(
        "model",
        "RandomForest"
    )

    mlflow.log_param(
        "n_estimators",
        100
    )

    mlflow.log_param(
        "max_depth",
        10
    )

    mlflow.log_param(
        "class_weight",
        "balanced"
    )

    # =====================================
    # LOG METRICS
    # =====================================

    mlflow.log_metric(
        "precision",
        precision
    )

    mlflow.log_metric(
        "recall",
        recall
    )

    mlflow.log_metric(
        "f1_score",
        f1
    )

    mlflow.log_metric(
        "roc_auc",
        roc_auc
    )

    mlflow.log_metric(
        "pr_auc",
        pr_auc
    )

    # =====================================
    # LOG MODEL
    # =====================================

    model_info = mlflow.sklearn.log_model(
    sk_model=rf,
    artifact_path="random_forest_model")

    print(model_info.model_uri)
    from mlflow import register_model

    registered_model = register_model(
        model_uri=model_info.model_uri,
        name="FraudDetectionRF")

    print(registered_model)

    # =====================================
    # SAVE MODEL
    # =====================================

    model_path = (
        ROOT_DIR /
        "models" /
        "random_forest.pkl"
    )

    joblib.dump(
        rf,
        model_path
    )

    print("\nModel Saved")

    print(
        f"Precision: {precision:.5f}"
    )

    print(
        f"Recall: {recall:.5f}"
    )

    print(
        f"F1: {f1:.5f}"
    )

    print(
        f"ROC-AUC: {roc_auc:.5f}"
    )

    print(
        f"PR-AUC: {pr_auc:.5f}"
    )