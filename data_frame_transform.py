#
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

class DataFrameTransform:
    @staticmethod
    def check_nulls(df):
        return df.isnull().sum()

    @staticmethod
    def drop_nulls(df, row_threshold=0.5, col_threshold=0.5):
        # Drop rows with null values exceeding the threshold
        df = df.dropna(axis=0, thresh=int(row_threshold * len(df.columns)))

        # Drop columns with null values exceeding the threshold
        df = df.dropna(axis=1, thresh=int(col_threshold * len(df)))

        return df

    @staticmethod
    def impute_nulls(df, strategy='median'):
        # Convert '36 months' to numeric
        df['term'] = df['term'].str.extract('(\d+)').astype(float)

        # Impute missing values with specified strategy (median by default)
        imputer = SimpleImputer(strategy=strategy)
        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

        return df_imputed

    @staticmethod
    def convert_to_numeric(df, columns):
        le = LabelEncoder()
        for col in columns:
            df[col] = le.fit_transform(df[col])
        return df

    @staticmethod
    def convert_to_categorical(df, columns):
        for col in columns:
            df[col] = df[col].astype('category')
        return df

    @staticmethod
    def remove_special_characters(df, columns):
        for col in columns:
            df[col] = df[col].str.replace('[^a-zA-Z0-9]', '', regex=True)
        return df

    @staticmethod
    def remove_outliers(df: pd.DataFrame, z_threshold: int = 3) -> pd.DataFrame:
        z_scores = zscore(df.select_dtypes(include=['number']))
        abs_z_scores = abs(z_scores)
        outliers = (abs_z_scores > z_threshold).all(axis=1)

        df_no_outliers = df[~outliers].reset_index(drop=True)

        return df_no_outliers

    @staticmethod
    def scale_numeric_features(df: pd.DataFrame) -> pd.DataFrame:
        scaler = StandardScaler()
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        return df

    @staticmethod
    def remove_highly_correlated_columns(df: pd.DataFrame, correlation_threshold: float = 0.8) -> pd.DataFrame:
        correlation_matrix = df.corr()

        highly_correlated_cols = set()
        for i in range(len(correlation_matrix.columns)):
            for j in range(i):
                if abs(correlation_matrix.iloc[i, j]) > correlation_threshold:
                    colname = correlation_matrix.columns[i]
                    highly_correlated_cols.add(colname)

        df_filtered = df.drop(columns=highly_correlated_cols)

        return df_filtered
