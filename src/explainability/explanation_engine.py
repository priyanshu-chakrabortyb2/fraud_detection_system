def explain_transaction(shap_df):

    reasons = []

    top_features = shap_df.reindex(
        shap_df["SHAP_Value"].abs().sort_values(
            ascending=False
        ).index
    )

    feature_map = {
        "balance_diff_orig": "Sender balance discrepancy",
        "amount_to_balance_ratio": "Transaction-to-balance ratio",
        "type": "Transaction type",
        "oldbalanceOrg": "Sender account balance pattern",
        "hour_of_day": "Transaction timing",
        "newbalanceOrig": "Post-transaction balance",
        "balance_diff_dest": "Receiver balance discrepancy"
    }

    for _, row in top_features.head(5).iterrows():

        feature = row["Feature"]

        feature_name = feature_map.get(
            feature,
            feature
        )

        direction = (
            "increased fraud risk"
            if row["SHAP_Value"] > 0
            else "reduced fraud risk"
        )

        reasons.append(
            f"{feature_name} {direction}"
        )

    return reasons