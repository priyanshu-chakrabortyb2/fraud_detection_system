import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ==================================
# CONFIG
# ==================================
import os
API_URL = os.getenv("API_URL","https://127.0.0.1:8000");

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🛡️",
    layout="wide"
)

# ==================================
# BACKEND STATUS
# ==================================

try:
    response = requests.get(
        f"{API_URL}/health",
        timeout=2
    )

    if response.status_code == 200:
        st.sidebar.success(
            "🟢 Backend Connected"
        )
    else:
        st.sidebar.error(
            "🔴 Backend Offline"
        )

except:
    st.sidebar.error(
        "🔴 Backend Offline"
    )

# ==================================
# TITLE
# ==================================

st.title("🛡️ Fraud Detection System")

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Predict",
        "History",
        "Analytics"
    ]
)

# ==================================
# PREDICT PAGE
# ==================================

if page == "Predict":

    st.header("Transaction Prediction")

    transaction_type = st.selectbox(
        "Transaction Type",
        [
            "CASH_IN",
            "CASH_OUT",
            "DEBIT",
            "PAYMENT",
            "TRANSFER"
        ]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        value=1000.0
    )

    oldbalanceOrg = st.number_input(
        "Sender Balance Before",
        min_value=0.0
    )

    newbalanceOrig = st.number_input(
        "Sender Balance After",
        min_value=0.0
    )

    oldbalanceDest = st.number_input(
        "Receiver Balance Before",
        min_value=0.0
    )

    newbalanceDest = st.number_input(
        "Receiver Balance After",
        min_value=0.0
    )

    if st.button("Predict Fraud"):

        type_mapping = {
            "CASH_IN": 0,
            "CASH_OUT": 1,
            "DEBIT": 2,
            "PAYMENT": 3,
            "TRANSFER": 4
        }

        sample = {
            "step": 300,
            "type": type_mapping[
                transaction_type
            ],
            "amount": amount,

            "oldbalanceOrg":
                oldbalanceOrg,

            "newbalanceOrig":
                newbalanceOrig,

            "oldbalanceDest":
                oldbalanceDest,

            "newbalanceDest":
                newbalanceDest,

            "balance_diff_orig":
                oldbalanceOrg -
                newbalanceOrig,

            "balance_diff_dest":
                oldbalanceDest -
                newbalanceDest,

            "amount_to_balance_ratio":
                (
                    amount /
                    oldbalanceOrg
                )
                if oldbalanceOrg > 0
                else 0,

            "is_zero_balance_org":
                int(
                    oldbalanceOrg == 0
                ),

            "is_zero_balance_dest":
                int(
                    oldbalanceDest == 0
                ),

            "hour_of_day": 12
        }

        try:

            response = requests.post(
                f"{API_URL}/predict",
                json=sample
            )

            result = response.json()

            st.success(
                "Prediction Complete"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Prediction",
                    result["prediction"]
                )

            with col2:
                st.metric(
                    "Fraud Probability",
                    f"{result['fraud_probability']*100:.2f}%"
                )

            with col3:
                st.metric(
                    "Risk Score",
                    result["risk_score"]
                )

            st.subheader(
                "Risk Category"
            )

            if (
                result["risk_category"]
                == "High Risk"
            ):
                st.error(
                    result["risk_category"]
                )

            elif (
                result["risk_category"]
                == "Medium Risk"
            ):
                st.warning(
                    result["risk_category"]
                )

            else:
                st.success(
                    result["risk_category"]
                )

            st.subheader(
                "Explanation"
            )

            for reason in result[
                "reasons"
            ]:
                st.write(
                    f"• {reason}"
                )

        except Exception as e:

            st.error(
                f"Prediction failed: {e}"
            )

# ==================================
# HISTORY PAGE
# ==================================

elif page == "History":

    st.header(
        "Prediction History"
    )

    try:

        response = requests.get(
            f"{API_URL}/history"
        )

        history = response.json()

        df = pd.DataFrame(
            history
        )

        if df.empty:

            st.warning(
                "No history records found"
            )

            st.stop()

        df = df.sort_values(
            by="id",
            ascending=False
        )

        st.metric(
            "Total Records",
            len(df)
        )

        csv = df.to_csv(
            index=False
        )

        st.download_button(
            label="Download History CSV",
            data=csv,
            file_name=
            "prediction_history.csv",
            mime="text/csv"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Failed to load history: {e}"
        )

# ==================================
# ANALYTICS PAGE
# ==================================

elif page == "Analytics":

    st.header(
        "Analytics Dashboard"
    )

    try:

        response = requests.get(
            f"{API_URL}/history"
        )

        history = response.json()

        df = pd.DataFrame(
            history
        )

        if df.empty:

            st.warning(
                "No analytics data available"
            )

            st.stop()

        total_predictions = len(df)

        fraud_count = len(
            df[
                df["prediction"]
                == "Fraud"
            ]
        )

        non_fraud_count = len(
            df[
                df["prediction"]
                == "Non-Fraud"
            ]
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Predictions",
                total_predictions
            )

        with col2:

            st.metric(
                "Fraud Predictions",
                fraud_count
            )

        with col3:

            st.metric(
                "Non-Fraud Predictions",
                non_fraud_count
            )

        # PIE CHART

        prediction_counts = (
            df["prediction"]
            .value_counts()
            .reset_index()
        )

        prediction_counts.columns = [
            "Prediction",
            "Count"
        ]

        fig = px.pie(
            prediction_counts,
            values="Count",
            names="Prediction",
            title=
            "Fraud vs Non-Fraud Predictions"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # BAR CHART

        risk_counts = (
            df["risk_category"]
            .value_counts()
            .reset_index()
        )

        risk_counts.columns = [
            "Risk Category",
            "Count"
        ]

        fig2 = px.bar(
            risk_counts,
            x="Risk Category",
            y="Count",
            title=
            "Risk Category Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        st.subheader(
            "Prediction Records"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Analytics failed: {e}"
        )