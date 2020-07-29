from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import json
import re

class Fundamentals:

    def _parse_html(self, page_type, symbol):
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
            print(symbol, 'not found: ', e)

        return soup

    def _get_all_metrics(self) -> list:
        """
        Gets all the metrics names in html
        :return: string with the metrics
        """
        p = []
        symbol = "TEF"  # TEF by reference
        soup = self.parse_html("comp_info", symbol)
        metrics = soup.find(class_="Mstart(a) Mend(a)").find_all("tr")
        for tr in metrics:
            td = tr.find_all("span")
            p.append(td[0].text)
        return p

    def _fundamental_metric(self, soup, metric) -> str:
        """
        Given HTML find the value of given metric
        :param metric: finantial metric we want to recover value
        :return: string value of given metric
        """
        fundMetric = ""
        try:
           fundMetric = soup.find(text=re.compile(metric + "*")).find_next(class_='Fz(s) Fw(500) Ta(end)').text
        except Exception as e:
            print('Metric ',metric, ' not found', e)
        return fundMetric

    def _company_info(self, soup) -> list:
        """
        Given HTML find the sector and industry of a company
        :param soup: HTML
        :return: List with Sector and Industry
        """
        sector = ""
        industry = ""
        try:
            sector = soup.find(text="Sector(s)").find_next().text
            industry = soup.find(text="Industry").find_next().text
        except Exception as e:
            print('Company Info not found: ', e)
        return [sector, industry]

    def _get_fundamental_data(self, df):
        """
        Given a DF with index companies and metrics in columns fills metric values with scrapped html
        :param df: Pandas empty dataframe with companies at index and metrics at columns
        :return: Pandas Dataframe with values
        """
        #Iterate over companies
        for symbol in df.index:
            #TO DO: try and catch expections
            compSoup = self._parse_html("comp_info", symbol)
            metricSoup = self._parse_html("statistics", symbol)

            lon = len(self.conf["comp_info"])
            for idx, col in enumerate(df.columns[:int(lon)]):
                df.loc[symbol, col] = self._company_info(compSoup)[idx]
            for metric in df.columns[int(lon):]:
                df.loc[symbol, metric] = self._fundamental_metric(metricSoup, metric)

        return df

    def fundamentalDF(self):
        """
        Creates empty Pandas DataFrame given companies and metrics from config
        :return: Indexed empty Dataframe
        """
        #Reads conf with companies and columns and create indexed Dataframe
        df = pd.DataFrame(index= self.conf["companies"], columns= self.conf["comp_info"] + self.conf["metrics"])
        return self._get_fundamental_data(df)


    def __init__(self):

        #Load the configuration
        conf_path = "conf/config.json"
        with open(conf_path) as file:
            self.conf = json.load(file)




