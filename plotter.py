import seaborn as sns
import matplotlib.pyplot as plt

class Plotter:
    @staticmethod
    def visualize_outliers(df):
        # Visualize outliers using box plots
        numeric_cols = df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            plt.figure(figsize=(8, 5))
            sns.boxplot(x=df[col])
            plt.title(f'Boxplot for {col}')
            plt.show()
