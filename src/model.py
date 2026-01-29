"""
model.py
Simple modeling utilities for therapy response prediction demo.
"""
from sklearn.linear_model import LogisticRegression
import pandas as pd

def train_logistic_regression(X: pd.DataFrame, y: pd.Series) -> LogisticRegression:
    """
    Trains a Logistic Regression model for binary therapy response prediction.
    Args:
        X (pd.DataFrame): Feature matrix
        y (pd.Series): Binary target vector
    Returns:
        LogisticRegression: Trained model
    """
    model = LogisticRegression()
    model.fit(X, y)
    return model

def get_feature_coefficients(model: LogisticRegression, feature_names: list) -> pd.Series:
    """
    Extracts feature coefficients from a trained Logistic Regression model.
    Args:
        model (LogisticRegression): Trained model
        feature_names (list): List of feature names
    Returns:
        pd.Series: Feature coefficients indexed by feature name
    """
    return pd.Series(model.coef_[0], index=feature_names)
