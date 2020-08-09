import pandas as pd
from pyStocks.fundamentals import Fundamentals

class Utils():

    def getAllData(tickers) -> pd.DataFrame:

        fundamentalData = {}
        exec_methods = ["getCompanyName", "getPrice", "getSector", "getIndustry", "getMarketCap", "getSharesVolume",
                        "getBeta", "getDividendRate", "getDividendYield", "getPayOutRatio", "getEPS", "getCurrentRatio",
                        "getQuickRatio", "getROE", "getPER", "getPEG"]

        #Creates dict sctructure
        for method in exec_methods:
            fundamentalData[method.split("get")[1]] = []

        for ticker in tickers:
            f =  Fundamentals(ticker)
            for method in exec_methods:
                fundamentalData[method.split("get")[1]].append(getattr(f, method)())

        return pd.DataFrame(fundamentalData)