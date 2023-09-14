from flask import render_template, request, jsonify
from app import app
from app.ml_model import predict_price

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_price = ''
    square_feet = ''
    num_bedrooms = ''
    location = ''

    if request.method == 'POST':
        square_feet = float(request.form['square_feet'])
        num_bedrooms = int(request.form['num_bedrooms'])
        location = request.form['location']

        predicted_price = predict_price(square_feet, num_bedrooms, location)

    return render_template('index.html', predicted_price=predicted_price, square_feet=square_feet, num_bedrooms=num_bedrooms, location=location)
