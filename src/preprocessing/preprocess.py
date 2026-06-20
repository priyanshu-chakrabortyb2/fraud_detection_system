import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import  Path

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT_DIR / "data" / "raw" / "PS_20174392719_1491204439457_log.csv"
df=pd.read_csv(DATA_PATH)
print(df.shape)

# Droping these columns as they are millions and are not useful  for us
cols_to_drop=["nameOrig","nameDest","isFlaggedFraud"]
df=df.drop(columns=cols_to_drop)

print(df.shape)

print(df.columns.to_list())

print(df["type"].unique())

from sklearn.preprocessing import LabelEncoder

encoder=LabelEncoder()

df['type']=encoder.fit_transform(df["type"])

print(df.head())
print(df["type"].value_counts())
print(dict(
    zip(
        encoder.classes_,
        encoder.transform(
            encoder.classes_
        )
    )
)
)


X=df.drop(columns=["isFraud"])
y=df["isFraud"]


X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42,stratify=y
)


print("Train Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

print()

print("Train Fraud %")
print(y_train.mean()*100)

print()

print("Test Fraud %")
print(y_test.mean()*100)

train_df = X_train.copy()
train_df["isFraud"] = y_train

test_df = X_test.copy()
test_df["isFraud"] = y_test


train_df.to_csv(
    "data/processed/train.csv",
    index=False
)

test_df.to_csv(
    "data/processed/test.csv",
    index=False
)

print("Files Saved Successfully")