import pandas  as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print(df.head())

print(df.shape)


print(df.head(10))


print(df.columns)


print(df.dtypes)

print(df.isnull().sum())


print(df.duplicated().sum())


print(df["Churn"].value_counts())