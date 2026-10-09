from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# Load Dataset
# =========================================================

df = pd.read_csv("Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)


# =========================================================
# 1. Verify Dataset
# =========================================================

print("========== DATASET VERIFICATION ==========")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nChurn Distribution:")
print(df["Churn"].value_counts())


# =========================================================
# 2. Churn Distribution
# =========================================================

print("\n========== CHURN DISTRIBUTION ==========")

churn_counts = df["Churn"].value_counts()

print(churn_counts)

print("\nChurn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)


# =========================================================
# 3. Churn Visualization
# =========================================================

plt.figure(figsize=(6, 4))

churn_counts.plot(kind="bar")

plt.title("Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# =========================================================
# 4. Gender vs Churn
# =========================================================

print("\n========== GENDER VS CHURN ==========")

gender_churn = pd.crosstab(
    df["gender"],
    df["Churn"]
)

print(gender_churn)

print("\nGender Churn Rate:")
print(
    pd.crosstab(
        df["gender"],
        df["Churn"],
        normalize="index"
    ) * 100
)

gender_churn.plot(
    kind="bar",
    figsize=(7, 4)
)

plt.title("Gender vs Churn")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")

plt.tight_layout()
plt.show()


# =========================================================
# 5. SeniorCitizen vs Churn
# =========================================================

print("\n========== SENIOR CITIZEN VS CHURN ==========")

senior_churn = pd.crosstab(
    df["SeniorCitizen"],
    df["Churn"]
)

print(senior_churn)

print("\nSeniorCitizen Churn Rate:")
print(
    pd.crosstab(
        df["SeniorCitizen"],
        df["Churn"],
        normalize="index"
    ) * 100
)

senior_churn.plot(
    kind="bar",
    figsize=(7, 4)
)

plt.title("SeniorCitizen vs Churn")
plt.xlabel("SeniorCitizen")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")

plt.tight_layout()
plt.show()


# =========================================================
# 6. Partner vs Churn
# =========================================================

print("\n========== PARTNER VS CHURN ==========")

partner_churn = pd.crosstab(
    df["Partner"],
    df["Churn"]
)

print(partner_churn)

print("\nPartner Churn Rate:")
print(
    pd.crosstab(
        df["Partner"],
        df["Churn"],
        normalize="index"
    ) * 100
)

partner_churn.plot(
    kind="bar",
    figsize=(7, 4)
)

plt.title("Partner vs Churn")
plt.xlabel("Partner")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")

plt.tight_layout()
plt.show()


# =========================================================
# 7. Dependents vs Churn
# =========================================================

print("\n========== DEPENDENTS VS CHURN ==========")

dependents_churn = pd.crosstab(
    df["Dependents"],
    df["Churn"]
)

print(dependents_churn)

print("\nDependents Churn Rate:")
print(
    pd.crosstab(
        df["Dependents"],
        df["Churn"],
        normalize="index"
    ) * 100
)

dependents_churn.plot(
    kind="bar",
    figsize=(7, 4)
)

plt.title("Dependents vs Churn")
plt.xlabel("Dependents")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")

plt.tight_layout()
plt.show()


# =========================================================
# 8. Tenure vs Churn
# =========================================================

print("\n========== TENURE VS CHURN ==========")

print(
    df.groupby("Churn")["tenure"].describe()
)

tenure_churn = df.groupby("Churn")["tenure"].mean()

print("\nAverage Tenure by Churn:")
print(tenure_churn)

plt.figure(figsize=(7, 4))

df.boxplot(
    column="tenure",
    by="Churn"
)

plt.title("Tenure vs Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Tenure (Months)")

plt.tight_layout()
plt.show()


# =========================================================
# 9. Contract vs Churn
# =========================================================

print("\n========== CONTRACT VS CHURN ==========")

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

print(contract_churn)

print("\nContract Churn Rate:")
print(
    pd.crosstab(
        df["Contract"],
        df["Churn"],
        normalize="index"
    ) * 100
)

contract_churn.plot(
    kind="bar",
    figsize=(8, 4)
)

plt.title("Contract vs Churn")
plt.xlabel("Contract")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")

plt.tight_layout()
plt.show()


# =========================================================
# 10. Write Findings
# =========================================================

print("\n========== FINDINGS ==========")

print("""
1. Churn distribution shows how many customers stayed
   and how many customers left.

2. Gender comparison shows whether churn differs between
   male and female customers.

3. SeniorCitizen comparison shows whether senior customers
   have a different churn pattern.

4. Partner comparison shows whether customers with or
   without a partner have different churn rates.

5. Dependents comparison shows whether having dependents
   is associated with different churn behavior.

6. Tenure comparison shows whether newer or longer-term
   customers are more likely to churn.

7. Contract comparison shows whether contract type is
   associated with customer churn.
""")


# =========================================================
# DAY 6 — EDA II: Charges, Payment, and Services
# =========================================================

SERVICE_COLUMNS = [
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
]

CATEGORICAL_COLUMNS = [
    "PaymentMethod",
    "InternetService",
    "TechSupport",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "StreamingTV",
    "StreamingMovies",
    "MultipleLines",
    "PhoneService",
    "PaperlessBilling",
]


def churn_summary(data, column):
    """Return customer counts and churn rates for each value of a column."""
    summary = data.groupby(column, dropna=False).agg(
        customers=("Churn", "size"),
        churned=("Churn", lambda values: values.eq("Yes").sum()),
    )
    summary["churn_rate_pct"] = summary["churned"] / summary["customers"] * 100
    return summary.sort_values("churn_rate_pct", ascending=False)


def run_day6_eda_ii(data):
    required_columns = {
        "customerID",
        "MonthlyCharges",
        "TotalCharges",
        "Churn",
        "tenure",
        *SERVICE_COLUMNS,
        *CATEGORICAL_COLUMNS,
    }
    missing_columns = sorted(required_columns.difference(data.columns))
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    print("\n========== DAY 6: DATASET VERIFICATION ==========")
    print(f"Shape: {data.shape}")
    print(f"Duplicate rows: {data.duplicated().sum()}")
    print(f"Duplicate customer IDs: {data['customerID'].duplicated().sum()}")
    print("Missing values by column:")
    print(data.isna().sum().to_string())
    print("\nChurn counts:")
    print(data["Churn"].value_counts().to_string())
    print("\nChurn percentages:")
    print((data["Churn"].value_counts(normalize=True) * 100).round(2).to_string())

    print("\n========== CHARGES BY CHURN ==========")
    for column in ("MonthlyCharges", "TotalCharges"):
        print(f"\n{column}:")
        print(
            data.groupby("Churn").agg(
                customers=(column, "count"),
                mean=(column, "mean"),
                median=(column, "median"),
                q1=(column, lambda values: values.quantile(0.25)),
                q3=(column, lambda values: values.quantile(0.75)),
            )
            .round(2)
            .to_string()
        )

    print("\n========== CATEGORICAL FEATURES VS CHURN ==========")
    for column in CATEGORICAL_COLUMNS:
        print(f"\n{column}:")
        print(churn_summary(data, column).round(2).to_string())

    # Count the six selected add-on/streaming services. "No internet service"
    # is not counted as a service.
    data["ServiceCount"] = data[SERVICE_COLUMNS].eq("Yes").sum(axis=1)
    print("\nServiceCount (number of selected services marked Yes) vs churn:")
    print(churn_summary(data, "ServiceCount").round(2).to_string())

    chart_dir = Path(__file__).resolve().parent
    charges_chart = chart_dir / "Day6_EDA_II_Charts.png"
    services_chart = chart_dir / "Day6_EDA_II_Service_Churn_Rates.png"

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, column in zip(axes, ("MonthlyCharges", "TotalCharges")):
        data.boxplot(column=column, by="Churn", ax=ax, showfliers=False, grid=False)
        ax.set_title(f"{column} by churn")
        ax.set_xlabel("Churn")
        ax.set_ylabel("Amount")
    fig.suptitle("Customer charges by churn status (outliers hidden)")
    fig.tight_layout()
    fig.savefig(charges_chart, dpi=160, bbox_inches="tight")
    plt.close(fig)

    fig, axes = plt.subplots(4, 3, figsize=(16, 17))
    for ax, column in zip(axes.flat, CATEGORICAL_COLUMNS):
        rates = data.groupby(column)["Churn"].apply(
            lambda values: values.eq("Yes").mean() * 100
        )
        rates.sort_values().plot(kind="bar", ax=ax, color="#3977a8")
        ax.set_title(column)
        ax.set_xlabel("")
        ax.set_ylabel("Churn rate (%)")
        ax.set_ylim(0, 50)
        ax.tick_params(axis="x", labelrotation=35, labelsize=8)
    axes.flat[-1].axis("off")
    fig.suptitle("Churn rate by payment, internet, and service segment", y=1.01)
    fig.tight_layout()
    fig.savefig(services_chart, dpi=160, bbox_inches="tight")
    plt.close(fig)

    print(f"\nCharts saved to:\n- {charges_chart.name}\n- {services_chart.name}")


run_day6_eda_ii(df)
