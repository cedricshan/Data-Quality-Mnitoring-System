import unittest
import pandas as pd
from src.data_validator import check_missing_values, check_outliers

class TestDataValidator(unittest.TestCase):
    def setUp(self):
        data = {'col1': [1, 2, None, 4], 'col2': [1, None, None, 4]}
        self.df = pd.DataFrame(data)

    def test_check_missing_values(self):
        result = check_missing_values(self.df, 0.25)
        self.assertIn('col2', result.index)

    def test_check_outliers(self):
        data = {'col1': [1, 2, 100, 4], 'col2': [1, 2, 3, 4]}
        df = pd.DataFrame(data)
        result = check_outliers(df, 0.25)
        self.assertIn('col1', result.index)

if __name__ == '__main__':
    unittest.main()
