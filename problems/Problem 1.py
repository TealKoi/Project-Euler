# Find the sum of all the multiples of 3 or 5 below 1000.

maxN, sum = 1000, 0

for i in range(3, maxN):
  if(i%3 == 0 or i%5 == 0):
    sum += i

print(sum)