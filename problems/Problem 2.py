# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

c, n1, n2, maxN, sum = 0, 1, 2, 4000000, 0

while n1 < maxN:
  if(n1%2 == 0):
    sum += n1
  n = n1 + n2
  n1 = n2
  n2 = n

print(sum)