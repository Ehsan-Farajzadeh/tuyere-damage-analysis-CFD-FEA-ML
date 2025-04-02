# utils.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_combined_csv(fuel_type, injection_rates, directory='.'):
    """
    Load and concatenate CSV files for a given fuel type across multiple injection rates.
    """
    combined_df = pd.DataFrame()
    for rate in injection_rates:
        file_path = os.path.join(directory, f"{fuel_type}_{rate}.csv")
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        else:
            print(f"File not found: {file_path}")
    return combined_df

def filter_high_stress(df, threshold=1000):
    """
    Filter the dataframe to include only rows where stress exceeds the given threshold.
    """
    return df[df['Stress'] > threshold]

def drop_irrelevant_columns(df, exclude_cols=['X', 'Y', 'Z', 'Strain']):
    """
    Drop irrelevant or unwanted columns from the dataframe.
    """
    return df.drop(columns=exclude_cols, errors='ignore')

def plot_correlation_heatmap(df, title, save_path=None):
    """
    Plot a heatmap of the correlation matrix for the dataframe.
    """
    correlation = df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.show()

def save_correlation_matrix(df, filename):
    """
    Save the correlation matrix of the dataframe to a CSV file.
    """
    correlation = df.corr()
    correlation.to_csv(filename)
    print(f"Saved correlation matrix to {filename}")

