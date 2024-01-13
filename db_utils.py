import pymysql
import pandas as pd
from sqlalchemy import create_engine

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials.get('RDS_HOST')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
        self.port = credentials.get('RDS_PORT')
        self.connection = None
        self.engine = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            print("Connected to the database")
            self.create_engine()
        except Exception as e:
            print(f"Error: Unable to connect to the database - {str(e)}")

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print("Disconnected from the database")
        except Exception as e:
            print(f"Error: Unable to disconnect from the database - {str(e)}")

    def create_engine(self):
        try:
            self.engine = create_engine(
                f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            )
            print("SQLAlchemy Engine created")
        except Exception as e:
            print(f"Error: Unable to create SQLAlchemy Engine - {str(e)}")

    def execute_query(self, query):
        try:
            if self.engine:
                result = pd.read_sql_query(query, self.engine)
                return result
            else:
                print("Error: SQLAlchemy Engine not initialized. Call connect() method first.")
                return None
        except Exception as e:
            print(f"Error executing query - {str(e)}")
            return None

    def extract_data_as_dataframe(self):
        # Assuming 'loan_payments' is the name of the table
        query = "SELECT * FROM loan_payments"
        return self.execute_query(query)

    def save_data_to_csv(self, data, file_path='loan_payments_data.csv'):
        try:
            data.to_csv(file_path, index=False)
            print(f"Data saved to {file_path}")
        except Exception as e:
            print(f"Error saving data to CSV - {str(e)}")

    def load_data_to_dataframe(self, file_path='loan_payments_data.csv'):
        try:
            data = pd.read_csv(file_path)
            print(f"Data loaded from {file_path}. Shape: {data.shape}")
            print("Sample of the data:")
            print(data.head())
            return data
        except Exception as e:
            print(f"Error loading data from CSV - {str(e)}")
            return None

# Example usage:
credentials = {
    'RDS_HOST': 'eda-projects.cq2e8zno855e.eu-west-1.rds.amazonaws.com',
    'RDS_USER': 'loansanalyst',
    'RDS_PASSWORD': 'EDALoananalyst',
    'RDS_DATABASE': 'payments',
    'RDS_PORT': 5432
}

rds_connector = RDSDatabaseConnector(credentials)
rds_connector.connect()

# Save data to a CSV file
loan_payments_data = rds_connector.extract_data_as_dataframe()
rds_connector.save_data_to_csv(loan_payments_data)

# Load data from the CSV file into a Pandas DataFrame
loaded_data = rds_connector.load_data_to_dataframe()

# Perform other operations as needed

rds_connector.disconnect()



