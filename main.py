import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf 

def download_data(stocks, start, end):
    data = pdr.get_data_yahoo(stocks, start=start, end=end)['Adj Close']
    data.columns = stocks
    return data

def show_data(data):
    data.plot(figsize=(10,5))
    plt.show()
    return None

def calculate_returns(data):
    return np.log(data / data.shift(1))

def calculate_weights(stocks):
    weights = np.random.random(len(stocks))
    return weights / np.sum(weights)

def calculate_portfolio_return(returns, weights):
    return np.sum((returns.mean() * weights)) * 252

def calculate_portfolio_variance(returns, weights):
    return np.sqrt(np.dot(np.array(weights).T, np.dot(returns.cov() * 252, weights))) 

if __name__ == '__main__':
    yf.pdr_override() 
    stocks = ['AAPL','WMT','TSLA','GE','AMZN','DB']

    start = pd.to_datetime('2014-01-01') 
    end = pd.to_datetime('2019-01-01')

    data = download_data(stocks, start, end)

    portfolio_returns = []
    portfolio_variances = []

    for i in range(10000):
        weights = calculate_weights(stocks)
        portfolio = dict(zip(stocks, weights))

        daily_returns = calculate_returns(data)
        portfolio_return = calculate_portfolio_return(daily_returns, list(portfolio.values()))
        portfolio_variance = calculate_portfolio_variance(daily_returns, list(portfolio.values()))

        portfolio_returns.append(portfolio_return)
        portfolio_variances.append(portfolio_variance)

    preturns = np.array(portfolio_returns)
    pvariances = np.array(portfolio_variances)

    plt.figure(figsize=(10,6))
    plt.scatter(pvariances, preturns, c=preturns/pvariances, marker='o')
    plt.grid = True
    plt.xlabel('Expected volatility')
    plt.ylabel('Expected returns')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()
