import sqlite3
import pandas as pd

conn=sqlite3.connect("fraud_detection.db")
df=pd.read_sql("SELECT * FROM predictions",conn)
print(df)