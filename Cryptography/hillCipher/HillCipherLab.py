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
    return alphabet[i].lower()

def prepare_string(s, alphabet):
    """removes characters from s not in alphabet, returns new string"""
    # Copy your method from subcipher.py here
    toRet = ""
    for i in s.upper():
      if i in alphabet:
        toRet += i
    return toRet.upper() #all preprepared strings are fully uppercase

def det(m):
  return m[0][0] * m[1][1] - (m[0][1] * m[1][0])

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def mod_inverse(a, m):
  for i in range(0, m):
    if (i*a) % m == 1:
      return i
  #print("Error, no modular inverse")
  return -1

def inverseMatrix(matrix, mod): #given a matrix, and a mod
  det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]) % 26
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
    return [ (matrixA[0][0] * matrixB[0] + matrixA[0][1] * matrixB[1]) % mod, (matrixA[1][0] * matrixB[0] + matrixA[1][1] * matrixB[1]) % mod ]

def hillEncode(encode, plaintext, alphabet):
  plaintext = prepare_string(plaintext.upper(), alphabet.upper())
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
  ciphertext = prepare_string(ciphertext.upper(), alphabet.upper())
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
          break
        else:
          A = []
  if A == []:
    return [ [ -1, -1 ], [ -1, -1 ] ]
  print(A)
  return hillDecode(A, ciphertext, alphabet)
###Individual Tests###
#exampleMatrix = [[5, 3], [7, 8]]
#print(inverseMatrix(exampleMatrix, 26))

'''#HW Problems:
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encodeM = [[7, 6], [4, 13]]
#print(hillEncode(encodeM, "AMERICAN", alpha))
#print(hillDecode(encodeM, "RGFNON", alpha))

##Problem Set
#Question 2:
encodeM = [[4, 3], [5, 6]]
plaintxt = "Lester S. Hill had a brilliant idea for a cipher"
ciphertxt = "MVTHVEQHWAIKZRBIPGQTQBVEODDATWKFSVYR"
print(inverseMatrix(encodeM, len(alpha)))
print(hillEncode(encodeM, plaintxt, alpha)) #ebzwpspcncntjsdgodzrgofxpgqukfqhggdnps
print(hillDecode(encodeM, ciphertxt, alpha)) #buthetragicallydidnotgetrichoffofita

#Question 3:
listOfDigraphs = []
encodeM = [[7, 6], [4, 13]]
for i in alpha:
  for j in alpha:
    origMatrix = [c2i(i, alpha), c2i(j, alpha)]
    newMatrix = matrixMult(encodeM, origMatrix, len(alpha))
    if newMatrix == origMatrix:
      listOfDigraphs.append((i, j))
print(listOfDigraphs)

#Question 4:
invert_count = 0
#apply Chinese remainder theorem
invert_count = (13**2 - 1) * (13**2 - 13) * (2**2 - 1) * (2**2 - 2)
'''
'''for i in range(26):
  for j in range(26):
    for k in range(26):
      for l in range(26):
        if(inverseMatrix([[i, j], [k, l]],len(alpha))) != -1:
          invert_count += 1'''
          '''
print("Inverse count for mod 26: %s" %(invert_count))

#Question 5:
invert_count = 0
for i in range(27):
  for j in range(27):
    for k in range(27):
      for l in range(27):
        if gcd(det([ [ i, j ], [ k, l ] ]), 27) == 1: #uses Euclidean algorithm
          invert_count += 1
[print("Inverse count for mod 27: %s" %(invert_count))]

#Question 6:
encodeM = [[4, 3], [5, 6]]
encodeM_exam = [[27, 13], [5, 14]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVW"  #mod 23
plaintxt = "Hello World"
ciphertxt = "ohzrsudqbv"
print(inverseMatrix(encodeM, len(alpha)))
print(hillEncode(encodeM, plaintxt, alpha)) #ebzwpspcncntjsdgodzrgofxpgqukfqhggdnps
print(hillDecode(encodeM, ciphertxt, alpha)) #buthetragicallydidnotgetrichoffofita

#Question 8:
cipherOne = "XBDYMNLMFEMAMCYXIEUGUIWKXEFZODSO" #(crib: “DEAR”)
print(hillDigraphDecode("DEAR", cipherOne, alpha))
cipherTwo = "GXIGBKYPCIGAKKRAUSFEVBGG" #(crib: “FLEWIN”)
print(hillDigraphDecode("FLEWIN", cipherTwo, alpha))
cipherThree = "DQJIFHSMBMSMTFSTWEPPWHJWOSULQE" #(crib: “ITOLDY”)
print(hillDigraphDecode("ITOLDY", cipherThree, alpha))
cipherFour = "RMYAAMRHMYRSDPSAMRRCXCBIFBFNMRBYQAFLJSNUAC" #(crib: “ILOOKATY”)
print(hillDigraphDecode("ILOOKATY", cipherFour, alpha))'''


alpha_exam ="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ':"
print(hillEncode(encodeM_exam, "I will go in this way, and find my own way out", alpha_exam))