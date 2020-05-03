# Find the sum of all the multiples of 3 or 5 below 1000.

import time

def sum_of_multiples_3_and_5(n):
  sum = 0
  multiple_of_three = False
  multiple_of_five = False

  for i in range(3,n):
    multiple_of_three = i%3 == 0
    multiple_of_five = i%5 == 0

    if(multiple_of_three or multiple_of_five):
      sum += i

  return sum

def main():
  print(sum_of_multiples_3_and_5(1000))

if __name__ == "__main__":
  startTime = time.perf_counter()
  main()
  print("Program executed in ",round(float(time.perf_counter()-startTime),2)," second(s)")