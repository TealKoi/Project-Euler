# What is the largest prime factor of the number 600851475143 ?

import time

goal = 600851475143
def prime_factorization(n):
  prime_factor = 1
  i = 2

  while i <= n/i:
    if n%i ==0:
      prime_factor = i
      n /= i
    else:
      i += 1
    if prime_factor < n:
      prime_factor = n

  return int(prime_factor)

def main():
  print(prime_factorization(goal))

if __name__ == "__main__":
  start = time.perf_counter()
  main()
  print("Program executed in ",round(float(time.perf_counter()-start),2)," second(s)")