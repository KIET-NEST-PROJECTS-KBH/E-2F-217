from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Load the main dataset
dataset = pd.read_csv('dataset.csv')

# Example data for training the model
X = dataset[['SquareFeet', 'NumBedrooms']]
y = dataset['Price']

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

def predict_price(square_feet, num_bedrooms):
    # Create a numpy array with the input features
    input_features = np.array([[square_feet, num_bedrooms]])

    # Make a prediction using the trained model
    predicted_price = model.predict(input_features)

    # Return the predicted price as a float
    return float(predicted_price[0])
