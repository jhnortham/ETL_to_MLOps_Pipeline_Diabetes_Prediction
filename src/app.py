"""

Flask Application

-Loads the trained diabetes prediction model
-Provides a REST API for making predictions

"""

# Import required libraries
from flask import Flask, request, jsonify

import joblib

import pandas as pd


# Load trained model

model = joblib.load("models/diabetes_model.pkl")

# Create Flask application
 
app = Flask('__name__')

# Prediction Endpoint

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    glucose = data["Glucose"]
    age = data["Age"]
    bmi = data["BMI"]

    input_data = pd.DataFrame(
        [[glucose, age, bmi]],
        columns=["Glucose", "Age", "BMI"]
    )

    prediction = model.predict(input_data)

    return jsonify({
        "prediction": int(prediction[0])
    })


# Run the application

if __name__ == '__main__':app.run(debug=True)