import pandas as pd

def load_production_data(path: str) -> pd.DataFrame:
    # Try to read as Excel first (in case it's an Excel file with .csv extension)
    try:
        df = pd.read_excel(path, parse_dates=["date"])
    except (ImportError, Exception):
        # If Excel reading fails, try different encodings for CSV
        encodings = ['utf-8', 'latin1', 'cp1252', 'iso-8859-1']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(path, encoding=encoding, parse_dates=["date"])
                break
            except UnicodeDecodeError:
                continue
            except Exception as e:
                if "parse_dates" in str(e):
                    # If parse_dates fails, try without it first
                    try:
                        df = pd.read_csv(path, encoding=encoding)
                        # Try to convert date column after reading
                        if 'date' in df.columns:
                            df['date'] = pd.to_datetime(df['date'])
                        break
                    except:
                        continue
                else:
                    continue
        
        if df is None:
            raise ValueError(f"Could not read file {path} with any supported encoding")

    required_columns = {
        "date", "operator_id", "shift",
        "total_time_min", "downtime_min",
        "spm", "produced_units"
    }

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df
