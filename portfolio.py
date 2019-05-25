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
        