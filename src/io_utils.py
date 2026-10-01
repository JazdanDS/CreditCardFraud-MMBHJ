"""
Input/Output utility functions for reading and writing data in project.

"""

from pathlib import Path
import pandas as pd

def load_csv_to_dataframe(file_path: str | Path) -> pd.DataFrame:

    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found at: {path}")
    
    try:
        df = pd.read_csv(path)

        if df.empty:
            raise ValueError(f"CSV File Empty: {path}")

        return df

    except pd.errors.EmptyDataError:
        raise ValueError(f"File does not contain CSV Data: {path}")