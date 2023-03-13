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

profit = prices[sellday] - prices[buyday]

for=>

print(max(prices))
print(min(prices))
print(prices[0-5])
print (profit)

prevPrice = max(prices)

for x in prices:
    if x > prevPrice:
        buyPrice = prevPrice

executionTime = (time.time() - startTime) * 1000
print('Execution time in milliseconds: ' + "{:.2f}".format(executionTime))
