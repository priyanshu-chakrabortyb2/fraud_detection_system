# Exploratory Data Analysis Report

## Project

AI-Powered Fraud Detection System

## Dataset

PaySim Mobile Money Fraud Detection Dataset (Kaggle)

# Dataset Overview

| Metric            | Value     |
| ----------------- | --------- |
| Total Records     | 6,362,620 |
| Total Features    | 11        |
| Missing Values    | 0         |
| Duplicate Records | 0         |

### Observations

* Dataset is extremely clean.
* No missing value handling required.
* No duplicate removal required.

# Feature Summary

## Numerical Features

* step
* amount
* oldbalanceOrg
* newbalanceOrig
* oldbalanceDest
* newbalanceDest
* isFraud
* isFlaggedFraud

## Categorical Features

* type
* nameOrig
* nameDest

# Target Variable Analysis

## Fraud Distribution

| Class       | Count     |
| ----------- | --------- |
| Genuine (0) | 6,354,407 |
| Fraud (1)   | 8,213     |

Fraud Rate:

0.129%

### Observations

* Dataset is highly imbalanced.
* Accuracy is not an appropriate evaluation metric.
* Precision, Recall, F1 Score and PR-AUC will be used.


# Transaction Type Analysis

Fraud occurs only in:

* CASH_OUT
* TRANSFER

No fraud found in:

* CASH_IN
* PAYMENT
* DEBIT

### Fraud Percentage by Transaction Type

| Transaction Type | Fraud Percentage |
| ---------------- | ---------------- |
| TRANSFER         | 0.769%           |
| CASH_OUT         | 0.184%           |
| CASH_IN          | 0.000%           |
| PAYMENT          | 0.000%           |
| DEBIT            | 0.000%           |

### Observations

* TRANSFER transactions are the riskiest.
* Fraudsters primarily move funds through TRANSFER and CASH_OUT operations.

# Transaction Amount Analysis

Overall Transaction Amount Statistics:

* Mean Amount: 179,861.90
* Median Amount: 74,871.94
* Maximum Amount: 92,445,516.64

Fraud Transaction Statistics:

* Mean Amount: 1,467,967
* Median Amount: 441,423

### Observations

* Fraudulent transactions involve significantly larger amounts.
* Transaction amount is expected to be an important predictive feature.

# Correlation Analysis

Top Features Correlated With Fraud:

| Feature        | Correlation |
| -------------- | ----------- |
| amount         | 0.0767      |
| isFlaggedFraud | 0.0441      |
| step           | 0.0316      |

### Observations

* Correlations are relatively low.
* Non-linear models such as XGBoost are expected to perform better than linear models.


# Leakage Analysis

## isFlaggedFraud

Distribution:

* 16 records flagged
* All 16 records are fraudulent

### Observation

The feature contains information that is strongly related to the target.

### Decision

Drop:

* isFlaggedFraud

Reason:

Potential data leakage as the model could cheat during testing
# Feature Selection Decisions

## Features To Keep

* step
* type
* amount
* oldbalanceOrg
* newbalanceOrig
* oldbalanceDest
* newbalanceDest

## Features To Drop

* nameOrig
* nameDest
* isFlaggedFraud

### Reasons

nameOrig and nameDest:

* High-cardinality account identifiers
* Not suitable for MVP modeling

isFlaggedFraud:

* Potential target leakage

# Conclusion

The dataset is clean and suitable for modeling.

Key findings:

* Fraud is extremely rare (0.129%).
* Fraud occurs primarily in TRANSFER and CASH_OUT transactions.
* Fraudulent transactions involve significantly higher amounts.
* isFlaggedFraud introduces data leakage and will be removed.
* Additional balance-based features are expected to improve model performance.

The next phase will focus on preprocessing and feature engineering.
