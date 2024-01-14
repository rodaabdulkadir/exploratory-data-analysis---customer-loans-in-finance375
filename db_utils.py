import yaml
import pandas as pd
from sqlalchemy import create_engine

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = None

    def connect(self):
        # Construct the database URL
        db_url = f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"

        # Create an SQLAlchemy engine
        self.engine = create_engine(db_url)

    def extract_data(self):
        if self.engine is None:
            raise ValueError("SQLAlchemy Engine not initialized. Call connect() method first.")

        # Execute a query to extract data from the RDS database
        query = "SELECT * FROM loan_payments"
        data_df = pd.read_sql(query, self.engine)

        return data_df

    def save_to_csv(self, data_df, filename='loan_payments_data.csv'):
        data_df.to_csv(filename, index=False)
        print(f"Data saved to {filename} successfully.")

    def load_from_csv(self, filename='loan_payments_data.csv'):
        try:
            data_df = pd.read_csv(filename)
            print(f"Data loaded from {filename} successfully.")
            return data_df
        except FileNotFoundError:
            print(f"Error loading data from CSV - File not found: {filename}")
            return None

# Function to load credentials from the credentials.yaml file
def load_credentials():
    credentials_file_path = "credentials.yaml"  # Assuming it's in the same directory
    with open(credentials_file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

def main():
    # Load credentials
    credentials = load_credentials()

    # Create an instance of RDSDatabaseConnector
    rds_connector = RDSDatabaseConnector(credentials)

    # Connect to the RDS database
    rds_connector.connect()

    # Extract data from the RDS database
    data_df = rds_connector.extract_data()

    # Save data to CSV
    rds_connector.save_to_csv(data_df)

    # Load data from CSV
    loaded_data_df = rds_connector.load_from_csv()

    # Perform additional analysis or processing if needed

if __name__ == "__main__":
    main()



