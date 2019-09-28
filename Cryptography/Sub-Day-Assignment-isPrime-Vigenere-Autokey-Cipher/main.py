def isPrime(x):
 if x < 4:
   return True
 for i in range(2, int(x**0.5)+1):
   if x % i == 0:
     return False
 return True

def c2i(c, alphabet): #from subcipher
  if c in alphabet:
    return alphabet.index(c)
  else:
    print(c + " does not exist in string: " + alphabet)
    return None

def i2c(i, alphabet): #from subcipher
  return alphabet[i]

def autokey_decode(p, ciphertext, alphabet):
  output = ''
  for char in ciphertext:
    if len(output) != 0:
      output += i2c(c2i(char, alphabet) - c2i(output[-1], alphabet), alphabet)
    else:
      output += i2c(c2i(char, alphabet) - c2i(p, alphabet), alphabet)
  return output

print(isPrime(1)) #true
print(isPrime(2)) #true
print(isPrime(3)) #true
print(isPrime(4)) #false
print(isPrime(5)) #true
print(isPrime(31)) #true
print(isPrime(91)) #false
print(isPrime(35657)) #false
print(isPrime(181)) #true
#print(isPrime(738748793)) #true
#print(isPrime(417133782732381653)) #true
print()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(autokey_decode('P', 'VOWJVNOBTMBALTBFPWLSG', alphabet))
print()
print(autokey_decode("S", 'ABBAMHOFGQAUVTLTFPMIHTSQRGHINMXVDMXFUE', alphabet))