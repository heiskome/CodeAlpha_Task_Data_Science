# CodeAlpha_Task_Data_Science
Machine Learning and Data Analysis Projects

Overview

This repository contains four distinct machine learning and data analysis projects, each with its own Python implementation and a professional GUI built using Tkinter. The projects utilize various datasets to perform classification, regression, and data analysis tasks. Each task is implemented in a separate Python script with a dedicated GUI for user interaction.

Project Structure

The repository includes the following tasks, each with its own Python script and associated dataset:





Iris Flower Classification (iris_classification.py)





Dataset: iris.csv



Description: Classifies Iris flower species (Setosa, Versicolor, Virginica) based on measurements using a Logistic Regression model.



Libraries: Pandas, Scikit-learn, Tkinter



GUI Features: Input fields for sepal and petal measurements, prediction button, and model accuracy display.



Unemployment Analysis (unemployment_analysis.py)





Datasets: Unemployment in India.csv, Unemployment_Rate_upto_11_2020.csv



Description: Analyzes unemployment rate trends, focusing on the impact of Covid-19, with visualizations of trends and regional differences.



Libraries: Pandas, Matplotlib, Seaborn, Tkinter



GUI Features: Tabbed interface with trend line plot, regional boxplot, and text-based insights.



Car Price Prediction (car_price_prediction.py)





Dataset: car data.csv



Description: Predicts car selling prices based on features like year, mileage, and fuel type using a Linear Regression model.



Libraries: Pandas, Scikit-learn, Tkinter



GUI Features: Input fields for car features, prediction button, and error handling for invalid inputs.



Sales Prediction (sales_prediction.py)





Dataset: Advertising.csv



Description: Forecasts sales based on advertising spend (TV, Radio, Newspaper) using a Linear Regression model.



Libraries: Pandas, Scikit-learn, Tkinter



GUI Features: Input fields for advertising spends, prediction button, and error handling.

Installation

To run these projects, ensure you have Python installed (version 3.6 or higher recommended). Install the required libraries using pip:

pip install pandas scikit-learn matplotlib seaborn

Note: Tkinter is included in standard Python installations, so no additional installation is needed for the GUI components.

Usage





Clone the Repository:

git clone <repository-url>
cd <repository-directory>



Place Datasets:





Ensure the datasets (iris.csv, Unemployment in India.csv, Unemployment_Rate_upto_11_2020.csv, car data.csv, Advertising.csv) are in the same directory as the respective Python scripts.



Run a Script:





For example, to run the Iris Classification:

python iris_classification.py



Similarly, run other scripts (unemployment_analysis.py, car_price_prediction.py, sales_prediction.py) to launch their respective GUIs.



Interact with the GUI:





Each script launches a Tkinter-based GUI.



Enter the required inputs (e.g., measurements for Iris, advertising spends for Sales) and click the "Predict" or view the visualizations.



Error handling ensures valid inputs; invalid inputs will trigger an error message.

Datasets





Iris.csv: Contains measurements of Iris flowers (Sepal Length, Sepal Width, Petal Length, Petal Width) and their species.



Unemployment in India.csv and Unemployment_Rate_upto_11_2020.csv: Contain unemployment data by region, date, and area, including estimated unemployment rates and labor participation.



car data.csv: Includes car features like Year, Present Price, Driven Kms, Fuel Type, Selling Type, Transmission, and Owner, along with Selling Price.



Advertising.csv: Contains advertising spend on TV, Radio, and Newspaper, along with Sales data.

Requirements





Python 3.6+



Libraries: pandas, scikit-learn, matplotlib, seaborn



Tkinter (included with Python)

Notes





Ensure datasets are correctly formatted and present in the working directory to avoid file-not-found errors.



The GUIs are designed for simplicity and functionality, with error handling for user inputs.



For the Unemployment Analysis, the datasets are combined for comprehensive analysis, focusing on Covid-19 impacts.



Model performance metrics (e.g., accuracy for Iris, MSE for Car Price and Sales) are printed to the console for reference and, where applicable, displayed in the GUI.

Future Improvements





Add more advanced models (e.g., Random Forest, XGBoost) for better prediction accuracy.



Enhance GUIs with additional visualizations or interactive elements.



Include data export options for analysis results.



Optimize code for larger datasets or real-time data integration.
