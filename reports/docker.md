# Phase 9: Dockerization & End-to-End Validation Report

## Objective

The objective of Phase 9 was to containerize the complete Fraud Detection System using Docker and Docker Compose, enabling consistent deployment across different environments while validating the entire end-to-end ML pipeline.

---

## Components Dockerized

### Backend Container

Technology Stack:

* FastAPI
* Random Forest Model
* SHAP Explainability Engine
* SQLite Database
* Uvicorn Server

Responsibilities:

* Load trained Random Forest model
* Generate fraud predictions
* Calculate fraud probability
* Generate SHAP-based explanations
* Calculate risk scores
* Store prediction history
* Serve REST APIs

Exposed Port:

* 8000

---

### Frontend Container

Technology Stack:

* Streamlit
* Plotly
* Requests

Responsibilities:

* Transaction input interface
* Prediction visualization
* History management
* Analytics dashboard
* Backend communication

Exposed Port:

* 8501

---

## Docker Files Created

### Backend Dockerfile

Purpose:

* Build FastAPI service container
* Install project dependencies
* Load trained model
* Launch Uvicorn server

### Frontend Dockerfile

Purpose:

* Build Streamlit dashboard container
* Install dashboard dependencies
* Launch Streamlit application

### Docker Compose Configuration

Purpose:

* Orchestrate frontend and backend services
* Configure networking
* Enable inter-container communication

---

## Networking Configuration

Frontend and backend containers communicate through Docker internal networking.

API Endpoint Used:

http://backend:8000

This replaced:

http://127.0.0.1:8000

which only works outside Docker.

---

## Validation Tests Performed

### Test Case 1 – Normal Transfer

Input:

Transaction Type: TRANSFER
Amount: 900000

Sender Balance Before: 900000
Sender Balance After: 0

Receiver Balance Before: 0
Receiver Balance After: 900000

Result:

Prediction: Non-Fraud
Fraud Probability: 46%
Risk Score: 46
Risk Category: Low Risk

Observation:

The destination account balance updated correctly after the transfer, indicating normal transaction behavior.

---

### Test Case 2 – Suspicious Transfer

Input:

Transaction Type: TRANSFER
Amount: 1000000

Sender Balance Before: 1000000
Sender Balance After: 0

Receiver Balance Before: 0
Receiver Balance After: 0

Result:

Prediction: Fraud
Fraud Probability: 67.97%
Risk Score: 68
Risk Category: Medium Risk

Observation:

The destination account balance did not update after money was transferred. The model correctly identified this pattern as suspicious and increased fraud probability significantly.

---

## Explainable AI Validation

SHAP explanations were successfully generated for every prediction.

Example Explanations:

* Transaction-to-balance ratio increased fraud risk
* Transaction type increased fraud risk
* Sender account balance pattern increased fraud risk
* Receiver balance discrepancy reduced fraud risk

This confirms the Explainable AI pipeline is functioning correctly inside Docker containers.

---

## Analytics Dashboard Validation

Successfully validated:

* Total prediction count
* Fraud prediction count
* Non-fraud prediction count
* Prediction history table
* Fraud vs Non-Fraud Pie Chart
* Risk Category Distribution Bar Chart
* CSV export functionality

---

## Database Validation

SQLite database successfully persisted:

* Prediction result
* Fraud probability
* Risk score
* Risk category
* SHAP explanations

History endpoint correctly retrieved stored records.

---

## Deployment Validation

Successfully executed:

docker build
docker compose up
docker compose down

Verified:

* Backend health endpoint
* API connectivity
* Container networking
* Model loading
* Dashboard accessibility

---

## Challenges Faced

### Docker Daemon Not Running

Issue:
Docker API connection failure.

Resolution:
Started Docker Desktop and verified Docker Engine status.

---

### Port Conflict on Port 8000

Issue:
Port already allocated.

Resolution:
Identified existing running container and removed conflicting service.

---

### Backend Offline in Dashboard

Issue:
Frontend attempted to access localhost inside container.

Resolution:
Replaced localhost with Docker service hostname:

http://backend:8000

---

## Outcome

The complete Fraud Detection System is now fully containerized and operational.

Features Successfully Integrated:

✓ Machine Learning Prediction Engine

✓ Feature Engineering Pipeline

✓ Explainable AI using SHAP

✓ Risk Scoring System

✓ FastAPI Backend

✓ SQLite Database

✓ Prediction History

✓ Analytics Dashboard

✓ Dockerized Deployment

✓ End-to-End Validation

---

## Phase 9 Status

Status: COMPLETED
