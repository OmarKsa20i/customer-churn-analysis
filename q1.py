import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df.head())

print(df.shape)

print(df.head(10))

print(df.columns)

print(df.dtypes)

print(df.isnull().sum())

print(df.duplicated().sum())

print(df["Churn"].value_counts())

print(df[["TotalCharges", "SeniorCitizen", "Churn"]].dtypes)


for col in ["gender", "Contract", "PaymentMethod", "InternetService", "TechSupport", "Churn"]:
    print(f"\n{col}:")
    print(df[col].unique())


    print(df[["tenure", "MonthlyCharges", "TotalCharges"]].describe().loc[["min", "max", "mean"]])

print("Missing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nFinal shape:")
print(df.shape)