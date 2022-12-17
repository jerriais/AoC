sum = 0
for x in range(1,1001):
  if x%3==0 or x%5==0:
    sum += x
    # print(x, sum)
print ("Result:", sum)