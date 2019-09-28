import time
import random

def isPrime(a):
  for i in range(1, a):
    if gcd(i, a) != 1:
      #print("Nope")
      return False  
  #print("Yes")
  print(a)
  return True

def isSquare(a):
  if (a**(0.5)).is_integer():
    return True
  return False
   
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def test (n, r, d):
  a = random.randint(2, n-1)
  if (pow(a, d, n) - 1) == 0:
     return True
  for s in range (0, r):
    if (pow(a, d*(2**s), n)) == n-1:
      return True
  return False

def primality_test(n):
  #n = random.randrange(2**(p-1)+1, 2**p+1, 2)
  #if condition == "prime":
  #print(n)
  if n%2 == 0:
    return False
  q = n-1
  r = 0
  while q%2==0:
    q = q//2
    r = r +1
  d = q
  count = 0
  while count < 10:
    if not test(n, r, d):
      return False
    count = count + 1
  return True
    
def prime_factors(n):
  x = (int)((n)**(0.5)) + 1
  while True:
    if(x**2 - n) < 0:
      continue
    if isSquare( (x**2) - n):
      y = (int)((x**2 - n)**(0.5))
      return (x-y, x+y)
    x += 1

def run_Test(e, num):
  count = 0
  arr = []
  start = time.perf_counter()
  while count<num:
  
    x = random.randint(2**(e-1), 2**(e))
    if primality_test(x):
      arr.append(x)
      count = count+1

  end = time.perf_counter()
  arr.append(end)
  #print(end-start)
  return(arr)

def run_trial(e):
  t = []
  start = time.perf_counter()
  x = run_Test(e, 2)
  end = time.perf_counter()
  t.append(end-start)
  n = x[0]*x[1]
  start2 = time.perf_counter()
  y = prime_factors(n)
  end2 = time.perf_counter()
  t.append(end2-start2)
  ans = [end-start, end2-start2]
  print("Between 2 to the " + str(e-1) + "th and 2 to the " + str(e) + "th power \nFound primes " + str(x[0])+" and " + str(x[1])+ "\nProduct " + str(n) + "\nFactored to (" + str(y[0]) + "," + str(y[1]) + ")\nFinding primes took " + str(t[0]) + " seconds \nFactoring product took " + str(t[1]) + " seconds")
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

#print(prime_factors(987263))
#run_trial(25)
#run_multiple_trials(25)
print(primality_test(12310706237801410831157345838419752517119523730000472087147511020300699537120695178879016811109946843728898127097841356595002627628293928385572185383447451))
print(primality_test(8206829719119161108123356954585756426843441153238660395745345503109749135288530082636328450960753858502315934501568023449629705902076730963474453046830629))
print(primality_test(101031869815734257026348135820803164201374845551481402969912143769555593700903957630074669267553336224974447927690871360486059886644963222804946990938960307476807710952236517984797000784176933487154666363542366565368549343708897179823666463561225934503271876246413748825749728782144992424158072880753318776679))