# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def difference(n):
  sum = 0
  sum_of_squares = 0
  for i in range(1,n+1):
    sum += i
    sum_of_squares += i**2
  diff = sum**2 - sum_of_squares
  print(diff)

difference(100)