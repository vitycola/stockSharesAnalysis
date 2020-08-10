import pandas as pd
from pyStocks.fundamentals import Fundamentals
import re

class Utils():

    def getAllData(tickers) -> pd.DataFrame:

        fundamentalData = {}
        exec_methods = ["getCompanyName", "getSector", "getIndustry", "getPrice", "getMarketCap", "getSharesVolume",
                        "getBeta", "getDividendRate", "getDividendYield", "getPayOutRatio", "getEPS", "getCurrentRatio",
                        "getQuickRatio", "getROE", "getPER", "getPEG", "calcIncreasingRevenue", "calcIncreasingNetIncome"]

        #Creates dict sctructure
        for method in exec_methods:
            fundamentalData[re.split("get|calc",method)[1]] = []

        for ticker in tickers:
            f =  Fundamentals(ticker)
            for method in exec_methods:
                fundamentalData[re.split("get|calc",method)[1]].append(getattr(f, method)())

        return pd.DataFrame(fundamentalData)