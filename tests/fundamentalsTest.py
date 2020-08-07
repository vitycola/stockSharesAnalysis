from __future__ import print_function

import fundamentals as fm

def test_fundamentals():

    tickers = ['MSFT', 'AAPL', 'MMM']

    for symbol in tickers:
        print(">>", symbol, end=' ... ')

        price = fm.Fundamentals(symbol).getPrice()

        # always should have info and history for valid symbols
        assert(price is not None)

        print("OK")

if __name__ == "__main__":
    test_fundamentals()