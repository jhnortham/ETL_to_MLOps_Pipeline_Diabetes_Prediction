"""
Testing the Flask Application

"""

# Import packages

import requests

url = "http://127.0.0.1:5000/predict"

patient = {
    "Glucose": 148,
    "Age": 50,
    "BMI": 33.6
}

response = requests.post(url, json=patient)

print("Status Code:", response.status_code)
print("Prediction:", response.json())