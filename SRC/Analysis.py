# src/analysis.py

import pandas as pd

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Load dataset
df = pd.read_csv('Data/raw/Hotel_bookings_final.csv')

print("\n" + "="*60)
print("DATASET SHAPE")
print("="*60)
print(df.shape)

print("\n" + "="*60)
print("COLUMN NAMES")
print("="*60)
print(df.columns.tolist())

print("\n" + "="*60)
print("DATA TYPES")
print("="*60)
print(df.dtypes)

print("\n" + "="*60)
print("MISSING VALUES")
print("="*60)
print(df.isnull().sum())

print("\n" + "="*60)
print("DUPLICATES")
print("="*60)
print(df.duplicated().sum())

print("\n" + "="*60)
print("FIRST 5 ROWS")
print("="*60)
print(df.head())