from math import gcd as bltin_gcd

def coprime(a, b):
    return bltin_gcd(a, b) == 1

def c2i(c, alphabet):
    """Returns the index of c in the string alphabet, starting at 0"""
    # Copy your method from subcipher.py here
    if c in alphabet:
      return alphabet.index(c)
    else:
      print("Mistake")
      print("%s is not in %s" %(c, alphabet))
      return None
    

def i2c(i, alphabet):
    """Returns the character at index i in alphabet"""
    # Copy your method from subcipher.py here
    return alphabet[i]

def prepare_string(s, alphabet):
    """removes characters from s not in alphabet, returns new string"""
    # Copy your method from subcipher.py here
    toRet = ""
    for i in s:
      if i in alphabet:
        toRet += i
    return toRet #all preprepared strings are fully uppercase

def det(m):
  return m[0][0] * m[1][1] - (m[0][1] * m[1][0])

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def mod_inverse(a, m):
  for i in range(1, m):
    if (i*a) % m == 1:
      return i
  #print("Error, no modular inverse")
  return -1

def inverseMatrix(matrix, mod): #given a matrix, and a mod
  det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]) % mod
  adjMatrix = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
  if mod_inverse(det, mod) == -1:
    return -1
  inv = mod_inverse(det, mod)
  toRet = [[0, 0], [0, 0]]
  for i in range(2):
    for j in range(2):
      toRet[i][j] = (inv * adjMatrix[i][j]) % mod
  return toRet

def matrixMult(matrixA, matrixB, mod):
  if isinstance(matrixB[0], list): #2x2 multiplication
    a = (matrixA[0][0] * matrixB[0][0] + matrixA[0][1] * matrixB[1][0]) % mod
    b = (matrixA[0][0] * matrixB[0][1] + matrixA[0][1] * matrixB[1][1]) % mod
    c = (matrixA[1][0] * matrixB[0][0] + matrixA[1][1] * matrixB[1][0]) % mod
    d = (matrixA[1][0] * matrixB[0][1] + matrixA[1][1] * matrixB[1][1]) % mod
    return [[a, b], [c, d]]
  else: #2x1 multiplication
    a = (matrixA[0][0] * matrixB[0] + matrixA[0][1] * matrixB[1]) % mod
    b = (matrixA[1][0] * matrixB[0] + matrixA[1][1] * matrixB[1]) % mod
    return [ a, b ]

def hillEncode(encode, plaintext, alphabet):
  plaintext = prepare_string(plaintext, alphabet)
  if(len(plaintext) % 2 == 1):
    plaintext += 'X'
  toRet = ""
  for i in range(0, len(plaintext), 2):
    charOne = plaintext[i]
    charTwo = plaintext[i+1]
    someMatrix = [c2i(charOne, alphabet), c2i(charTwo, alphabet)]
    newMatrix = matrixMult(encode, someMatrix, len(alphabet))
    toRet += i2c(newMatrix[0], alphabet) + i2c(newMatrix[1], alphabet)
  return toRet

def hillDecode(encode, ciphertext, alphabet):
  ciphertext = prepare_string(ciphertext, alphabet)
  toRet = ""
  decode = inverseMatrix(encode, len(alphabet))
  for i in range(0, len(ciphertext), 2):
    charOne = ciphertext[i]
    charTwo = ciphertext[i+1]
    someMatrix = [c2i(charOne, alphabet), c2i(charTwo, alphabet)]
    newMatrix = matrixMult(decode, someMatrix, len(alphabet))
    toRet += i2c(newMatrix[0], alphabet) + i2c(newMatrix[1], alphabet)
  return toRet

def hillDigraphDecode(crib, ciphertext, alphabet):
  x = []
  A = []
  for i in range(0, len(crib), 2):
    for j in range(i+2, len(crib), 2):
      x = [[c2i(crib[i], alphabet), c2i(crib[j], alphabet) ], 
           [c2i(crib[i+1], alphabet), c2i(crib[j+1], alphabet)]]
      if inverseMatrix(x, len(alphabet)) != -1:
        b = [[c2i(ciphertext[i], alphabet), c2i(ciphertext[j], alphabet) ], 
             [c2i(ciphertext[i+1], alphabet), c2i(ciphertext[j+1], alphabet)]]
        A = matrixMult(b, inverseMatrix(x, len(alphabet)), len(alphabet))
        if inverseMatrix(A, len(alphabet)) != -1:
          print(A)
        else:
          A = []
  if A == []:
    return [ [ -1, -1 ], [ -1, -1 ] ]
  return hillDecode(A, ciphertext, alphabet)


##Main program
test_alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ':"
hill_m = [[27,13],[5,14]]
print(hillEncode(hill_m, "I will go in this way, and find my own way out", test_alpha))
print(hillDecode(hill_m, "CnzHbKasnOnbeznbhtmHAcv,Xlnbro?M", test_alpha))
print(hillDigraphDecode("Why won't", "JYnbMGhQXyUo?OAUuCtwWFPNckxtjsANHeJ.uyCFDSMGZvuCvKJYnbMGhQXyUo?Of", test_alpha))

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = [[1, 2], [3, 4]]
n = [[27, -24], [-23, 56]]
print(hillEncode(m, "FGGF", alpha))
print(hillEncode(n, "FGGF", alpha))