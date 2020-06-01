#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner

#How many such routes are there through a 20×20 grid?

import time
from math import factorial

def find_paths(n):
  r = n
  n = n*2
  return factorial(n)/(factorial(r)*factorial(n-r))

def main():
    print(int(find_paths(20)))

if __name__ == "__main__":
  start_time = time.perf_counter()
  main()
  print("Program executed in {r:1.4f} second(s)".format(r=time.perf_counter()-start_time))
