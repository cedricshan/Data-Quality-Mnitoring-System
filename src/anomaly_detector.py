from config.config import THRESHOLDS
from .data_validator import check_missing_values, check_outliers

def detect_anomalies(df):
    anomalies = {}
    missing_values = check_missing_values(df, THRESHOLDS['missing_values'])
    if not missing_values.empty:
        anomalies['missing_values'] = missing_values

    outliers = check_outliers(df, THRESHOLDS['outliers'])
    if not outliers.empty:
        anomalies['outliers'] = outliers

    return anomalies
