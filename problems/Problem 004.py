# Find the largest palindrome made from the product of two 3-digit numbers.

import time

def is_palindrome(n):
  s = str(n)
  reverse = ""
  for i in range(len(s)-1,-1,-1):
    reverse += s[i]
  return reverse == s

def largest_palindrome(maxN):
  palindrome = -1
  upperN = maxN
  lowerN = round(maxN/10)-1
  for i in range(upperN, lowerN, -1):
    for j in range(i, lowerN, -1):
      if is_palindrome(i*j) and i*j > palindrome:
        palindrome = i*j
  return palindrome

def main():
  print(largest_palindrome(999))

if __name__ == "__main__":
  start_time = time.perf_counter()
  main()
  print("Program executed in {r:1.4f} second(s)".format(r=time.perf_counter()-start_time))