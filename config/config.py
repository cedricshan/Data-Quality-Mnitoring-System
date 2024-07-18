import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/sample_data.csv')
LOG_PATH = os.path.join(os.path.dirname(__file__), '../logs/data_quality.log')
THRESHOLDS = {
    'missing_values': 0.05,
    'outliers': 0.01
}
ALERT_EMAIL = 'ys328@duke.edu'
