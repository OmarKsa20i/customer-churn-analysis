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



# =========================================================
# DAY 7 — Relationship Analysis
# =========================================================

CONTRACT_ORDER = ["Month-to-month", "One year", "Two year"]
TENURE_GROUP_ORDER = [
    "New (0-12)",
    "Early (13-24)",
    "Established (25-48)",
    "Loyal (49-72)",
]
PAYMENT_ORDER = [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)",
]


def run_day7_relationship_analysis(data):
    data["TenureGroup"] = pd.cut(
        data["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=TENURE_GROUP_ORDER,
        include_lowest=True,
    )

    contract_tenure = data.groupby(
        ["Contract", "TenureGroup"], observed=True
    ).agg(
        customers=("Churn", "size"),
        churned=("Churn", lambda values: values.eq("Yes").sum()),
    )
    contract_tenure["churn_rate_pct"] = (
        contract_tenure["churned"] / contract_tenure["customers"] * 100
    )
    contract_tenure = contract_tenure.reindex(
        pd.MultiIndex.from_product(
            [CONTRACT_ORDER, TENURE_GROUP_ORDER],
            names=["Contract", "TenureGroup"],
        )
    )

    charges = data.groupby(["Contract", "Churn"], observed=True).agg(
        customers=("MonthlyCharges", "count"),
        mean=("MonthlyCharges", "mean"),
        median=("MonthlyCharges", "median"),
    )
    charges = charges.reindex(
        pd.MultiIndex.from_product(
            [CONTRACT_ORDER, ["No", "Yes"]], names=["Contract", "Churn"]
        )
    )

    service_count = data.groupby("ServiceCount").agg(
        customers=("Churn", "size"),
        churned=("Churn", lambda values: values.eq("Yes").sum()),
    )
    service_count["churn_rate_pct"] = (
        service_count["churned"] / service_count["customers"] * 100
    )

    payment_contract = data.groupby(
        ["PaymentMethod", "Contract"], observed=True
    ).agg(
        customers=("Churn", "size"),
        churned=("Churn", lambda values: values.eq("Yes").sum()),
    )
    payment_contract["churn_rate_pct"] = (
        payment_contract["churned"] / payment_contract["customers"] * 100
    )
    payment_contract = payment_contract.reindex(
        pd.MultiIndex.from_product(
            [PAYMENT_ORDER, CONTRACT_ORDER],
            names=["PaymentMethod", "Contract"],
        )
    )

    print("\n========== DAY 7: CONTRACT + TENURE GROUP ==========")
    print(contract_tenure.round(2).to_string())
    print("\n========== MONTHLY CHARGES + CONTRACT + CHURN ==========")
    print(charges.round(2).to_string())
    print("\n========== SERVICE COUNT + CHURN ==========")
    print(service_count.round(2).to_string())
    print("\n========== PAYMENT METHOD + CONTRACT + CHURN ==========")
    print(payment_contract.round(2).to_string())

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    contract_rates = contract_tenure["churn_rate_pct"].unstack("TenureGroup")
    contract_rates = contract_rates.reindex(
        index=CONTRACT_ORDER, columns=TENURE_GROUP_ORDER
    )
    image = axes[0, 0].imshow(contract_rates, cmap="YlOrRd", vmin=0, vmax=60, aspect="auto")
    axes[0, 0].set_title("Churn rate by contract and tenure group")
    axes[0, 0].set_xticks(range(len(TENURE_GROUP_ORDER)), TENURE_GROUP_ORDER, rotation=25, ha="right")
    axes[0, 0].set_yticks(range(len(CONTRACT_ORDER)), CONTRACT_ORDER)
    for row in range(contract_rates.shape[0]):
        for col in range(contract_rates.shape[1]):
            axes[0, 0].text(col, row, f"{contract_rates.iloc[row, col]:.1f}%", ha="center", va="center")
    fig.colorbar(image, ax=axes[0, 0], label="Churn rate (%)")

    charge_means = charges["mean"].unstack("Churn").reindex(
        index=CONTRACT_ORDER, columns=["No", "Yes"]
    )
    charge_means.columns = ["Stayed", "Churned"]
    charge_means.plot(kind="bar", ax=axes[0, 1], color=["#3977a8", "#d47748"])
    axes[0, 1].set_title("Average monthly charges by contract and churn")
    axes[0, 1].set_xlabel("")
    axes[0, 1].set_ylabel("Monthly charges")
    axes[0, 1].tick_params(axis="x", rotation=0)
    axes[0, 1].legend(title="Customer status")

    axes[1, 0].plot(
        service_count.index,
        service_count["churn_rate_pct"],
        marker="o",
        color="#3977a8",
    )
    axes[1, 0].set_title("Churn rate by number of selected services")
    axes[1, 0].set_xlabel("Service count (0–6)")
    axes[1, 0].set_ylabel("Churn rate (%)")
    axes[1, 0].set_xticks(service_count.index)
    axes[1, 0].set_ylim(0, 55)
    axes[1, 0].grid(axis="y", alpha=0.25)

    payment_rates = payment_contract["churn_rate_pct"].unstack("Contract")
    payment_rates = payment_rates.reindex(index=PAYMENT_ORDER, columns=CONTRACT_ORDER)
    image = axes[1, 1].imshow(payment_rates, cmap="YlOrRd", vmin=0, vmax=60, aspect="auto")
    axes[1, 1].set_title("Churn rate by payment method and contract")
    axes[1, 1].set_xticks(range(len(CONTRACT_ORDER)), CONTRACT_ORDER, rotation=20, ha="right")
    axes[1, 1].set_yticks(range(len(PAYMENT_ORDER)), PAYMENT_ORDER)
    for row in range(payment_rates.shape[0]):
        for col in range(payment_rates.shape[1]):
            axes[1, 1].text(col, row, f"{payment_rates.iloc[row, col]:.1f}%", ha="center", va="center")
    fig.colorbar(image, ax=axes[1, 1], label="Churn rate (%)")

    fig.suptitle("Day 7 — Combined churn relationships")
    fig.tight_layout()
    chart_path = Path(__file__).resolve().parent / "Day7_Relationship_Analysis.png"
    fig.savefig(chart_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"\nRelationship chart saved to: {chart_path.name}")


run_day6_eda_ii(df)
run_day7_relationship_analysis(df)


# =========================================================
# DAY 8 — Statistical Analysis
# =========================================================

def holm_adjust(p_values):
    """Apply Holm's step-down adjustment and return values in input order."""
    order = sorted(range(len(p_values)), key=lambda index: p_values[index])
    adjusted = [0.0] * len(p_values)
    running_max = 0.0
    total = len(p_values)
    for rank, index in enumerate(order):
        candidate = min(1.0, (total - rank) * p_values[index])
        running_max = max(running_max, candidate)
        adjusted[index] = running_max
    return adjusted


def run_day8_statistical_analysis(data):
    try:
        from scipy.stats import chi2_contingency, ttest_ind
    except ImportError as error:
        raise ImportError(
            "Day 8 statistical analysis requires SciPy. "
            "Install the project packages with: pip install -r requirements.txt"
        ) from error

    tests = []
    print("\n========== DAY 8: STATISTICAL TESTS ==========")
    print("Categorical features: Pearson chi-square test of independence")
    for column in ("Contract", "PaymentMethod"):
        table = pd.crosstab(data[column], data["Churn"]).reindex(
            columns=["No", "Yes"], fill_value=0
        )
        chi2, p_value, degrees_freedom, expected = chi2_contingency(
            table, correction=False
        )
        sample_size = int(table.to_numpy().sum())
        cramer_v = (chi2 / (sample_size * min(table.shape[0] - 1, table.shape[1] - 1))) ** 0.5
        tests.append(
            {
                "name": f"{column} vs Churn",
                "p_value": float(p_value),
                "statistic": float(chi2),
                "degrees_freedom": int(degrees_freedom),
                "effect": f"Cramer's V = {cramer_v:.3f}",
            }
        )
        print(f"\n{column} x Churn contingency table:")
        print(table.to_string())
        print(
            f"Chi-square({degrees_freedom}) = {chi2:.2f}; "
            f"p = {p_value:.3e}; N = {sample_size}; "
            f"Cramer's V = {cramer_v:.3f}; "
            f"minimum expected cell = {expected.min():.1f}"
        )

    stayed = data.loc[data["Churn"].eq("No"), "MonthlyCharges"].astype(float)
    churned = data.loc[data["Churn"].eq("Yes"), "MonthlyCharges"].astype(float)
    welch = ttest_ind(churned, stayed, equal_var=False, nan_policy="omit")
    variance_churned = churned.var(ddof=1)
    variance_stayed = stayed.var(ddof=1)
    term_churned = variance_churned / churned.count()
    term_stayed = variance_stayed / stayed.count()
    welch_df = (term_churned + term_stayed) ** 2 / (
        term_churned**2 / (churned.count() - 1)
        + term_stayed**2 / (stayed.count() - 1)
    )
    mean_difference = churned.mean() - stayed.mean()
    tests.append(
        {
            "name": "MonthlyCharges: churned vs stayed (Welch t-test)",
            "p_value": float(welch.pvalue),
            "statistic": float(welch.statistic),
            "degrees_freedom": float(welch_df),
            "effect": f"mean difference = ${mean_difference:.2f}",
        }
    )
    print("\nMonthlyCharges by Churn:")
    print(
        f"Stayed: n={stayed.count()}, mean=${stayed.mean():.2f}; "
        f"Churned: n={churned.count()}, mean=${churned.mean():.2f}"
    )
    print(
        f"Welch t({welch_df:.1f}) = {welch.statistic:.2f}; "
        f"p = {welch.pvalue:.3e}; mean difference (churned - stayed) "
        f"= ${mean_difference:.2f}"
    )

    adjusted = holm_adjust([test["p_value"] for test in tests])
    print("\nHolm-adjusted results (family-wise alpha = 0.05):")
    for test, adjusted_p in zip(tests, adjusted):
        test["adjusted_p_value"] = adjusted_p
        print(
            f"{test['name']}: raw p={test['p_value']:.3e}; "
            f"adjusted p={adjusted_p:.3e}; {test['effect']}"
        )

    print(
        "\nInterpretation: all three selected comparisons remain statistically "
        "significant after Holm adjustment. These tests show associations or "
        "mean differences in this dataset; they do not establish causation."
    )


run_day8_statistical_analysis(df)
