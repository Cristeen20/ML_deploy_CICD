import pandas as pd
from flask import Flask, render_template
from analysis import run_analysis

app = Flask(__name__)

@app.route('/')
def index():
    mean_value = run_analysis()
    return render_template('index.html', mean_value = mean_value)

# def run_analysis():
#     file_path = r'C:\Users\siva\Desktop\ML_DEPLOY_CICD\ML_deploy_CICD\Annual-balance-sheets-2007-2022-provisional.csv'
#     data = pd.read_csv(file_path)
#     data['Values'] = pd.to_numeric(data['Values'], errors='coerce')
#     data = data.dropna(subset=['Values'])
#     mean_value = data['Values'].mean()
#     print("111111111111111111111111111")
#     print(mean_value)
#     return mean_value

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
