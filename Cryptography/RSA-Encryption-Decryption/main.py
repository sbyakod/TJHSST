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
  m = (x[0])*(x[1])
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
  d = find_d(e, tot)
  print("d = " + str(d))
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
plaintext = "Testing 1, 2, 3!"
plaintext2 = "This is a larger test, but nothing quite special yet... BOO!"
ciphertext2 = "Hello Danny, this is Sharath. If this decrypts correctly, then you should be able to read it in plain old English!"
ciphertext3 = "Hello Mr. Eckel, I hope you are receiving this. This summer, I hope to gain an internship at Capital One (now that I am finally a senior) or another firm in the local community or elsewhere. Additionally, I hope to visit my campus-to-be and get situated with life as a college student including exploring campus, the regional area, hotspots, etc. Aside from that, I plan to enjoy this summer by accomplishing tasks off my bucket list, playing games, watching movies, playing basketball, and living a healthy lifestyle." 

facs = [12310706237801410831157345838419752517119523730000472087147511020300699537120695178879016811109946843728898127097841356595002627628293928385572185383447451, 8206829719119161108123356954585756426843441153238660395745345503109749135288530082636328450960753858502315934501568023449629705902076730963474453046830629]
#facs1 = [10745914002293, 14627728288231]
arr = [21898369312040184916080364670224934053001145013739397733242323545916938096750412032058540796669965270998685392802786997211175496217935275540062046654941280346978721204129620457043606762834355400983417991931951479308096376681930177799659520560944285274656296887412621075275824654353583635128523325466560415797] #Danny Mittal
print(crack(65537, 101031869815734257026348135820803164201374845551481402969912143769555593700903957630074669267553336224974447927690871360486059886644963222804946990938960307476807710952236517984797000784176933487154666363542366565368549343708897179823666463561225934503271876246413748825749728782144992424158072880753318776679, alpha3, arr, facs)) #Danny Mittal
print(encode(65537, 58046628629322702632560120164621017424400800642192258026683403343931051985190098917238691929799069556867850477957498413867003745022777646254370710490349720212228122861195196152260066999068379975984686509205582982634814106428081568411429354470535255136769641383962874570149014566253865429080793902465647623297, alpha3, ciphertext2)) #Danny Mittal
print(encode(65537, 147690143426417720543026043890448472042375285573365468767128662033037446713246419100204917883446300400801225405192554010954725249626347314234029446068634707387105420955618605845881594400970904496218962357799602434736918859856803813645781043520129383769019885018939343481635017846708963422603112278784470086259, alpha3, ciphertext3))
#run_trial(44, 65537, alpha, plaintext)
#run_trial(55, 65537, alpha, plaintext2.upper())
#run_trial(512, 65537, alpha3, plaintext3)
#print(9212195437355394949415208113719178491917850174618700981116748000868937295473721563732366745069005066238626662344187587892816905619172469258827632227598989*7522789666320398628998470505817729017983130379530839688367784440670053965130902301722408788452469864048055815746074463270622255574915020983458567784993473)