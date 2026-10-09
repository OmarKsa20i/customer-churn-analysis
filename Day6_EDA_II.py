from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path(__file__).resolve().parent / "Telco-Customer-Churn.csv"
CHART_PATH = Path(__file__).resolve().parent / "Day6_EDA_II_Charts.png"

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


def churn_summary(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """Return customer counts and churn rates for each value of a column."""
    summary = data.groupby(column, dropna=False).agg(
        customers=("Churn", "size"),
        churned=("Churn", lambda values: values.eq("Yes").sum()),
    )
    summary["churn_rate_pct"] = summary["churned"] / summary["customers"] * 100
    return summary.sort_values("churn_rate_pct", ascending=False)


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    required_columns = {
        "customerID",
        "MonthlyCharges",
        "TotalCharges",
        "Churn",
        "tenure",
        *SERVICE_COLUMNS,
        *CATEGORICAL_COLUMNS,
    }
    missing_columns = sorted(required_columns.difference(df.columns))
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    print("========== DATASET VERIFICATION ==========")
    print(f"Shape: {df.shape}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print(f"Duplicate customer IDs: {df['customerID'].duplicated().sum()}")
    print("Missing values by column:")
    print(df.isna().sum().to_string())
    print("\nChurn counts:")
    print(df["Churn"].value_counts().to_string())
    print("\nChurn percentages:")
    print((df["Churn"].value_counts(normalize=True) * 100).round(2).to_string())

    print("\n========== CHARGES BY CHURN ==========")
    for column in ("MonthlyCharges", "TotalCharges"):
        print(f"\n{column}:")
        print(
            df.groupby("Churn").agg(
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
        print(churn_summary(df, column).round(2).to_string())

    # Count the six selected add-on/streaming services for a compact service
    # breadth comparison. "No internet service" is not counted as a service.
    df["ServiceCount"] = df[SERVICE_COLUMNS].eq("Yes").sum(axis=1)
    print("\nServiceCount (number of selected services marked Yes) vs churn:")
    print(churn_summary(df, "ServiceCount").round(2).to_string())

    # Save a compact chart set so the analysis can be reviewed without rerunning
    # the whole project interactively.
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, column in zip(axes, ("MonthlyCharges", "TotalCharges")):
        df.boxplot(column=column, by="Churn", ax=ax, showfliers=False, grid=False)
        ax.set_title(f"{column} by churn")
        ax.set_xlabel("Churn")
        ax.set_ylabel("Amount")
    fig.suptitle("Customer charges by churn status (outliers hidden)")
    fig.tight_layout()
    fig.savefig(CHART_PATH, dpi=160, bbox_inches="tight")
    plt.close(fig)

    fig, axes = plt.subplots(4, 3, figsize=(16, 17))
    for ax, column in zip(axes.flat, CATEGORICAL_COLUMNS):
        rates = (df.groupby(column)["Churn"].apply(lambda values: values.eq("Yes").mean() * 100))
        rates.sort_values().plot(kind="bar", ax=ax, color="#3977a8")
        ax.set_title(column)
        ax.set_xlabel("")
        ax.set_ylabel("Churn rate (%)")
        ax.set_ylim(0, 50)
        ax.tick_params(axis="x", labelrotation=35, labelsize=8)
    axes.flat[-1].axis("off")
    fig.suptitle("Churn rate by payment, internet, and service segment", y=1.01)
    fig.tight_layout()
    fig.savefig(CHART_PATH.with_name("Day6_EDA_II_Service_Churn_Rates.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)

    print(f"\nCharts saved to:\n- {CHART_PATH.name}\n- Day6_EDA_II_Service_Churn_Rates.png")


if __name__ == "__main__":
    main()
