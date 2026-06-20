# Feature Engineering Report

## Objective

Enhance fraud detection performance by creating domain-specific features that capture transaction behavior and account balance anomalies.

## New Features Created

### 1. balance_diff_orig

Formula:

oldbalanceOrg - newbalanceOrig

Purpose:

Captures the balance reduction in the sender account.

---

### 2. balance_diff_dest

Formula:

newbalanceDest - oldbalanceDest

Purpose:

Captures the increase in the receiver account balance.

---

### 3. amount_to_balance_ratio

Formula:

amount / (oldbalanceOrg + 1)

Purpose:

Measures transaction size relative to account balance.

---

### 4. is_zero_balance_org

Formula:

(oldbalanceOrg == 0)

Purpose:

Flags accounts with zero starting balance.

---

### 5. is_zero_balance_dest

Formula:

(oldbalanceDest == 0)

Purpose:

Flags destination accounts with zero balance.

---

### 6. hour_of_day

Formula:

step % 24

Purpose:

Captures temporal transaction behavior.

---

## Results

Original Features: 8

Engineered Features: 7

Total Features: 15

Train Dataset Shape:

(5090096, 15)

Test Dataset Shape:

(1272524, 15)

## Conclusion

Feature engineering successfully expanded the feature space and introduced fraud-focused behavioral indicators expected to improve model performance.
