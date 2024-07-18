import pandas as pd
import numpy as np
from scipy.stats import zscore

def check_missing_values(df: pd.DataFrame, threshold: float):

############################################################################################################
    # print("############################################")
    # print("threshold")
    # print(threshold)
    # print("############################################")
############################################################################################################

    missing_ratio = df.isnull().mean()
    return missing_ratio[missing_ratio > threshold]

def check_outliers(df: pd.DataFrame, threshold: float) -> pd.DataFrame:

############################################################################################################
    # print("############################################")
    # print("threshold")
    # print(threshold)
    # print("############################################")
############################################################################################################


############################################################################################################
    # print("############################################")
    # print("df")
    # print(df)
    # print(df.size)
    # print("############################################")
############################################################################################################


    # Select only numeric columns for zscore calculation
    numeric_df = df.select_dtypes(include=[np.number])

############################################################################################################
    # print("############################################")
    # print("numeric_df")
    # print(numeric_df)
    # print("############################################")
############################################################################################################

    # Apply zscore to numeric columns
    z_scores = numeric_df.apply(lambda col: zscore(col, nan_policy='omit'))

############################################################################################################
    # print("############################################")
    # print(z_scores)
    # print("############################################")
############################################################################################################
  

    # Identify outliers based on the threshold
    # Here, we consider a value as an outlier if its z-score is above 3 or below -3
    outliers_mask = (z_scores.abs() > threshold)
    
    # Filter the original DataFrame based on the outliers_mask
    # We use any(axis=1) to select rows where at least one column satisfies the condition

############################################################################################################
    # print("############################################")
    # print(outliers_mask)
    # print("############################################")
############################################################################################################
    outliers_df = df[outliers_mask.any(axis=1)]
    
    # Return the DataFrame containing outliers
    # If no outliers are detected, this will return an empty DataFrame
    return outliers_df
