from scrapper.loadData import loadData

if __name__ == '__main__':

    df = loadData()
    print(df.createDF().head())

    print(df.createDF().__doc__)