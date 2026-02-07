import pandas as pd

def load_production_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])

    required_columns = {
        "date", "operator_id", "shift",
        "total_time_min", "downtime_min",
        "spm", "produced_units"
    }

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df
