# Find the sum of all the primes below two million.

import time

def is_prime(n):
  if(n<2): return False
  for i in range(2,int(n**0.5)+1):
    if(n%i == 0):
      return False
  return True

def sum_primes(maxN):
  sum = 0
  for i in range(2,maxN):
    if(is_prime(i)):
      sum += i
  return sum

def main():
  print(sum_primes(2000000))

if __name__ == "__main__":
  start_time = time.perf_counter()
  main()
  print("Program executed in {r:1.4f} second(s)".format(r=time.perf_counter()-start_time))