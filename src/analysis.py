from load_data import load_production_data
from metrics import calculate_metrics

def main():
    df = load_production_data("data/production_data.csv")
    df_metrics = calculate_metrics(df)

    summary = (
        df_metrics
        .groupby("operator_id")
        .agg(
            avg_efficiency=("efficiency_pct", "mean"),
            avg_downtime_pct=("downtime_pct", "mean"),
            total_units=("produced_units", "sum")
        )
        .reset_index()
    )

    print(summary)

if __name__ == "__main__":
    main()
