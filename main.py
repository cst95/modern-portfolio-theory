import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from portfolio import Portfolio 
from stockdata import StockData


def show_data(data):
    data.plot(figsize=(10,5))
    plt.show()
    return None

def calculate_returns(data):
    return np.log(data / data.shift(1))


def calculate_portfolio_return(returns, weights):
    return np.sum((returns.mean() * weights)) * 252

def calculate_portfolio_variance(returns, weights):
    return np.sqrt(np.dot(np.array(weights).T, np.dot(returns.cov() * 252, weights))) 

if __name__ == '__main__':
    stocks = ['AAPL','WMT','TSLA','GE','AMZN','DB']

    start = pd.to_datetime('2014-01-01') 
    end = pd.to_datetime('2019-01-01')

    data = StockData(stocks, start, end)

    adj_close = data.get('adj close')
    daily_returns = calculate_returns(adj_close)
    
    portfolio_returns = []
    portfolio_variances = []

    for i in range(10000):
        p = Portfolio(stocks)

        portfolio_return = calculate_portfolio_return(daily_returns, p.weights)
        portfolio_variance = calculate_portfolio_variance(daily_returns, p.weights)

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
