from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Example data for training the model
X = np.array([
    [1500, 2, 'location1'],
    [1800, 3, 'location2'],
    [1200, 2, 'location1'],
    [2200, 4, 'location3'],
    [1700, 3, 'location2']
])
y = [250000, 320000, 190000, 410000, 295000]

# Encode the 'location' column using LabelEncoder
location_encoder = LabelEncoder()
locations_encoded = location_encoder.fit_transform(X[:, 2])

# Replace the 'location' column in X with the encoded values
X[:, 2] = locations_encoded

# Convert the data type of X to float
X = X.astype(float)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

def predict_price(square_feet, num_bedrooms, location):
    # Encode the location input using the trained encoder
    location_encoded = location_encoder.transform([location])

    # Create a numpy array with the input features
    input_features = np.array([[square_feet, num_bedrooms, location_encoded[0]]])

    # Make a prediction using the trained model
    predicted_price = model.predict(input_features)

    # Return the predicted price as a float
    return float(predicted_price[0])
