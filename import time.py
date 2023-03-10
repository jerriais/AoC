import random
import time

startTime = time.time()

prices = []
for i in range(0,5000):
  n = random.randint(1,1000000)
  prices.append(n)

print (max(prices))
print (min(prices))
print (prices[0-10])

prevPrice = max(prices)

for x in prices:
  if (x > prevPrice):
    buyPrice = prevPrice

executionTime = (time.time() - startTime) * 1000
print('Execution time in milliseconds: ' + "{:.2f}".format(executionTime))