import unittest
import pandas as pd
from src.anomaly_detector import detect_anomalies

class TestAnomalyDetector(unittest.TestCase):
    def setUp(self):
        data = {'col1': [1, 2, None, 4], 'col2': [1, 2, 100, 4]}
        self.df = pd.DataFrame(data)

    def test_detect_anomalies(self):
        anomalies = detect_anomalies(self.df)
        self.assertIn('missing_values', anomalies)
        self.assertIn('outliers', anomalies)

if __name__ == '__main__':
    unittest.main()
