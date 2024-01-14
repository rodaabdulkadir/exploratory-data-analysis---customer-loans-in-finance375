## Exploratory Data Analysis - Customer Loans in Finance

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [License](#license)

## Description

This project focuses on analysing loan payment data to derive insights into customer payment behaviour and potential risks. The project includes data preprocessing, exploratory data analysis, and visualisation of key indicators related to loan status, recovery percentages, and potential losses.

The main goals of the project are:
1.Identify indicators that may suggest a customer is unable to pay the loan.
2.Analyse loan grades, purposes, and home ownership as potential factors affecting loan repayment.
3.Visualise and understand the distribution of loan statuses and recovery percentages.

Throughout the project, various Python scripts have been developed to perform data transformation, correlation analysis, and payments analysis. These scripts assist in uncovering patterns, trends, and potential risks within the loan payment dataset, aiding in informed decision-making for the lending institution.

## Installation

1. Clone the repository:

   git clone https://github.com/rodaabdulkadir/exploratory-data-analysis---customer-loans-in-finance375.git
   
 2. Install the required dependencies:  
    ```bash
    pip install -r requirements.txt


## Usage

1.Execute the Jupyter Notebooks or Python scripts for specific analyses:

- data_frame_info.py: Display information about the DataFrame.
- data_frame_transform.py: Data preprocessing and transformation.
- correlation_analysis.py: Identify and remove highly correlated columns.
- loan_indicators_analysis.py: Analyze indicators affecting loan repayment.
- payment_analysis.py: Analyze loan payments, recovery percentages, and potential losses.
- plotter.py: Utility for visualization.
  
2.Follow the instructions within each script for additional configurations and analysis steps.

## File Structure


exploratory-data-analysis---customer-loans-in-finance375/

│

|--  .gitignore

|-- Additional analysis.ipynb

|-- README.md

|-- correlation_analysis.py

|--  credentials.yaml

|--  data_frame_info.py

|--  data_frame_transform.py

|--  data_transform.py

|--  db_utils.py

|--  loan_indicators_analysis.py

|--  loan_payments_data.csv

|--  payment_analysis.py

|--  plotter.py

|--  requirements.txt
