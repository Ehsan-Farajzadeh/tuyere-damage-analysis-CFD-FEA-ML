import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Define the injection rates for RCOG
injection_rates = [100, 125, 150, 175, 200]

# Function to load data and perform analysis
def analyze_file(file_path):
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    # Ensure all relevant columns are of numeric type
    input_columns = ['CO', 'CO2', 'H2', 'H2O', 'Heat_of_Het', 'Het1', 'Het2', 'Het3', 'N2', 'O2', 'RR2', 'RR3', 'Static_Enth', 'Velocity']
    data[input_columns] = data[input_columns].apply(pd.to_numeric, errors='coerce')

    # Drop rows with any NaN values
    data = data.dropna()

    X = data[input_columns]
    y_strain = data['Strain']
    y_stress = data['Stress']

    # Train-test split for both output parameters
    X_train_strain, X_test_strain, y_train_strain, y_test_strain = train_test_split(X, y_strain, test_size=0.2, random_state=42)
    X_train_stress, X_test_stress, y_train_stress, y_test_stress = train_test_split(X, y_stress, test_size=0.2, random_state=42)

    # Define the model
    model_strain = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
    model_stress = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)

    # Train the model
    model_strain.fit(X_train_strain, y_train_strain)
    model_stress.fit(X_train_stress, y_train_stress)

    # Predict on the test set
    y_pred_strain = model_strain.predict(X_test_strain)
    y_pred_stress = model_stress.predict(X_test_stress)

    # Evaluate the model
    mse_strain = mean_squared_error(y_test_strain, y_pred_strain)
    mse_stress = mean_squared_error(y_test_stress, y_pred_stress)

    print(f'{file_path} - Mean Squared Error for Strain: {mse_strain}')
    print(f'{file_path} - Mean Squared Error for Stress: {mse_stress}')

    # Feature importance
    xgb.plot_importance(model_strain)
    plt.title(f'Feature Importance for Strain ({file_path})')
    plt.show()

    xgb.plot_importance(model_stress)
    plt.title(f'Feature Importance for Stress ({file_path})')
    plt.show()

# Loop through injection rates for RCOG
for rate in injection_rates:
    file_path = f'RCOG_{rate}.csv'
    print(f'Analyzing RCOG at injection rate {rate}')
    analyze_file(file_path)

