from pandas_datareader import data as pdr
import datetime
#import fix_yahoo_finance as yf
import pandas as pd
import json

class Stocks:

    def stocksDF(self):
        start = datetime.datetime(2008, 1, 1)
        end = datetime.datetime(2018, 8, 28)
        companyStocks = {}
        for company in self.conf["companies"]:
            companyStocks[company] = pdr.get_data_yahoo(company, start=start, end=end)
        return companyStocks

    def __init__(self):

        #Load the configuration
        conf_path = "conf/config.json"
        with open(conf_path) as file:
            self.conf = json.load(file)




