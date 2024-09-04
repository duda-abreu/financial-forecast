import yfinance as yf
import pandas as pd
import numpy as np

def download_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv('data/stock_data.csv')
    return data

def load_and_preprocess_data(filepath, n_steps):
    data = pd.read_csv(filepath)
    data['Close'] = (data['Close'] - data['Close'].mean()) / data['Close'].std()
    X, y = [], []
    for i in range(len(data) - n_steps):
        X.append(data['Close'].values[i:i+n_steps])
        y.append(data['Close'].values[i+n_steps])
    return np.array(X), np.array(y)

if __name__ == "__main__":
    download_stock_data('^GSPC', '2000-01-01', '2024-01-01')  # Período aumentado