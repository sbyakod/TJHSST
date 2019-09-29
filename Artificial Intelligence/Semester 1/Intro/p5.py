#Name: Sharath Byakod
#Period: 4
#Date: 8/31/17

import sys

def isPrime(x):
   if(x < 2):
      return(False)
   else:
      if(x == 2):
         return(True)
      else:
         for i in range(2, x):
            if(x % i == 0):
               return(False)
         return(True)
  
arg = sys.argv[1]

if(isPrime(int(arg)) == True):
   print("Prime number!")
else:
   print("Not a prime number.")