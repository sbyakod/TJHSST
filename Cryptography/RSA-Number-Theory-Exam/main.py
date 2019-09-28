import random

def prepare_string(s, alphabet):
  toRet = ""
  for i in s:
    if i in alphabet:
      toRet += i
  return toRet 

def c2i(c, alphabet):
    if c in alphabet:
      return alphabet.index(c)
    else:
      print("Mistake")
      print("%s is not in %s" %(c, alphabet))
      return None
    
def i2c(i, alphabet):
    return alphabet[i]

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
    
def find_d(e, m):
  green = []
  p = m%e
  q = m
  while p >1:
    green.append(m//e)
    p  = m%e
    m = e
    e = p
  for x in range (len(green)):
    green[x] = green[x]*(-1)
  red = green[len(green)-1]
  green = green[0:len(green)-1]
  blue = 1
  while len(green) > 0:
    red_old = red
    #print(red_old)
    red = blue + (red_old)*green[len(green)-1]
    #print(red)
    green = green[0:len(green)-1]
    #print(green)
    blue = red_old
    #print(blue)
  return (red%q)

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
  while count<num:
  
    x = random.randint(2**(e-1), 2**(e))
    if primality_test(x):
      arr.append(x)
      count = count+1
  return(arr)

def run_trial(p, e, alpha, plaintext):
  x = run_Test(p, 2)
  #print(x)
  #x = [10745914002293, 14627728288231]
  #x = [21106957630336313, 21570315346262729]
   #x = [2041116501031104912810800714483341548737, 2311878851983253498803073844655748835649]
  #x = [10571396892009300643226252328280166659643387812225832276428385091772366030222023366558848817281935284169965526389431306054912292543378992954947795439306011, 9604565631525187361527816975303615076516260308882492873230667868884876641813105758533614524653773326960156543965316493614518628446551334929495529784785541]
  #x = 9212195437355394949415208113719178491917850174618700981116748000868937295473721563732366745069005066238626662344187587892816905619172469258827632227598989, 7522789666320398628998470505817729017983130379530839688367784440670053965130902301722408788452469864048055815746074463270622255574915020983458567784993473
  m = (x[0])*(x[1])
  tot = (x[0]-1)*(x[1]-1)
  while gcd(e, tot) != 1:
    x = run_Test(p, 2)
    m = (x[0]*x[1])
    tot = (x[0]-1)*(x[1]-1)
  g = prepare_string(plaintext, alpha)
  l = len(alpha)
  n = 0
  while (l**(n+1))<m:
    n = n + 1
  d = find_d(e, tot)
  subs = []
  nums = []
  numsencoded = []
  numsdecoded = []
  prep = ""
  ans = ""
  for v in range (0, len(g)//n):
    s = g[0:n]
    g = g[n:len(g)]
    prep += s
    subs.append(s)
  temp = n-len(g)
  for v in range (0, temp):
    g += "Z"
  prep += g
  subs.append(g)
  for v in subs:
    v = v[::-1]
    num = 0
    count = 0
    for z in range (n):
      num = num + (c2i(v[z], alpha))*(l**count)
      count = count + 1
    nums.append(num)
  for v in nums:
    numsencoded.append(pow(v, e, m))
  for v in numsencoded:
    numsdecoded.append(pow(v, d, m))
  s = ""
  for v in numsdecoded:
    u = v
    s = ""
    for z in range (n):
      let = i2c((u%l), alpha)
      s += let
      u = u//l
    s = s[::-1] #reverse s
    ans += s
  print("Between 2 to the " + str(p-1) + "th and 2 to the " + str(p) + "th power \nFound primes " + str(x[0])+" and " + str(x[1])+ "\nThe mod is: " + str(m) + " and the totient of the mod is: " + str(tot) + "\ne is: " + str(e) + " and d is: " +  str(d) + " and if this worked, this is 1:1\nYour input is: " + str(plaintext) + "\nYour alphabet is: " + str(alpha) + "\nPrepared input is: " + str(prep) + "\nAlphabet length is " + str(l) + " and the highest power is " + str(n) + "\nBroken into substrings: " + str(subs) + "\nBecome numbers: " + str(nums) + "\nEncoded to: " + str(numsencoded) + "\nDecoded to: " + str(numsdecoded) + "\nBack to text: " + str(ans))
  return(ans)

def crack(e, m, alpha, arr, facs):
  l = len(alpha)
  n = 0
  while (l**(n+1))<m:
    n = n + 1
  #x = prime_factors(m) -- if actually cracking; we will know the factors of the mod we are receving messages in
  x = facs
  tot = (x[0]-1)*(x[1]-1)
  if gcd(e, tot) != 1:
    return("Error, your exponent is not coprime to the totient of your mod")
  d = find_d(e, tot)
  numsencoded = arr
  numsdecoded = []
  ans = ""
  for v in numsencoded:
    numsdecoded.append(pow(v, d, m))
  s = ""
  for v in numsdecoded:
    u = v
    s = ""
    for z in range (n):
      let = i2c((u%l), alpha)
      s += let
      u = u//l
    s = s[::-1] #reverse s
    ans += s
  return(ans)

def encode(e, m, alpha, plaintext):
  g = prepare_string(plaintext, alpha)
  l = len(alpha)
  n = 0
  while (l**(n+1))<m:
    n = n + 1
  subs = []
  nums = []
  numsencoded = []
  prep = ""
  ans = ""
  for v in range (0, len(g)//n):
    s = g[0:n]
    g = g[n:len(g)]
    prep += s
    subs.append(s)
  temp = n-len(g)
  for v in range (0, temp):
    g += "Z"
  prep += g
  subs.append(g)
  for v in subs:
    v = v[::-1]
    num = 0
    count = 0
    for z in range (n):
      num = num + (c2i(v[z], alpha))*(l**count)
      count = count + 1
    nums.append(num)
  for v in nums:
    numsencoded.append(pow(v, e, m))
  return(numsencoded)


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha3 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.;-, !'"
alpha4 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz., '!0123456789-?"
plaintext = "ALLWORKANDNOPLAYMAKESJACKADULLBOY"
plaintext2 = "Short strings should work"
plaintext3 = "This is a sentence with completely normal formatting and as you can see as long as you include every character in your alphabet, it will decode perfectly with no issues whatsoever, isn't that exciting!"
plaintext4 = "All of us should be able to encode using messages that start with the letter A"
plaintext5 = "All of us should be able to encode using messages that start with the letter A. Then we should say '1, 2, 3!'"
ciphertext2 = "Hello my name is Sharath Byakod!"
#facs = [9212195437355394949415208113719178491917850174618700981116748000868937295473721563732366745069005066238626662344187587892816905619172469258827632227598989, 7522789666320398628998470505817729017983130379530839688367784440670053965130902301722408788452469864048055815746074463270622255574915020983458567784993473]
facs = [2416363112414950060519635683535800218561, 2098303306428630021601794861694296487297]
#facs1 = [10745914002293, 14627728288231]
arr2 = [562365820385219521717460729334598798324672562625423015369404609051953137745318, 1955110710380344294036042834259653385330972459141503081086566115492388083041112, 4041488021136173266895254489374576963277822572265841388155671158920794390507505, 695137775045168494331371182778452452919628847549633965649914960338685277285955, 3671666461418645127323901945507450757110156824397679321364615187689726254423234, 2551322109965571461589270213863901591460577021474477302746474828215311496947745, 3323912136590043044700351895924008573314468285932679683779456723148987072664984]

arr3 = [730602677384, 2170692030797, 2519141974152, 1777958819315, 1496954342587, 2186605246622, 2241804349613, 153250334791, 514577811429]
facs3 = [12146506381645834038938637694315560145605522481099001678525961130513503330983463286913894837422547560452046476688310536561557005074571465528726771144222297, 6841181471228144056720961233011919562929461148315947269150349289240990263876119140774193696991680295609812474830147505476097737728291793488537259523362993]
#[50837210231237492016593431211323805839983064096663985728397606713013637823325213733006298708372763675277685385422451330481478253815989701364691152429516888118631215716651584133298062128550056002550598703029921897758721402032930865431018738997389089732386635867527453376972971727760206011808884494542493442209]


#print(crack(65537, facs[0]*facs[1], alpha4, arr, facs))

print(encode(65537, 14712509198209*15249998708993, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "RSA ENCRYPTION WAS NAMED AFTER RON RIVEST ADI SHAMIR AND LEONARD ADLEMAN"))

print(crack(65537, facs[0]*facs[1], alpha4, arr2, facs))
#print(prime_factors(2494279923802253606287472092668310204875649561581672691813431640440219048972006082731965879))
#print(crack(65537, 2789701478689, alpha, arr3, facs3))

print(crack(65537, facs3[0]*facs[1], "ABCDEFGHIJKLMNOPQRSTUVWXYZ., []0123456789", 51067169418462057946035271407596584206898470229948837025243238360682207489049940521332316064501444037312305552752324515016504618449765390427754168876074131879784613096721414049832244807553779598060039598331370583030202390206371995360432749375936016189125266198408794541779708034026032700137396253674599089757, facs3))
#run_trial(44, 65537, alpha, plaintext)
#run_trial(55, 65537, alpha, plaintext2.upper())
#run_trial(512, 65537, alpha4, plaintext5)
#print(facs[0] * facs[1])
#print(9212195437355394949415208113719178491917850174618700981116748000868937295473721563732366745069005066238626662344187587892816905619172469258827632227598989*7522789666320398628998470505817729017983130379530839688367784440670053965130902301722408788452469864048055815746074463270622255574915020983458567784993473)