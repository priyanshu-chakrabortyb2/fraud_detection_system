import pandas as pd
from pathlib import Path
from sklearn.metrics import roc_auc_score,average_precision_score

ROOT_DIR = Path(__file__).resolve().parents[2]
train_df = pd.read_csv(ROOT_DIR / "data" / "processed" / "train_df.csv")
test_df = pd.read_csv(ROOT_DIR / "data" / "processed" / "test_df.csv")

print(train_df.shape)
print(test_df.shape)


from sklearn.model_selection import train_test_split

train_sample, _ = train_test_split(
    train_df, train_size=500000, stratify=train_df["isFraud"], random_state=42
)

X_train = train_sample.drop(columns=["isFraud"])
y_train = train_sample["isFraud"]
X_test = test_df.drop(columns=["isFraud"])
y_test = test_df["isFraud"]

print(X_train.columns.tolist())

print("Train Fraud %")
print(y_train.mean() * 100)

print("Test Fraud %")
print(y_test.mean() * 100)

fraud = y_train.sum()
non_fraud = len(y_train) - fraud
scale_pos_weight = non_fraud / fraud
print("Fraud:", fraud)
print("Non Fraud:", non_fraud)
print("Scale Pos Weight:", scale_pos_weight)

# //Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

lr=LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)
y_prob_lr=lr.predict_proba(X_test)[:,1]

# Classification Report
print(classification_report(y_test, y_pred_lr))

# confusion matrix
cm = confusion_matrix(y_test, y_pred_lr)
print(cm)


precision = precision_score(y_test, y_pred_lr)
recall = recall_score(y_test, y_pred_lr)
f1 = f1_score(y_test, y_pred_lr)
roc_auc_lr = roc_auc_score(
    y_test,
    y_prob_lr
)

pr_auc_lr = average_precision_score(
    y_test,
    y_prob_lr
)

print("ROC-AUC:", roc_auc_lr)
print("PR-AUC:", pr_auc_lr)

print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)

print("----------------DECISION TREE----------------------")
# Decision Tree
from sklearn.tree import DecisionTreeClassifier

dt=DecisionTreeClassifier(random_state=42,max_depth=10,class_weight="balanced")
dt.fit(X_train,y_train)

y_prob_dt = dt.predict_proba(X_test)[:,1]
y_pred_dt=dt.predict(X_test)

print(classification_report(y_test,y_pred_dt))
print(confusion_matrix(y_test,y_pred_dt))
precision = precision_score(y_test, y_pred_dt)
recall = recall_score(y_test, y_pred_dt)
f1 = f1_score(y_test, y_pred_dt)

roc_auc_dt = roc_auc_score(
    y_test,
    y_prob_dt
)

pr_auc_dt = average_precision_score(
    y_test,
    y_prob_dt
)

print("ROC-AUC:", roc_auc_dt)
print("PR-AUC:", pr_auc_dt)

print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)


print("----------------RANDOM FOREST----------------------")
# RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier(random_state=42,max_depth=10,class_weight="balanced",n_estimators=100,n_jobs=-1)
rf.fit(X_train,y_train)

y_prob_rf = rf.predict_proba(X_test)[:,1]
y_pred_rf=rf.predict(X_test)

print(classification_report(y_test,y_pred_rf))
print(confusion_matrix(y_test,y_pred_rf))
precision_rf=precision_score(y_test, y_pred_rf)
recall_rf=recall_score(y_test, y_pred_rf)
f1_rf=f1_score(y_test, y_pred_rf)

roc_auc_rf = roc_auc_score(
    y_test,
    y_prob_rf
)

pr_auc_rf = average_precision_score(
    y_test,
    y_prob_rf
)

print("ROC-AUC:", roc_auc_rf)
print("PR-AUC:", pr_auc_rf)

print("Precision:", precision_rf)
print("Recall:", recall_rf)
print("F1:", f1_rf)

feature_importance = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": rf.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print(feature_importance)

print(
    pd.crosstab(
        train_df["type"],
        train_df["isFraud"],
        normalize="index"
    ) * 100
)

print("----------------XGBOOST----------------------")
# XGBOOST
from xgboost import XGBClassifier

xgb=XGBClassifier(random_state=42,max_depth=6,learning_rate=0.1,n_estimators=200,n_jobs=-1,scale_pos_weight=scale_pos_weight,objective="binary:logistic",eval_metric="logloss")
xgb.fit(X_train,y_train)

y_prob_xgb=xgb.predict_proba(X_test)[:,1]
y_pred_xgb=xgb.predict(X_test)

print(classification_report(y_test,y_pred_xgb))
print(confusion_matrix(y_test,y_pred_xgb))
precision_xgb=precision_score(y_test, y_pred_xgb)
recall_xgb=recall_score(y_test, y_pred_xgb)
f1_xgb=f1_score(y_test, y_pred_xgb)

roc_auc_xgb = roc_auc_score(
    y_test,
    y_prob_xgb
)

pr_auc_xgb = average_precision_score(
    y_test,
    y_prob_xgb
)

print("ROC-AUC:", roc_auc_xgb)
print("PR-AUC:", pr_auc_xgb)
print("Precision:", precision_xgb)
print("Recall:", recall_xgb)
print("F1:", f1_xgb)


# Saving Model
import joblib

joblib.dump(
    rf,
    ROOT_DIR/"models"/"random_forest.pkl"
)

joblib.dump(
    xgb,
    ROOT_DIR/"models"/"xgboost.pkl"
)