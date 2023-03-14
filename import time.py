"""docstring"""

import random
import time

random.seed(10)

# prices = [4,3,2,7,8,9]
prices = []
for i in range(0, 5000):
    n = random.randint(1, 5000)
    prices.append(n)

startTime = time.time()

buyDay = 0
bestBuyDay = 0
sellDay = 1
bestSellDay = 1

maxProfit = -5000

for buyDay in range(len(prices)-1):
    for sellDay in range(buyDay,len(prices)):
        # if buyDay < sellDay:
            profit = prices[sellDay] - prices[buyDay]
            # print(buyDay,sellDay,profit)
            if profit > maxProfit:
                maxProfit = profit
                bestBuyDay = buyDay
                bestSellDay = sellDay

print(bestBuyDay,bestSellDay,maxProfit)

executionTime = (time.time() - startTime) * 1000
print('Execution time in milliseconds: ' + "{:.2f}".format(executionTime))
