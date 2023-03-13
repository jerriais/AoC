"""docstring"""

import random
import time

startTime = time.time()

prices = [4,3,2,7,8,9]
# for i in range(0, 5000):
#     n = random.randint(1, 1000000)
#     prices.append(n)

buyday = 0
sellday = 1

def name(args):
 pass

def calculateProfit(sellday, buyday):
    return prices[sellday] - prices[buyday]

while sellday < len(prices):
    while buyday < (len(prices)-1):
        print(calculateProfit(sellday, buyday))
        buyday += 1
    sellday += 1

print(max(prices))
print(min(prices))
print ("AA")

prevPrice = max(prices)

for x in prices:
    if x > prevPrice:
        buyPrice = prevPrice

executionTime = (time.time() - startTime) * 1000
print('Execution time in milliseconds: ' + "{:.2f}".format(executionTime))
