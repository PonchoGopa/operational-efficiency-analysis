import pandas as pd

def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["effective_time_min"] = df["total_time_min"] - df["downtime_min"]
    df["expected_units"] = df["effective_time_min"] * df["spm"]
    df["efficiency_pct"] = (df["produced_units"] / df["expected_units"]) * 100
    df["downtime_pct"] = (df["downtime_min"] / df["total_time_min"]) * 100

    return df
