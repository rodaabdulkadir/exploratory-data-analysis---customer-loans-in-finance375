## Exploratory Data Analysis - Customer Loans in Finance

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [License](#license)

## Description

This project focuses on analyzing loan payment data to derive insights into customer payment behavior and potential risks. The project includes data preprocessing, exploratory data analysis, and visualization of key indicators related to loan status, recovery percentages, and potential losses.

The main goals of the project are:
- Identify indicators that may suggest a customer is unable to pay the loan.
- Analyze loan grades, purposes, and home ownership as potential factors affecting loan repayment.
- Visualize and understand the distribution of loan statuses and recovery percentages.

Throughout the project, various Python scripts have been developed to perform data transformation, correlation analysis, and payments analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rodaabdulkadir/exploratory-data-analysis---customer-loans-in-finance375.git
   cd exploratory-data-analysis---customer-loans-in-finance375

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


project-root/
│
├── .gitignore
├── Additional analysis.ipynb
├── README.md
├── credentials.yaml
├── data_frame_info.py
├── data_frame_transform.py
├── data_transform.py
├── db_utils.py
├── loan_indicators_analysis.py
├── payment_analysis.py
├── plotter.py
├── loan_payments_data.csv
└── requirements.txt
