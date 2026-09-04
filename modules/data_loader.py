import pandas as pd
import os

def load_data(file_path="data/rcb_t20_stats.csv"):
    if not os.path.exists(file_path):
        print(f"[ERROR] Data file not found at {file_path}")
        return None
    
    try:
        df = pd.read_csv(file_path)
        print("\n[SUCCESS] Data loaded successfully!")
        print("-" * 45)
        print(df.head())
        print("-" * 45)
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return None