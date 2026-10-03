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


print("Shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum().sum())
print("\nData types:")
print(df.dtypes)

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["New", "Early", "Established", "Loyal"]
)

print("\nTenure Groups:")
print(df["TenureGroup"].value_counts())


print(
    pd.crosstab(
        df["TenureGroup"],
        df["Churn"],
        normalize="index"
    ) * 100
)


service_columns = [
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies"
]

df["ServiceCount"] = (
    df[service_columns] == "Yes"
).sum(axis=1)

print("\nService Count:")
print(df["ServiceCount"].value_counts().sort_index())


print("\nService Count Statistics:")
print(df["ServiceCount"].describe())


print(
    pd.crosstab(
        df["ServiceCount"],
        df["Churn"],
        normalize="index"
    ) * 100
)



print("\nFeature Review:")
print(
    df[
        [
            "tenure",
            "TenureGroup",
            "ServiceCount",
            "Churn"
        ]
    ].head(10)
)



print("\nNew Feature Missing Values:")
print(
    df[
        [
            "TenureGroup",
            "ServiceCount"
        ]
    ].isnull().sum()
)




