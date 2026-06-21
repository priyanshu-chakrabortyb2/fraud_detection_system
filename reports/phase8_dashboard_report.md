# Phase 8: Streamlit Dashboard Report

## Project

AI-Powered Fraud Detection System

## Objective

The objective of Phase 8 was to develop an interactive Streamlit dashboard that allows users to submit transaction details, obtain fraud predictions from the trained machine learning model, view explainability insights, and analyze historical prediction records through visual dashboards.

---

# Dashboard Architecture

```text
User Input
    ↓
Streamlit Dashboard
    ↓
FastAPI Backend
    ↓
Random Forest Model
    ↓
Risk Engine
    ↓
SHAP Explainability
    ↓
SQLite Database
```

The dashboard communicates with the FastAPI backend using REST APIs and displays predictions in real time.

---

# Features Implemented

## 1. Transaction Prediction Interface

Users can enter transaction information including:

* Transaction Type
* Transaction Amount
* Sender Balance Before
* Sender Balance After
* Receiver Balance Before
* Receiver Balance After

The dashboard automatically sends the transaction data to the FastAPI `/predict` endpoint.

---

## 2. Fraud Prediction Results

The dashboard displays:

* Fraud / Non-Fraud Prediction
* Fraud Probability
* Risk Score
* Risk Category

Example:

```text
Prediction: Fraud
Fraud Probability: 99.98%
Risk Score: 100
Risk Category: High Risk
```

---

## 3. Explainable AI Integration

SHAP explanations are displayed for every prediction.

Example explanations:

* Transaction type increased fraud risk
* Sender balance discrepancy increased fraud risk
* High transaction-to-balance ratio detected

This provides transparency and interpretability for model decisions.

---

## 4. Prediction History

A dedicated History page was developed.

Features:

* Retrieve all historical predictions from SQLite database
* Display prediction records in tabular format
* Sort records by prediction ID
* Review previous model decisions

Stored information:

* Prediction
* Fraud Probability
* Risk Score
* Risk Category
* Explanation Reasons

---

## 5. CSV Export

Users can export prediction history as CSV.

Benefits:

* Offline analysis
* Auditing
* Reporting
* Data archival

---

## 6. Analytics Dashboard

An analytics section was implemented to summarize prediction activity.

Metrics displayed:

* Total Predictions
* Fraud Predictions
* Non-Fraud Predictions

---

## 7. Fraud Distribution Visualization

A Pie Chart was implemented using Plotly.

Purpose:

* Visualize fraud vs non-fraud prediction proportions
* Provide quick operational insights

---

## 8. Risk Category Visualization

A Bar Chart was implemented using Plotly.

Categories:

* Low Risk
* Medium Risk
* High Risk

Purpose:

* Analyze risk distribution across transactions
* Monitor fraud exposure levels

---

## 9. Backend Health Monitoring

Dashboard verifies FastAPI connectivity using the `/health` endpoint.

Status indicators:

* Backend Connected
* Backend Offline

This improves reliability and operational monitoring.

---

# Technologies Used

## Frontend

* Streamlit

## Visualization

* Plotly
* Pandas

## Backend

* FastAPI

## Machine Learning

* Random Forest Classifier
* SHAP Explainability

## Database

* SQLite
* SQLAlchemy

---

# API Endpoints Consumed

## GET /health

Purpose:

* Backend health verification

---

## POST /predict

Purpose:

* Fraud prediction
* Risk scoring
* SHAP explanation generation

---

## GET /history

Purpose:

* Retrieve historical prediction records

---

# Dashboard Pages

## Predict Page

Features:

* Transaction input form
* Fraud prediction
* Risk score display
* Risk category display
* SHAP explanation display

---

## History Page

Features:

* Historical prediction records
* CSV download
* Database integration

---

## Analytics Page

Features:

* Summary statistics
* Fraud distribution chart
* Risk category chart
* Prediction monitoring

---

# Testing Performed

## Prediction Testing

Verified:

* FastAPI communication
* Model prediction accuracy
* Risk score generation
* SHAP explanation generation

---

## Database Testing

Verified:

* Prediction persistence
* Record retrieval
* History endpoint functionality

---

## Dashboard Testing

Verified:

* Streamlit rendering
* Navigation functionality
* Chart visualization
* CSV export

---

# Phase 8 Deliverables

Completed Deliverables:

* Streamlit Dashboard
* Prediction Interface
* FastAPI Integration
* Explainable AI Display
* Prediction History
* CSV Export
* Analytics Dashboard
* Fraud Distribution Chart
* Risk Category Chart
* Backend Monitoring

---

# Outcome

Phase 8 successfully transformed the fraud detection pipeline into an interactive end-to-end application. Users can now submit transactions, receive fraud predictions, understand model reasoning through SHAP explanations, review historical records, and analyze fraud trends through visual dashboards.

Status: COMPLETED

