import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(filepath):
    """Load and preprocess the eCommerce transactions data"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    if os.stat(filepath).st_size == 0:
        raise ValueError(f"The file {filepath} is empty.")
    
    df = pd.read_csv(filepath)
    
    # Handle missing values
    df = df.dropna()
    
    # Convert date columns to datetime
    date_columns = df.select_dtypes(include=['object']).columns
    for col in date_columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col])
    
    # Check for required columns
    required_columns = ['TransactionDate', 'CustomerID']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"The required column '{col}' is missing from the data.")
            
    return df

def create_features(df):
    """Create relevant features for analysis"""
    # Time-based features
    df['hour'] = df['TransactionDate'].dt.hour
    df['day_of_week'] = df['TransactionDate'].dt.dayofweek
    df['month'] = df['TransactionDate'].dt.month
    
    # Customer behavior features
    df['total_items'] = df.groupby('CustomerID')['Quantity'].transform('sum')
    df['avg_order_value'] = df.groupby('CustomerID')['TotalValue'].transform('mean')
    
    return df

def scale_features(df, features_to_scale):
    """Scale numerical features"""
    scaler = StandardScaler()
    df[features_to_scale] = scaler.fit_transform(df[features_to_scale])
    return df
