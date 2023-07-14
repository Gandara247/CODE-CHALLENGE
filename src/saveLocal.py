from datetime import datetime
from pathlib import Path


def write_json(df, source, table_name):
    today = datetime.today().strftime("%Y-%m-%d")

    filepaths = f"local_data/{source}/{today}"
    Path(filepaths).mkdir(parents=True, exist_ok=True)

    filename = f"{table_name}.json"
    df.to_json(f"{filepaths}/{filename}")
