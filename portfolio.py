import numpy as np


class Portfolio():
    def __init__(self, stocks, weights=None):
        self.stocks = stocks
        self.weights = self._initialise_weights(weights)
        self.items = dict(zip(self.stocks, self.weights))


    def __repr__(self):
        return f'Portfolio(stocks={self.stocks}, weights={self.weights})'


    def __getitem__(self, value):
        try:
            item = self.items.get(value)
        except KeyError:
            raise KeyError('KeyError: That stock does not exist in this portfolio.')
        
        return item


    def _initialise_weights(self, weights):
        if not weights:
            weights = np.random.random(size=len(self.stocks))
            weights /= sum(weights)
        else:
            if len(weights) != len(self.stocks):
                raise ValueError('Parameters weights and stocks must be of the same length.')

        return np.array(weights)


    def calculate_return(self, return_data):
        """ For a set of historical returns data, calculate the overall return for this portfolio."""
        returns_data = self.cleanse_return_data(return_data)

        return np.sum((returns_data.mean() * self.weights)) * 252


    def calculate_volatility(self, return_data):
        """ For a set of historical returns data, calculate the overall volatility for this portfolio."""
        returns_data = self.cleanse_return_data(return_data)

        return np.sqrt(np.dot(self.weights.T, np.dot(returns_data.cov() * 252, self.weights))) 


    def cleanse_return_data(self, return_data):
        stock_in_data = set(stock.lower() for stock in return_data.columns.to_list())
        stock_in_portfolio = set(stock.lower() for stock in self.stocks)

        # Filter the data to only include stocks in this portfolio
        if len(stock_in_data - stock_in_portfolio) > 0:
            log_returns_data = log_returns_data.filter(items=self.stocks)
        # Check that the all the stocks of this portfolio are in the data=
        elif len(stock_in_portfolio - stock_in_data) > 0:
            raise ValueError('Not all stocks represented in the data supplied to this function.')

        return return_data