import pymysql
import yaml

def load_credentials(file_path='credentials.yaml'):
    try:
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)
            return credentials
    except Exception as e:
        print(f"Error: Unable to load credentials from {file_path} - {str(e)}")
        return None

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials.get('RDS_HOST')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
        self.port = credentials.get('RDS_PORT')
        self.connection = None

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
        except Exception as e:
            print(f"Error: Unable to connect to the database - {str(e)}")

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print("Disconnected from the database")
        except Exception as e:
            print(f"Error: Unable to disconnect from the database - {str(e)}")

# Example usage:
# credentials = load_credentials()
# rds_connector = RDSDatabaseConnector(credentials)
# rds_connector.connect()
# # Perform operations like fetching data or other tasks
# rds_connector.disconnect()

