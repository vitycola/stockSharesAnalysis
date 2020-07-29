from scrapper.Fundamentals import Fundamentals
from scrapper.Stocks import Stocks

if __name__ == '__main__':

    df = Fundamentals()
    print(df.fundamentalDF().head())
    #dfStocks = Stocks()
    #print(dfStocks.stocksDF())
