# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import time

sum = 0
def sum_of_fibonacci(a,b,n):
  global sum
  if b <= n:
    if b%2 == 0:
      sum += b
    sum_of_fibonacci(b,a+b,n)
  else:
    print(sum)

def main():
  sum_of_fibonacci(1,2,4000000)

if __name__ == "__main__":
  start_time = time.perf_counter()
  main()
  print("Program executed in {r:1.4f} second(s)".format(r=time.perf_counter()-start_time))