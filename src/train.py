"""
Model Training Pipeline

-Reads cleaned data from SQLite
-Selects predictor variables
-Splits the data into training and test sets
-trains a logistic regression model
-evaluates model performance
-saves trained model

"""

# Data

import pandas as pd

# Database

from sqlalchemy import create_engine

# Machine Learning

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Model Evaluation

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)

# Save trained model

import joblib

# Create SQLite database connection

engine = create_engine("sqlite:///data/diabetes_mlops.db")

# Load cleaned database from SQLite

diabetes = pd.read_sql("diabetes", con=engine)

# Inspect the database

print(diabetes.head())
print(diabetes.info())
print(diabetes.describe())

# Explore relationships with correlation matrix

correlation_matrix = diabetes.corr(numeric_only=True)

print(correlation_matrix)

# Choose variables: Glucose, Age, and BMI are chosen as most important variables

X = diabetes[["Glucose", "Age", "BMI"]]
y = diabetes["Outcome"]

# Split dataset into train and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=123)

# Create the model

model = LogisticRegression(random_state=123)

# Train the model

model.fit(X_train, y_train)

# Predict diabetes outcomes

y_pred = model.predict(X_test)

# Show metrics

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Save trained model

joblib.dump(model, "models/diabetes_model.pkl")


