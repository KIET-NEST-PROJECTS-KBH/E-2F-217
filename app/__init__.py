from flask import Flask

# Initialize the Flask app
app = Flask(__name__, template_folder='../template')

# Import the routes module
from app import routes
