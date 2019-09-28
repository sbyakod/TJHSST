from math import gcd as bltin_gcd
from PIL import Image

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
  return hillDecode(A, ciphertext, alphabet)


##Main program
'''
im = Image.open("Disco.bmp")
print(im.size)
print(im.getpixel((499, 341)))
im.putpixel((499, 341), 0)
im.save("DiscoModified.bmp")
'''

#to open an RGB file in grayscale:
'''
im = Image.open("filename").convert("L")
im.save("new filename")
'''

#Question 1:
'''
def caesarCipher(imageName, shift):
  im = Image.open(imageName)
  r, c = im.size
  for i in range(r):
    for j in range(c):
      curr = im.getpixel((i, j))
      im.putpixel((i, j), (curr + shift) % 256)
  im.save("Question1.bmp")
'''
'''
This is useless at disguising the contents of an image, because it merely changes the colors of an image, but the overall integrity of the image remains the same
'''

#Question 2:
'''
def imgHillEncode(imageName, matrix):
  im = Image.open(imageName)
  r, c = im.size #rows, columns of matrix
  for j in range(c):
    for i in range(0, r, 2):
      a, b = im.getpixel((i,j)), im.getpixel((i+1,j))
      newMatrix = matrixMult(matrix, [a, b], 256)
      im.putpixel((i,j), newMatrix[0])
      im.putpixel((i+1,j), newMatrix[1])
  im.save("Question2Encode.bmp")
'''
'''
This is much better than using the Caesar shift equivalent, because the image does look significantly different. I would say that this is more secure, because upon first glance, one can not just assume what the image is.
'''

#Question 3
'''
def imgHillDecode(imageName, matrix):
  im = Image.open(imageName)
  r, c = im.size #rows, columns of matrix
  decode = inverseMatrix(matrix, 256)
  for j in range(c):
    for i in range(0, r, 2):
      a, b = im.getpixel((i,j)), im.getpixel((i+1,j))
      newMatrix = matrixMult(decode, [a, b], 256)
      im.putpixel((i,j), newMatrix[0])
      im.putpixel((i+1,j), newMatrix[1])
  im.save("Question3Decoded.bmp")
'''

#Question 4:
def hillAugmentEncode(imageName, matrix, vector):
  im = Image.open(imageName)
  aug = matrix[:]
  toMult = 1
  r, c = im.size #rows, columns of matrix
  for j in range(c):
    for i in range(0, r, 2):
      #print(aug)
      a, b = im.getpixel((i,j)), im.getpixel((i+1,j))
      #print("I/J: %s, %s" %(i, j))
      #print("orig: %s" %(aug))
      #print("A/B: %s, %s" %(a, b))
      #print("inverse: %s" %(inverseMatrix(aug, 256)))
      newMatrix = matrixMult(aug, [a, b], 256)
      if(toMult==1):
        aug = [ [ aug[0][0] * vector[0] % 256, aug[0][1] * vector[1] % 256] , [ aug[1][0] , aug[1][1] ] ]
        toMult=2
      else:
        aug = [ [ aug[0][0], aug[0][1] ] , [ aug[1][0] * vector[0] % 256, aug[1][1] * vector[1] % 256] ]
        toMult=1
      im.putpixel((i,j), newMatrix[0])
      im.putpixel((i+1,j), newMatrix[1])
      print("new: %s" %(newMatrix))
      print("--")
  #print("---------")
  im.save("Question6Encode.bmp")

#Question 5:
def hillAugmentDecode(imageName, aug, vector):
  im = Image.open(imageName)
  toMult = 1
  matrix = aug[:]
  r, c = im.size #rows, columns of matrix
  for j in range(c):
    for i in range(0, r, 2):
      a, b = im.getpixel((i,j)), im.getpixel((i+1,j))
      inv = inverseMatrix(matrix, 256)
      newMatrix = matrixMult(inv, [a,b], 256)
      if toMult==1:
        matrix = [ [ matrix[0][0] * vector[0] % 256, matrix[0][1] * vector[1] % 256] , [ matrix[1][0] , matrix[1][1] ] ]
        toMult = 2
      else:
        matrix = [ [ matrix[0][0], matrix[0][1] ] , [ matrix[1][0] * vector[0] % 256, matrix[1][1] * vector[1] % 256] ]
        toMult=1
      im.putpixel((i,j), newMatrix[0])
      im.putpixel((i+1,j), newMatrix[1])
  im.save("Question5Decoded.bmp")

#Question 6:
def impHillAug(imageName, aug, vector, m):
  im = Image.open(imageName)
  toMult = 1
  matrix = aug[:]
  r, c = im.size #rows, columns of matrix
  for j in range(c):
    for i in range(0, r, 2):
      a, b = im.getpixel((i,j)), im.getpixel((i+1,j))
      inv = inverseMatrix(matrix, 256)
      newMatrix = matrixMult(inv, [a,b], 256)
      if toMult==1:
        matrix = [ [ matrix[0][0] * vector[0] % 256, matrix[0][1] * vector[1] % 256] , [ matrix[1][0] , matrix[1][1] ] ]
        toMult = 2
      else:
        matrix = [ [ matrix[0][0], matrix[0][1] ] , [ matrix[1][0] * vector[0] % 256, matrix[1][1] * vector[1] % 256] ]
        toMult=1
      f = mod_inverse(newMatrix[0], m)
      g = mod_inverse(newMatrix[1], m)
      im.putpixel((i,j), f)
      im.putpixel((i+1,j), g)
  im.save("Question6Encoded.bmp")

#Question 6b:
def impHillDec(imageName, aug, vector, m):
  im = Image.open(imageName)
  toMult = 1
  matrix = aug[:]
  r, c = im.size #rows, columns of matrix
  for j in range(c):
    for i in range(0, r, 2):
      a, b = mod_inverse(im.getpixel((i,j)) , m), mod_inverse(im.getpixel((i+1,j)), m)
      inv = inverseMatrix(matrix, 256)
      newMatrix = matrixMult(inv, [a,b], 256)
      if toMult==1:
        matrix = [ [ matrix[0][0] * vector[0] % 256, matrix[0][1] * vector[1] % 256] , [ matrix[1][0] , matrix[1][1] ] ]
        toMult = 2
      else:
        matrix = [ [ matrix[0][0], matrix[0][1] ] , [ matrix[1][0] * vector[0] % 256, matrix[1][1] * vector[1] % 256] ]
        toMult=1
      f = newMatrix[0]
      g = newMatrix[1]
      im.putpixel((i,j), f)
      im.putpixel((i+1,j), g)
  im.save("Question6Decoded.bmp")



#Run main methods
#caesarCipher("Disco.bmp", 53)
#imgHillEncode("SC.bmp", [[2, 5], [3, 20]])
#imgHillDecode("Question2Encode.bmp", [[2, 5], [3, 20]])
#imgHillDecode("Mystery1.bmp", [[2, 5], [3,20]])
#hillAugmentEncode("SC.bmp", [[2,5],[3,20]], [3,5])
#hillAugmentDecode("Question4Encode.bmp", [[2,5],[3,20]], [3, 5])
#hillAugmentDecode("Mystery2.bmp", [[2,5],[3,20]], [101,141])
#impHillAug("logo1.bmp", [[2,5],[3,20]], [3,5], 7)
#impHillAug("logo2.bmp", [[2,5],[3,20]], [3,5], 256)
#impHillDec("Question6Encoded.bmp", [[2,5],[3,20]], [3,5], 256)