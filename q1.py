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
