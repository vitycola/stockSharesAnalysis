from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import json
import re

class loadData:

    def parse_html(self, page_type, symbol):
        """
        Parse html depending on page type and company

        Arguments:
            page_type -- the page type
            symbol -- company short name

        Return:
            BeautifulSoup Object with parsed html

        """
        page_dict = {"statistics": "/key-statistics",
                     "comp_info": "/profile"
                     }

        try:
            # Parse company statistic site
            url = ("https://finance.yahoo.com/quote/" + symbol.lower() + page_dict[page_type])
            soup = bs(requests.get(url).content, "html.parser")
        except Exception as e:
            print(symbol, 'not found')

        return soup

    def get_all_metrics(self) -> list:
        """
        TO DO
        :return:
        """
        p = []
        symbol = "TEF"  # TEF by reference
        soup = self.parse_html("comp_info", symbol)
        metrics = soup.find(class_="Mstart(a) Mend(a)").find_all("tr")
        for tr in metrics:
            td = tr.find_all("span")
            p.append(td[0].text)
        return p

    def fundamental_metric(self, soup, metric) -> str:
        """
        TO DO
        :param metric:
        :return:
        """
        #TO DO: Try Catch excpections
        return soup.find(text=re.compile(metric+"*")).find_next(class_='Fz(s) Fw(500) Ta(end)').text

    def company_info(self, soup) -> list:
        """
        TO DO
        :param symbol:
        :return:
        """
        #TO DO: Try Catch expections
        sector = soup.find(text="Sector").find_next().text
        industry = soup.find(text="Industry").find_next().text
        return [sector, industry]



    def get_fundamental_data(self, df):
        """
        TO DO
        :param df:
        :return:
        """
        #Iterate over companies
        for symbol in df.index:
            #TO DO: try and catch expections
            compSoup = self.parse_html("comp_info", symbol)
            metricSoup = self.parse_html("statistics", symbol)

            lon = len(self.conf["comp_info"])
            for idx, col in enumerate(df.columns[:int(lon)]):
                df.loc[symbol, col] = self.company_info(compSoup)[idx]
            for metric in df.columns[int(lon):]:
                df.loc[symbol, metric] = self.fundamental_metric(metricSoup, metric)

        return df

    def createDF(self):
        """
        TO DO
        :return:
        """
        #Reads conf with companies and columns and create indexed Dataframe
        df = pd.DataFrame(index= self.conf["companies"], columns= self.conf["comp_info"] + self.conf["metrics"])
        return self.get_fundamental_data(df)

    def __init__(self):

        #Load the configuration
        conf_path = "conf/config.json"
        with open(conf_path) as file:
            self.conf = json.load(file)




