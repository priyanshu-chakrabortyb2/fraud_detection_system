import pandas as pd
from pathlib import Path

ROOT_DIR=Path(__file__).resolve().parents[2]
train_df=pd.read_csv(ROOT_DIR/"data"/"processed"/"train.csv")
test_df=pd.read_csv(ROOT_DIR/"data"/"processed"/"test.csv")

print("Here")

print(train_df.shape)
print(test_df.shape)

print(train_df.columns.to_list())


# Create new features
def create(df):
    df=df.copy()

    # feature 1
    df["balance_diff_orig"]=(df["newbalanceOrig"]-df["oldbalanceOrg"])

    # feature 2
    df["balance_diff_dest"]=(df["newbalanceDest"]-df["oldbalanceDest"])

    # feature 3
    df["amount_to_balance_ratio"]=(df["amount"]/(df["oldbalanceOrg"]+1))

    # feature 4
    df["is_zero_balance_org"]=(df["oldbalanceOrg"]==0).astype(int)

    # feature 5
    df["is_zero_balance_dest"]=(df["oldbalanceDest"]==0).astype(int)

    # feature 7
    df["hour_of_day"]=(df["step"]%24)

    return df

train_df=create(train_df)
test_df=create(test_df)

print(train_df.columns.to_list())
print(train_df.shape)
print(test_df.shape)

print(train_df[["balance_diff_orig","balance_diff_dest","amount_to_balance_ratio"]].describe())

print("Missing Values:",train_df.isnull().sum().sum())
import numpy as np

print("Infinite values:",np.isinf(train_df.select_dtypes(include=np.number)).sum().sum())

train_df.to_csv(ROOT_DIR/"data"/"processed"/"train_df.csv",index=False)
test_df.to_csv(ROOT_DIR/"data"/"processed"/"test_df.csv",index=False)