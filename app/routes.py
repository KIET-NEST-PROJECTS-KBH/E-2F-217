from flask import render_template, request
from app import app
from app.ml_model import predict_price

# ... Other imports and initialization code ...

@app.route('/', methods=['GET', 'POST'])
def index():
    global location_adjustments

    predicted_price = ''
    square_feet = ''
    num_bedrooms = ''
    location = ''

    if request.method == 'POST':
        square_feet = float(request.form['square_feet'])
        num_bedrooms = int(request.form['num_bedrooms'])
        location = request.form['location']

        # Predict the base price using the machine learning model
        base_price = predict_price(square_feet, num_bedrooms)

        # Include the location in the result
        # You can directly use the 'location' variable here

        # Assign the adjusted_price to predicted_price
        predicted_price = f"₹{base_price:.2f}"

    return render_template(
        'index.html',
        predicted_price=predicted_price,
        square_feet=square_feet,
        num_bedrooms=num_bedrooms,
        location=location  # Pass the location to the template
    )
