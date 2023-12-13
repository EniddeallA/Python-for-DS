import pandas as pd


def load(path: str) -> pd.DataFrame:
    if path == "" or path is None or type(path) is not str:
        exit(f"File {path} is Invalid")
    check_path = path.lower().split(".")
    if (check_path[-1] != "csv" or len(check_path) == 1):
        exit(f"File {path} is not a valid csv file")
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
        return df
    except FileNotFoundError:
        exit(f"File {path} not found")
    except Exception as e:
        exit(f"Error while loading file {path}: {e}")
