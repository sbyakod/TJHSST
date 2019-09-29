#Name: Sharath Byakod
#Period: 4
#Date: 8/31/17

import sys

def fib(n):
   cur = 1
   old = 1
   i = 1
   while (i < n):
      cur, old, i = cur + old, cur, i+1
   return cur

arg = sys.argv[1]
arg = int(arg)

for i in range(arg):
   print(fib(i))