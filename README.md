
# ETL_to_MLOps_Pipeline_Diabetes_Prediction
Complete ETL to MLOps pipeline for diabetes prediction using the Pima Indian Diabetes dataset

# Pima Diabetes MLOps Pipeline

## Overview
The purpose of this project was to create a extract-transfer-load (ETL) to machine learning operations (MLOps) pipeline for the prediction of diabetes.

## Project Structure
The project was structured into three phases for a complete ETL to MLOps pipeline completed in the Python 3.14 computer langauge. 
The first phase addressed the ETL pathway, extracting data from an open source dataset and a public health API. The pipeline demonstrates a pathway for extraction of both csv and api data, although only csv data was used for the classification model.
The data was extracted and cleaned, prior to model development. A logistic regression classification model was created using influential variables determined by a correlation matrix.
The logistic regression model was created with metrics identified. The final phase of the project included deployment in a Flask application to return a prediction based on the identified variables (Glucose, Age, and BMI).

## Technologies
The technologies included Windows PowerShell for development in the local environment using Python 3.14. Notepad files were used for storing python code, requirements text, and this README file.
Python packages required for this pipeline include use of pandas for extraction and inspection of data frames, SQLite for loading of cleaned dataframes, scikit-learn for building of the classification model.
Flask was used for application deployment.
 
## Data Sources
Two data sources were included in the pipeline to demonstrate the capability of the pipeline in acquisition of both csv files and api data. The Pima Indian Diabetes dataset, from Kaggle.com, was the source for the csv file.
The CDC State Diabetes Indicators API was the source for API data. The JSON endpoint was used for extraction, already in tabular format for loading. 

## ETL Pipeline
The ETL pipeline included the etl.py file for extraction, data cleaning, and loading of the cleaned datasets to SQLite.
Extracts data from a CSV file:
	- Pima Indians Diabetes CSV
	- CDC Diabetes API

Transformation and preprocessing was included in the etl.py file. Metadata columns were removed from the CDC Diabetes API dataframe. Additionally, the standard error column was removed.
The API dataset included over 114,000 rows, with over 25,000 rows with missing values. Because the purpose of this project was to complete an ETL to MLOps pipeline, the rows with missing values were removed.
Following removal of the rows with missing values, there were over 88,000 rows of the API data included in the data frame.
Transforms/Processes data:
	-Removes metadata
	-Converts data types
	-Cleans data

Once transformed and cleaned, the cleaned data frames were loaded to SQLite.
Load:
	-Save processed CSVs
	-Load into SQLite

## Machine Learning Pipeline
The model training was completed using the train.py file.

The cleaned data from the Pima Indian Diabetes csv was read from SQLite. Data inspection was completed with .head(), .info(), and .describe(). A correlation matrix was created for variable inspection.
The variables of Glucose, Age, and BMI were chosen for the logistic regression model, with correlations of 0.467, 0.238, and 0.293 as the highest correlations across the variables.
The data was split into 80/20 train/test sets for model training and testing. 
Outcome metrics were determined:
Accuracy: 0.779
Precision: 0.8
Recall: 0.552
F1 Score: 0.653

The model was then saved for deployment.

-Reads cleaned data from SQLite
-Selects predictor variables
-Splits the data into training and test sets
-trains a logistic regression model
-evaluates model performance
-saves trained model

## Deployment
The flask (Flask, request, jsonify), joblib and pandas were the required packages for application deployment. The saved model was loaded.
A Flask application was created with prediction endpoints created using the Glucose, Age, and BMI variables.
The application returns a prediction score based on the values of glucose, age, and BMI.
The application was tested with a test_api.py file and returned the appropriate status code (200) with a prediction score indicating the pipeline was functioning and the REST API was validated.


-Loads the trained diabetes prediction model
-Provides a REST API for making predictions

## How to Run
The following steps are required for running this project:
* create a working directory for this project
* change directory to ensure all work occurs in the project directory
* set up folder structure:
	* src: source code files: etl.py, train.py, app.py, test_api.py
	* data: raw: Pima Indian Diabetes database
		processed: cleaned data frames
	* models: model: created using joblib.dump()
	* logs: for future use with monitoring application statistics
* in Word PowerShell, call files to run python code
* packages required are listed in requirements.txt
* include README file
* include .gitignore

