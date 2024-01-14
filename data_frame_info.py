import pandas as pd
class DataFrameInfo:
    @staticmethod
    def describe_columns(df):
        """Describe all columns in the DataFrame to check their data types."""
        return df.dtypes

    @staticmethod
    def extract_statistical_values(df):
        """Extract statistical values: median, standard deviation, and mean from the columns and the DataFrame."""
        return df.describe()

    @staticmethod
    def count_distinct_values(df, categorical_columns):
        """Count distinct values in categorical columns."""
        return df[categorical_columns].nunique()

    @staticmethod
    def print_shape(df):
        """Print out the shape of the DataFrame."""
        return df.shape

    @staticmethod
    def generate_null_counts(df):
        """Generate a count/percentage count of NULL values in each column."""
        null_counts = df.isnull().sum()
        return null_counts, null_counts / len(df) * 100
