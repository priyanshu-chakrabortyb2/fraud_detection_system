# Phase 6: FastAPI Backend Development

## Objective

The objective of this phase was to transform the trained fraud detection model into a production-ready REST API using FastAPI. This enables real-time fraud prediction, risk assessment, and explainable AI outputs through HTTP endpoints.

---

# Technologies Used

* FastAPI
* Uvicorn
* Pydantic
* Scikit-Learn
* Random Forest Classifier
* SHAP
* Python

---

# API Architecture

The backend follows a modular architecture.

```text
Client Request
      |
      v
FastAPI Endpoint
      |
      v
Input Validation (Pydantic)
      |
      v
Prediction Engine
      |
      +----------------+
      |                |
      v                v
Random Forest      SHAP Explainer
      |                |
      +--------+-------+
               |
               v
        Risk Engine
               |
               v
        JSON Response
```

---

# Project Structure

```text
fraud_detection_system/

├── api/
│   ├── app.py
│   ├── predictor.py
│   ├── schemas.py
│   └── __init__.py
│
├── src/
│   └── explainability/
│       ├── explanation_engine.py
│       ├── risk_engine.py
│       └── shap_analysis.py
│
├── models/
│   └── random_forest.pkl
│
└── reports/
    └── api_backend_report.md
```

---

# Endpoint Overview

## Root Endpoint

### GET /

Purpose:

Verify API availability.

Response:

```json
{
  "message": "Fraud Detection API Running"
}
```

---

## Health Endpoint

### GET /health

Purpose:

Monitor API health.

Response:

```json
{
  "status": "healthy"
}
```

---

## Metrics Endpoint

### GET /metrics

Purpose:

Provide model performance metrics.

Response:

```json
{
  "model": "Random Forest",
  "precision": 0.99695,
  "recall": 0.99574,
  "f1_score": 0.99635,
  "roc_auc": 0.99906,
  "pr_auc": 0.99756
}
```

---

## Prediction Endpoint

### POST /predict

Purpose:

Generate fraud predictions for incoming transactions.

Input Example:

```json
{
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
  "hour_of_day": 12
}
```

---

# Prediction Pipeline

1. Receive transaction data.
2. Validate request using Pydantic schema.
3. Convert input into DataFrame format.
4. Generate Random Forest prediction.
5. Calculate fraud probability.
6. Compute risk score.
7. Assign risk category.
8. Generate SHAP values.
9. Create human-readable explanations.
10. Return final response.

---

# Risk Engine

Fraud probability is converted into a risk score.

Formula:

```text
Risk Score = Fraud Probability × 100
```

Risk Categories:

| Risk Score | Category    |
| ---------- | ----------- |
| 0 - 49     | Low Risk    |
| 50 - 79    | Medium Risk |
| 80 - 100   | High Risk   |

Example:

```text
Fraud Probability = 0.47

Risk Score = 47

Risk Category = Low Risk
```

---

# Explainability Integration

SHAP TreeExplainer was integrated into the prediction pipeline.

Benefits:

* Feature-level explanations
* Model transparency
* Improved trust
* Easier fraud investigation
* Regulatory compliance support

Example Explanation:

```json
{
  "reasons": [
    "Sender balance discrepancy reduced fraud risk",
    "Transaction-to-balance ratio increased fraud risk",
    "Transaction type increased fraud risk",
    "Receiver balance discrepancy reduced fraud risk",
    "Post-transaction balance increased fraud risk"
  ]
}
```

---

# Example API Response

```json
{
  "prediction": "Non-Fraud",
  "fraud_probability": 0.47,
  "risk_score": 47,
  "risk_category": "Low Risk",
  "reasons": [
    "Sender balance discrepancy reduced fraud risk",
    "Transaction-to-balance ratio increased fraud risk",
    "Transaction type increased fraud risk",
    "Receiver balance discrepancy reduced fraud risk",
    "Post-transaction balance increased fraud risk"
  ]
}
```

---

# Swagger Documentation

FastAPI automatically generated interactive API documentation.

Available at:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI enables:

* Endpoint testing
* Request validation
* Response inspection
* API debugging

---

# Deliverables Completed

* FastAPI Setup
* Uvicorn Configuration
* Pydantic Schema Validation
* Random Forest Model Serving
* Risk Scoring Engine Integration
* SHAP Explainability Integration
* GET / Endpoint
* GET /health Endpoint
* GET /metrics Endpoint
* POST /predict Endpoint
* Swagger UI Documentation

---

# Phase 6 Outcome

A production-ready fraud detection API was successfully developed. The system now supports real-time fraud prediction, risk assessment, and explainable AI outputs through REST endpoints. The backend serves as the foundation for dashboard integration, database logging, containerization, and cloud deployment in later phases.
