#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although #it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

import time

sequenceList = {}

def sequencer(n):
  global sequenceList
  count = 1
  while n != 1:
    if(n%2 == 0):
      n = int(n/2)
    else:
      n = int((3*n)+1)
    count += 1
  return count

def main(n=1000000):
  maxV = 0
  for i in range(1,n+1):
    t = sequencer(i)
    if(t>maxV):
      maxV = t
  print(maxV)

if __name__ == "__main__":
  start_time = time.perf_counter()
  main()
  print("Program executed in {r:1.4f} second(s)".format(r=time.perf_counter()-start_time))