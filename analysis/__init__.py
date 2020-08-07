

if __name__ == '__main__':

    def calc_profitability(sharesNum, sharePrice, estimatedGrowth, dividendYield, dividendGrowthR, time):
        """
        Calculate dividends and share price profit from a initial share price and growth estimation

        :param sharesNum: number of shares to buy
        :param sharePrice: price of each share to buy
        :param estimatedGrowth: % growth estimation for shares price (Ex: 6 -> 6%)
        :param dividendYield: %
        :param dividendGrowthR: % of how much the company increase the dividend (Ex: 3.7)
        :param time: number of years to simulate
        :return: Out format is WIP
        """

        #TODO: include annual contribution param and add to simulation
        #TODO: include YOC calc
        #TODO: include 3 scenario based on given estimated growth
        #TODO: format in functions and format the output

        shares = [sharePrice]
        dividends = [0]
        actualDivYield = dividendYield / 100

        for year in range(1,time+1):

            sharePriceYTD = shares[year - 1]
            #Calculate current dividend Yield and dividend amount
            dividendAmount = round(sharesNum * sharePriceYTD * actualDivYield,2)
            dividends.append(dividendAmount)
            actualDivYield = round(actualDivYield + actualDivYield * (dividendGrowthR / 100),4)

            #Calculate Stock Value
            sharePriceTTM = round(sharePriceYTD * (1 + estimatedGrowth / 100),2)
            totalSharePriceTTM = sharesNum * sharePriceTTM
            shares.append(sharePriceTTM)

            #Caculate Stock Balance, share accum profit and share + dividends accumulated profit
            stockBalance = round(totalSharePriceTTM + dividendAmount, 2)
            shareAccumProfit = round(((totalSharePriceTTM / (sharesNum * sharePrice)) - 1) * 100, 4)
            balanceAccumProfit = round((((totalSharePriceTTM + sum(dividends)) / (sharesNum * sharePrice)) - 1) * 100, 4)

            print(year, sharesNum, dividendAmount/sharesNum, dividendAmount, sharePriceTTM, sharesNum * sharePriceTTM, stockBalance, shareAccumProfit, balanceAccumProfit )
        print("Total dividends:",sum(dividends))

    calc_profitability(7, 42.5, 1, 7.90, 2.96, 10)


