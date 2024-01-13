import pymysql

class RDSDatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
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

import yaml

# Function to read credentials from YAML file
def read_credentials(file_path='credentials.yaml'):
    try:
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)
            return credentials
    except Exception as e:
        print(f"Error: Unable to read credentials from {file_path} - {str(e)}")
        return None

# Example usage:
credentials = read_credentials()
print(credentials)
