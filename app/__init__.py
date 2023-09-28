from flask import Flask
import pandas as pd

app = Flask(__name__, template_folder='../template')

# Initialize the dataset
dataset = None

def initialize_dataset():
    global dataset
    try:
        dataset = pd.read_csv('dataset.csv')
    except FileNotFoundError:
        print("Error: 'dataset.csv' not found.")
    except pd.errors.EmptyDataError:
        print("Error: 'dataset.csv' is empty.")

# Initialize the dataset
initialize_dataset()

# Import the routes module
from app import routes
