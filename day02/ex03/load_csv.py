import pandas as pd

def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df