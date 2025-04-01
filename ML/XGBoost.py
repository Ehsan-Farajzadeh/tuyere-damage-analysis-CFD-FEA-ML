# XGBoost Feature Correlation Heatmap Generator

This script analyzes the impact of different hydrogen-rich fuels on tuyere thermal stress using correlation analysis and heatmaps.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define the fuel types and injection rates
fuels = ["COG", "RCOG", "H2", "NormalBlast"]
injection_rates = [100, 125, 150, 175, 200]

# Placeholder for results
correlation_results = {}

# Loop through each fuel
def analyze_correlation():
    for fuel in fuels:
        combined_df = pd.DataFrame()

        # Load and combine data for all injection rates for the current fuel
        for rate in injection_rates:
            filename = f"{fuel}_{rate}.csv"
            if os.path.exists(filename):
                df = pd.read_csv(filename)
                combined_df = pd.concat([combined_df, df])

        # Ensure we have data to process
        if combined_df.empty:
            continue

        # Filter the data to include only rows where Stress > 1000 MPa
        filtered_df = combined_df[combined_df['Stress'] > 1000]

        # Exclude X, Y, Z, and Strain columns
        filtered_df = filtered_df.drop(columns=['X', 'Y', 'Z', 'Strain'], errors='ignore')

        # Ensure there is data after filtering
        if filtered_df.empty:
            continue

        # Calculate the correlation matrix for all remaining variables
        correlation_df = filtered_df.corr()

        # Save the correlation matrix to a CSV file
        correlation_df.to_csv(f'{fuel}_correlation_matrix_stress_above_1000_MPa.csv')

        # Store the correlation results for heatmap visualization
        correlation_results[fuel] = correlation_df

# Generate heatmaps for visualization
def plot_heatmaps():
    for fuel, correlation_df in correlation_results.items():
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_df, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
        plt.title(f'Correlation Matrix Heatmap for Stress > 1000 MPa - {fuel}')
        plt.show()

# Run the analysis
if __name__ == "__main__":
    analyze_correlation()
    plot_heatmaps()
