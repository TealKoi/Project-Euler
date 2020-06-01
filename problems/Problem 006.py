# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time

def difference(n):
  sum = 0
  sum_of_squares = 0
  for i in range(1,n+1):
    sum += i
    sum_of_squares += i**2
  diff = sum**2 - sum_of_squares
  print(diff)

def main():
  difference(100)

if __name__ == "__main__":
  start_time = time.perf_counter()
  main()
  print("Program executed in {r:1.4f} second(s)".format(r=time.perf_counter()-start_time))