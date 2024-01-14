# data_transform.py
import pandas as pd

class DataTransform:
    @staticmethod
    def convert_to_numeric(df, columns):
        """Convert specified columns to numeric format."""
        df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
        return df

    @staticmethod
    def convert_to_datetime(df, columns):
        """Convert specified columns to datetime format."""
        df[columns] = df[columns].apply(pd.to_datetime, errors='coerce')
        return df

    @staticmethod
    def convert_to_categorical(df, columns):
        """Convert specified columns to categorical format."""
        df[columns] = df[columns].astype('category')
        return df

    @staticmethod
    def remove_special_characters(df, columns):
        """Remove special characters from specified columns."""
        df[columns] = df[columns].replace('[^a-zA-Z0-9]', '', regex=True)
        return df
