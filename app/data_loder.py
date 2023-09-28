# app/data_loader.py
import pandas as pd

# Initialize empty DataFrames for the datasets
dataset = None

# Load the main dataset if it exists and has data
try:
    dataset = pd.read_csv('dataset.csv')
except FileNotFoundError:
    print("Error: 'dataset.csv' not found.")
except pd.errors.EmptyDataError:
    print("Error: 'dataset.csv' is empty.")
