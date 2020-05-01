# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

sum = 0
def sum_of_fibonacci(a,b,n):
  global sum
  if b <= n:
    if b%2 == 0:
      sum += b
    sum_of_fibonacci(b,a+b,n)
  else:
    print(sum)

sum_of_fibonacci(1,2,4000000)