# Find the largest palindrome made from the product of two 3-digit numbers.

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
  print(upperN, lowerN)
  for i in range(upperN, lowerN, -1):
    for j in range(i, lowerN, -1):
      if is_palindrome(i*j) and i*j > palindrome:
        palindrome = i*j
  return palindrome

print(largest_palindrome(999))