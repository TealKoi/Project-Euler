# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

def smallest_multiple(n):
  for i in range(n, factorial(n)+1,n):
    if is_multiple(i,n):
      return i
  return -1

def is_multiple(x,n):
  for i in range(1,n):
    if x%i != 0:
      return False
  return True

def factorial(n):
  if n>1:
    return n*factorial(n-1)
  elif n>=0:
    return 1
  else:
    return -1

def main():
  print(smallest_multiple(20))

if __name__ == "__main__":
  start = time.perf_counter()
  main()
  print("Program executed in ",round(float(time.perf_counter()-start),2)," second(s)")