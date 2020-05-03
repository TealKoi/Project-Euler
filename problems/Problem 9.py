# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import time

def pythagorean_triplet(n):
  for a in range(1,n):
    for b in range(a+1,999):
      c = (a**2 + b**2)**0.5
      if(a+b+c == 1000):
        return int(a*b*c)

def main():
  print(pythagorean_triplet(1000))

if __name__ == "__main__":
  start = time.perf_counter()
  main()
  print("Program executed in ",round(float(time.perf_counter()-start),2)," second(s)")