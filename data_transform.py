import pandas as pd

class DataTransform:
    @staticmethod
    def convert_dates(df, date_columns):
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        return df

    @staticmethod
    def convert_to_numeric(df, numeric_columns):
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df

    @staticmethod
    def convert_to_categorical(df, categorical_columns):
        for col in categorical_columns:
            df[col] = df[col].astype('category')
        return df

    @staticmethod
    def remove_excess_symbols(df, numeric_columns):
        for col in numeric_columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)
        return df
