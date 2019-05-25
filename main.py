import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from portfolio import Portfolio 
from stockdata import StockData


def show_data(data):
    data.plot(figsize=(10,5))
    plt.show()
    return None


if __name__ == '__main__':
    stocks = ['AAPL','WMT','TSLA','GE','AMZN','DB']

    start = '2014-01-01'
    end = '2019-01-01'

    data = StockData(stocks, start, end)

    daily_returns = data.log_returns

    portfolio_returns = []
    portfolio_variances = []

    for i in range(10000):
        p = Portfolio(stocks)

        p_return = p.calculate_return(daily_returns)
        p_variance = p.calculate_volatility(daily_returns)

        portfolio_returns.append(p_return)
        portfolio_variances.append(p_variance)

    preturns = np.array(portfolio_returns)
    pvariances = np.array(portfolio_variances)

    plt.figure(figsize=(10,6))
    plt.scatter(pvariances, preturns, c=preturns/pvariances, marker='o')
    plt.grid = True
    plt.xlabel('Expected volatility')
    plt.ylabel('Expected returns')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()
