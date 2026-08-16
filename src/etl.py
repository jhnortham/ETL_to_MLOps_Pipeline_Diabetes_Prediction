"""
ETL Pipeline

Extracts data from a CSV file:
	- Pima Indians Diabetes CSV
	- CDC Diabetes API

Transforms/Processes data:
	-Removes metadata
	-Converts data types
	-Cleans data

Load:
	-Save processed CSVs
	-Load into SQLite
"""

# Import required libraries

import pandas as pd
import requests
from sqlalchemy import create_engine

# Create SQLite database connection

engine = create_engine("sqlite:///data/diabetes_mlops.db")

# Extract: Read the Pima Indians Diabetes Database
diabetes = pd.read_csv("data/raw/diabetes.csv")

# Extract: Request CDC diabetes data from the public API
response = requests.get("https://data.cdc.gov/api/v3/views/b559-sbez/query.json?accessType=DOWNLOAD")

# Inspect the data
print(diabetes.head())
print(response.status_code)

# Convert API JSON response into pandas DataFrame
api_data = response.json()
cdc_diabetes = pd.DataFrame(api_data)

print(cdc_diabetes.columns)

print(cdc_diabetes.head())

print(cdc_diabetes.info())

print(type(api_data))
print(type(api_data[0]))
print(api_data[0])

# Drop metadata columns and inspect
cdc_diabetes = cdc_diabetes.drop(columns=[':id', ':version', ':created_at', ':updated_at', 'estimatefootnote'])

print(cdc_diabetes.info())

print(diabetes.isnull().sum())
print(cdc_diabetes.isnull().sum())

# Change string data types to numeric data types using for loop
numeric_columns = [
    "year",
    "estimate",
    "lowerlimit",
    "upperlimit",
    "seestimate"
]

for column in numeric_columns:
    cdc_diabetes[column] = pd.to_numeric(
        cdc_diabetes[column],
        errors="coerce"
    )

print(cdc_diabetes.columns)

# Drop NA rows and standard error column
cdc_diabetes = cdc_diabetes.dropna(subset=["estimate"])
cdc_diabetes = cdc_diabetes.drop(columns=["seestimate"])


# Inspect cleaned data frames
print(cdc_diabetes.isna().sum())
print(cdc_diabetes.shape)
print(cdc_diabetes.info())

# Store cleaned databases in processed folder for future use
diabetes.to_csv(
    "data/processed/diabetes_clean.csv",
    index=False
)

cdc_diabetes.to_csv(
    "data/processed/cdc_diabetes_clean.csv",
    index=False
)

# Load cleaned databases to SQLite database
diabetes.to_sql(
    "diabetes",
    con=engine,
    if_exists="replace",
    index=False
)

cdc_diabetes.to_sql(
    "cdc_diabetes",
    con=engine,
    if_exists="replace",
    index=False
)

# Print statement to confirm loading
print("Data successfully loaded into SQLite.")