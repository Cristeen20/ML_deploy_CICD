
import pandas as pd

def run_analysis():
    file_path = r'C:\Users\siva\Desktop\ML_DEPLOY_CICD\ML_deploy_CICD\Annual-balance-sheets-2007-2022-provisional.csv'
    data = pd.read_csv(file_path)
    data['Values'] = pd.to_numeric(data['Values'], errors='coerce')
    data = data.dropna(subset=['Values'])
    mean_value = data['Values'].mean()
    result = f"{mean_value:.2f}"
    print(result)  # Debugging output
    print(f"Type of result: {type(result)}")  # Print the type of result
    return result
