import time
import random
from random import randrange
from random import choice

def primeGEN(n):
  r1 = choice(range(2**(n-1)+1, 2**n+1, 2))
  r2 = choice(range(2**(n-1)+1, 2**n+1, 2))

  #for i in range

  return r1, r2

def rand_prime(n):
  while True:
    p = randrange(2**(n-1)+1, 2**n+1, 2)
    if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
      return p

n = 512
#print(primeGEN(n))
start = time.perf_counter()
print(rand_prime(n))
print(rand_prime(n))
end = time.perf_counter()
print(end - start)
#print(choice(range(2**(n-1)+1, 2**n+1, 2)))
#while True:
  #randint = random.randint(2 ** (n - 1), 2 ** n)
