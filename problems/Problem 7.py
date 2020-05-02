# What is the 10 001st prime number?

def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if n%i == 0:
      return False
  return True

def nth_prime(n):
  num_primes = 0
  prime = 1
  while num_primes < n:
    prime += 1
    if is_prime(prime):
      num_primes += 1
  return prime

print(nth_prime(10001))