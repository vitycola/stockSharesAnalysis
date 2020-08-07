from __future__ import print_function
import utils

def test_utils():

    tickers = ['MSFT', 'AAPL', 'MMM']

    assert (utils.getAllData(tickers).shape[0] == len(tickers))

if __name__ == "__main__":
    test_utils()