"""docstring"""

import random
import time

random.seed(10)

startTime = time.time()

# prices = [4,3,2,7,8,9]
prices = []
for i in range(0, 10):
    n = random.randint(1, 5000)
    prices.append(n)

buyDay = 0
bestBuyDay = 0
sellDay = 1
bestSellDay = 1

def calculateProfit(sellDay, buyDay):
    if sellDay > buyDay:
        return prices[sellDay] - prices[buyDay]

maxProfit = calculateProfit(sellDay,buyDay)

for buyDay in range(len(prices)-1):
    for sellDay in range(buyDay,len(prices)):
        if buyDay < sellDay:
            profit = calculateProfit(sellDay, buyDay)
            print(buyDay,sellDay,profit)
            if profit > maxProfit:
                maxProfit = profit
                bestBuyDay = buyDay
                bestSellDay = sellDay


print(max(prices))
print(min(prices))
print ((prices))
print(bestBuyDay,bestSellDay,maxProfit)

executionTime = (time.time() - startTime) * 1000
print('Execution time in milliseconds: ' + "{:.2f}".format(executionTime))
