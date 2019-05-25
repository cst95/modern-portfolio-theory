import pandas as pd
import fix_yahoo_finance as yf 
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import numpy as np

VALID__DATATYPES = ['close', 'high', 'low', 'open', 't', 'volume', 'adj close']
PLOT_TYPES = ['log_returns','close', 'high', 'low', 'open', 't', 'volume', 'adj close']

yf.pdr_override() 


class StockData():
    def __init__(self, stocks, start='2014-01-01', end='2019-01-01'):
        self.stocks = stocks
        self.start = pd.to_datetime(start)
        self.end = pd.to_datetime(end)
        self._data = self.fetch_data() 


    @property
    def log_returns(self):
        close_data = self.get('Adj Close') 
        return np.log(close_data / close_data.shift(1))


    def fetch_data(self):
        try:
            data = pdr.get_data_yahoo(self.stocks, self.start, self.end)
        except:
            raise Exception("Couldn't fetch the stock data.")
        return data


    def get(self, key):
        if key.lower() in VALID__DATATYPES:
            data = self._data[key.title()]
            data.columns = self.stocks
            return data
        else: 
            raise ValueError(f'Invalid data type. Please choose from one of {VALID__DATATYPES}')
    
    
    def plot(self, plottype):
        if plottype.lower() in PLOT_TYPES:
            if plottype.lower() == 'log_returns':
                self.log_returns.plot()
                plt.show()
            else:
                self.get(plottype.title()).plot()
                plt.show()
        return None
            