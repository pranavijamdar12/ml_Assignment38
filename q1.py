import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("first 5 records:")
print(df.head())
print("\n last 5 records:")
print(df.tail())
print("\n total number of rows and coloumns:")
print(df.shape)
print("\n coloumns names:")
print(df.columns.tolist())
print("\n Data type of each column:")
print(df.dtypes)

