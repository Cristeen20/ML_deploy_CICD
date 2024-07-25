import pandas as pd

# Load the data
file_path = r'C:\Users\siva\Desktop\ML_DEPLOY_CICD\ML_deploy_CICD\Annual-balance-sheets-2007-2022-provisional.csv'
data = pd.read_csv(file_path)

# Convert 'Values' column to numeric, forcing non-numeric values to NaN
data['Values'] = pd.to_numeric(data['Values'], errors='coerce')

# Handle NaN values by dropping them (or alternatively, fill them)
data = data.dropna(subset=['Values'])

# Calculate the mean
mean_value = data['Values'].mean()

def run_analysis():
    mean_value = data['Values'].mean()
    return mean_value

# print(run_analysis())