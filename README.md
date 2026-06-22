# 🛡️ AI-Powered Fraud Detection System

An end-to-end Explainable AI (XAI) powered Fraud Detection Platform built using Machine Learning, FastAPI, Streamlit, Docker, and MLflow.

The system analyzes financial transactions in real time, predicts fraudulent activity, generates explainable insights using SHAP, calculates risk scores, stores prediction history, and provides an analytics dashboard for monitoring.

---

# 🚀 Features

## Fraud Detection
- Real-time fraud prediction
- Random Forest based classification model
- XGBoost benchmark model

## Explainable AI (XAI)
- SHAP feature attribution
- Human-readable fraud explanations
- Risk factor analysis

## Risk Scoring Engine
- Fraud probability calculation
- Risk score generation (0-100)
- Risk categorization:
  - Low Risk
  - Medium Risk
  - High Risk

## FastAPI Backend
- RESTful API
- Swagger documentation
- Health monitoring endpoint

## Database Integration
- SQLite database
- Prediction history storage
- Historical lookup endpoints

## Analytics Dashboard
- Streamlit web application
- Fraud statistics
- Prediction history
- Interactive visualizations
- Risk distribution analytics

## MLOps
- Docker containerization
- MLflow Experiment Tracking
- MLflow Model Registry

---

# 📊 Dataset

Dataset Used:

**PaySim Fraud Detection Dataset**

Dataset Characteristics:

- Total Records: 6.3 Million+
- Transaction Types:
  - CASH_IN
  - CASH_OUT
  - DEBIT
  - PAYMENT
  - TRANSFER

Target Variable:

```text
isFraud
0 → Legitimate Transaction
1 → Fraudulent Transaction
```

---

# 🛠️ Tech Stack

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost

## Explainability

- SHAP

## Backend

- FastAPI
- Uvicorn

## Frontend

- Streamlit
- Plotly

## Database

- SQLite
- SQLAlchemy

## MLOps

- Docker
- Docker Compose
- MLflow

---

# 📂 Project Structure

```text
fraud_detection_system/

├── api/
│   ├── app.py
│   ├── predictor.py
│   └── schemas.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── database.py
│   ├── models.py
│   └── crud.py
│
├── models/
│   ├── random_forest.pkl
│   └── xgboost.pkl
│
├── src/
│   ├── preprocessing/
│   ├── feature_engineering/
│   ├── training/
│   └── explainability/
│
├── data/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🏗️ System Architecture

```text
                        +------------------+
                        | PaySim Dataset   |
                        +--------+---------+
                                 |
                                 v
                    +-------------------------+
                    | Data Preprocessing      |
                    +------------+------------+
                                 |
                                 v
                    +-------------------------+
                    | Feature Engineering     |
                    +------------+------------+
                                 |
                                 v
                    +-------------------------+
                    | Model Training          |
                    | RF + XGBoost            |
                    +------------+------------+
                                 |
                                 v
                    +-------------------------+
                    | SHAP Explainability     |
                    +------------+------------+
                                 |
                                 v
                    +-------------------------+
                    | FastAPI Backend         |
                    +------------+------------+
                                 |
           +---------------------+----------------------+
           |                                            |
           v                                            v
+-------------------------+            +-------------------------+
| SQLite Database         |            | Streamlit Dashboard     |
| Prediction History      |            | Analytics & Monitoring  |
+-------------------------+            +-------------------------+
           |
           v
+-------------------------+
| MLflow Tracking         |
| Model Registry          |
+-------------------------+
```

---

# 📈 Model Performance

## Random Forest

| Metric | Score |
|----------|----------|
| Precision | 0.99695 |
| Recall | 0.99574 |
| F1 Score | 0.99635 |
| ROC-AUC | 0.99906 |
| PR-AUC | 0.99756 |

---

# 🔌 API Endpoints

## Health Check

```http
GET /health
```

## Fraud Prediction

```http
POST /predict
```

## Prediction History

```http
GET /history
```

## Prediction By ID

```http
GET /history/{id}
```

## Model Metrics

```http
GET /metrics
```

---

# 🐳 Docker Deployment

Build Image:

```bash
docker build -t fraud-api .
```

Run Container:

```bash
docker run -p 8000:8000 fraud-api
```

Docker Compose:

```bash
docker compose up
```

---

# 📊 MLflow

Features Implemented:

- Experiment Tracking
- Metric Logging
- Parameter Tracking
- Artifact Storage
- Model Registry
- Version Management

Launch MLflow:

```bash
mlflow ui
```

Access:

```text
http://127.0.0.1:5000
```

---

# 🎯 Future Enhancements

- Real-time Kafka Streaming
- Cloud Deployment (AWS/GCP/Azure)
- Drift Detection
- Model Monitoring
- CI/CD Pipeline
- User Authentication
- Role-Based Access Control

---

# 👨‍💻 Author

Priyanshu Chakraborty

B.Tech Computer Science Engineering

Machine Learning | Data Science | MLOps | Backend Development