from primefac import *
import time
import random

def run_Test(e, num):
  count = 0
  arr = []
  start = time.time()
  while count<num:
  
    y = random.randint(2**(e-1), 2**(e))
    x = nextprime(y)
    print(x)
    arr.append(x)
    count = count+1

  end = time.time()
  arr.append(end)
  #print(end-start)
  return(arr)

def run_trial(e):
  t = []
  start = time.time()
  x = run_Test(e, 2)
  end = time.time()
  t.append(end-start)
  n = x[0]*x[1]
  start2 = time.time()
  y = factorint(n)
  end2 = time.time()
  t.append(end2-start2)
  ans = [end-start, end2-start2]
  print("Between 2 to the " + str(e-1) + "th and 2 to the " + str(e) + "th power \nFound primes " + str(x[0])+" and " + str(x[1])+ "\nProduct " + str(n) + "\nFactored to (" + str(y) + ")\nFinding primes took " + str(t[0]) + " seconds \nFactoring product took " + str(t[1]) + " seconds")
  return(ans)

def run_multiple_trials(e):
  count = 0
  primetime = []
  factortime = []
  while count < 10:
    x = run_trial(e)
    primetime.append(x[0])
    factortime.append(x[1])
    count += 1
  primeaverage = (primetime[0] + primetime[1] + primetime[2] + primetime[3] + primetime[4] + primetime[5] + primetime[6] + primetime[7] + primetime[8] + primetime[9])/10
  factoraverage = (factortime[0] + factortime[1] + factortime[2] + factortime[3] + factortime[4] + factortime[5] + factortime[6] + factortime[7] + factortime[8] + factortime[9])/10
  print("Average time to find two primes: " + str(primeaverage) + "\nAverage time to factor product: " + str(factoraverage))

#run_multiple_trials(34)
#run_Test(512, 2)

print(12310706237801410831157345838419752517119523730000472087147511020300699537120695178879016811109946843728898127097841356595002627628293928385572185383447451 * 8206829719119161108123356954585756426843441153238660395745345503109749135288530082636328450960753858502315934501568023449629705902076730963474453046830629)