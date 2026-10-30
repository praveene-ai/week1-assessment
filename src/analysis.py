import pandas as pd
import timeit

df = pd.read_csv("data/employees.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df = df.drop_duplicates()
df["salary"] = df["salary"].fillna(df["salary"].median())

print(df)
print(df.groupby("department")["salary"].mean())
print(df["department"].value_counts())
print(df.loc[df["salary"].idxmax()])

print(timeit.timeit(lambda: pd.read_csv("data/employees.csv"), number=100))