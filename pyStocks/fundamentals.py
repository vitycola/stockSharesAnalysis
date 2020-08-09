import yfinance as yf
import pandas as pd

class Fundamentals():

    def __init__(self,ticker):
        self.ticker = ticker.upper()
        self.share = yf.Ticker(ticker)

    def getCompanyName(self):
        return self.share.info['shortName']

    def getPrice(self):
        return self.share.info['currentPrice']

    def getHistPrice(self) -> pd.Series:
        return self.share.history('max')['Open']

    def getSector(self):
        return self.share.info['sector']

    def getIndustry(self):
        return self.share.info['industry']

    def getMarketCap(self):
        return self.share.info['marketCap']

    def getSharesVolume(self):
        return self.share.info['volume']

    def getBeta(self):
        return self.share.info['beta']

    def getDividendRate(self):
        return self.share.info['trailingAnnualDividendRate']

    def getDividendYield(self):
        return self.share.info['dividendYield']

    def getDividendHistory(self):
        return self.share.actions

    def getAvgDividendYield(self):
        return self.share.info['fiveYearAvgDividendYield']

    def getExDividendDate(self):
        return self.share.info['exDividendDate']

    def getPayOutRatio(self):
        return self.share.info['payoutRatio']

    def getHistRevenue(self):
        return self.share.financials.loc['Total Revenue']

    def getHistNetIncome(self):
        return self.share.financials.loc['Net Income']

    def getEPS(self):
        return self.share.info['trailingEps']

    def getForwardEPS(self):
        return self.share.info['forwardEps']

    def getSectorEPS(self): #TODO
        pass

    def getPairEPS(self): # TODO
        pass

    def getHistAssets(self) -> pd.Series:
        return self.share.balance_sheet.loc['Total Assets']

    def getHistLiabilities(self) -> pd.Series:
        return self.share.balance_sheet.loc['Total Liab']

    def getCurrentAssets(self)  -> pd.Series:
        return self.share.balance_sheet.loc['Total Current Assets']

    def getCurrentLiabilities(self)  -> pd.Series:
        return self.share.balance_sheet.loc['Total Current Liabilities']

    def getCurrentRatio(self):
        return self.share.info['currentRatio']

    def getQuickRatio(self):
        return self.share.info['quickRatio']

    def getROE(self):
        return self.share.info['returnOnEquity']

    def getSectorROE(self): #TODO
        pass

    def getHistFreeCashFlow(self) -> pd.Series: #TODO
        pass

    def getPER(self):
        return self.share.info['trailingPE']

    def getforwardPER(self):
        return self.share.info['forwardPE']

    def getPEG(self):
        return self.share.info['pegRatio']

    def getAnalystRecommendations(self) ->pd.DataFrame:
        return self.share.recommendations.groupby('To Grade').count()

    def getAnalystRecommendations(self, date) -> pd.DataFrame:
        return self.share.recommendations[date].groupby('To Grade').count()

