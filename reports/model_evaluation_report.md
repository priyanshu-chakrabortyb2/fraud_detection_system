# Model Evaluation Report

## Dataset Information

Dataset: PaySim Fraud Detection Dataset

Training Sample Size: 500,000 transactions

Test Size: 1,272,524 transactions

Fraud Rate: ~0.129%

Problem Type: Binary Classification

Target Variable:

* 0 = Genuine Transaction
* 1 = Fraudulent Transaction

---

## Models Evaluated

### 1. Logistic Regression

Results:

* Precision: 2.23%
* Recall: 93.06%
* F1 Score: 4.36%

Confusion Matrix:

* True Positives: 1529
* False Positives: 67009
* False Negatives: 114
* True Negatives: 1203872

Observations:

* Achieved very high recall.
* Generated a large number of false positives.
* Not suitable for production fraud detection due to poor precision.

---

### 2. Decision Tree

Results:

* Precision: 45.92%
* Recall: 96.90%
* F1 Score: 62.31%

Confusion Matrix:

* True Positives: 1592
* False Positives: 1875
* False Negatives: 51
* True Negatives: 1269006

Observations:

* Significant improvement over Logistic Regression.
* Captured non-linear fraud patterns effectively.
* Reduced false positives substantially.

---

### 3. Random Forest

Results:

* Precision: 99.70%
* Recall: 99.57%
* F1 Score: 99.63%

Confusion Matrix:

* True Positives: 1636
* False Positives: 5
* False Negatives: 7
* True Negatives: 1270876

Feature Importance:

1. balance_diff_orig (30.5%)
2. amount_to_balance_ratio (29.3%)
3. newbalanceOrig (8.4%)
4. oldbalanceOrg (7.7%)
5. type (6.0%)

Observations:

* Best overall performance.
* Extremely low false positive rate.
* Extremely low false negative rate.
* Strong utilization of engineered balance-based features.

---

### 4. XGBoost

Results:

* Precision: 98.01%
* Recall: 99.09%
* F1 Score: 98.55%

Confusion Matrix:

* True Positives: 1628
* False Positives: 33
* False Negatives: 15
* True Negatives: 1270848

Observations:

* Excellent performance.
* Slightly lower precision and F1 score than Random Forest.
* Strong alternative model for deployment.

---

## Model Comparison

| Model               | Precision | Recall | F1 Score |
| ------------------- | --------: | -----: | -------: |
| Logistic Regression |     2.23% | 93.06% |    4.36% |
| Decision Tree       |    45.92% | 96.90% |   62.31% |
| Random Forest       |    99.70% | 99.57% |   99.63% |
| XGBoost             |    98.01% | 99.09% |   98.55% |

---

## Why Random Forest Was Selected

Although XGBoost is generally considered a more advanced boosting algorithm, Random Forest was selected for this project because:

1. Higher Precision

   * Random Forest: 99.70%
   * XGBoost: 98.01%

   In fraud detection, false positives directly impact customer experience and investigation costs.

2. Higher F1 Score

   * Random Forest: 99.63%
   * XGBoost: 98.55%

   Random Forest achieved the best balance between precision and recall.

3. Lower False Positives

   * Random Forest: 5
   * XGBoost: 33

   Random Forest generated significantly fewer false fraud alerts.

4. Simpler Training Pipeline

   * Fewer hyperparameters.
   * Easier to explain and maintain.
   * Faster experimentation during MVP development.

5. Strong Feature Utilization

   Random Forest effectively leveraged engineered balance-related features without extensive tuning.

---

## Final Model Selection

Selected Model: Random Forest Classifier

Final Metrics:

* Precision: 99.70%
* Recall: 99.57%
* F1 Score: 99.63%

Reason:

Random Forest achieved the highest overall performance while maintaining the lowest false positive rate and the strongest balance between fraud detection capability and operational efficiency.

