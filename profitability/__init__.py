

if __name__ == '__main__':

    def calc_profitability(sharesNum, sharePrice, estimatedGrowth, dividendYield, dividendGrowthR, time, volatility= 6):

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
    calc_profitability(2, 151.5, 6, 3.76, 3.13, 10)


