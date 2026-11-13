import json
import pandas as pd


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def build_table(data):
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    else:
        df = pd.DataFrame(data)
    return df
