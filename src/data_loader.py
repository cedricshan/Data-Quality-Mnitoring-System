import pandas as pd
from config.config import DATA_PATH

def load_data():
    return pd.read_csv(DATA_PATH)
