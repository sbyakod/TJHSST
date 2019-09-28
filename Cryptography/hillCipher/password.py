import re
def gcd(a, b):
  if b == 0:
   return a; 
  return gcd(b, a % b)

def det(M):
  return M[0][0] * M[1][1] - M[0][1] * M[1][0]

def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return -1

def invmatrix(M, N):
  modinv = mod_inverse(det(M), N)
  if modinv == -1:
    return -1
  newM = [[modinv*M[1][1], modinv*-1*M[0][1]], 
          [modinv*-1*M[1][0], modinv*M[0][0]] ]
  for i in range(2):
    for j in range(2):
      newM[i][j] %= N
  return newM

def matrixmultiplytwotwo(A, B):
  retM = [
          [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
          [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
         ]
  return retM

def matrixmultiplytwoone(A, B):
  retM = [
          [A[0][0]*B[0] + A[0][1]*B[1]],
          [A[1][0]*B[0] + A[1][1]*B[1]]
         ]
  return retM

def decode(ciphertext, alphabet, M):
  invM = invmatrix(M, N)
  if invM == -1:
    return None
  if gcd(det(invM), N) != 1:
    return None
  decoded = ""
  for i in range(0, len(ciphertext), 2):
    f = alphabet.find(ciphertext[i])
    s = alphabet.find(ciphertext[i+1])
    B = [f, s]
    multiplied = matrixmultiplytwoone(invM, B)
    decoded += alphabet[multiplied[0][0] % N] + alphabet[multiplied[1][0] % N]
  return decoded

def didecode(crib, ciphertext):
  if len(crib) % 2 == 1:
    crib = crib[:-1]
  for i in range(0, len(crib), 2):
    for j in range(i+2, len(crib), 2):
      a = alphabet.find(crib[i])
      b = alphabet.find(crib[j])
      c = alphabet.find(crib[i+1])
      d = alphabet.find(crib[j+1])

      x = alphabet.find(ciphertext[i])
      y = alphabet.find(ciphertext[j])
      z = alphabet.find(ciphertext[i+1])
      w = alphabet.find(ciphertext[j+1])

      m = [ [a, b], [c, d] ]
      mp = [ [x, y], [z, w] ]

      if gcd(det(m), N) == 1:
        invM = invmatrix(m, N)
        ans = matrixmultiplytwotwo(mp, invM)
        for a in range(2):
          for b in range(2):
            ans[a][b] %= N
        return ans
  #print("ERROR")
  return [ [-1, -1], [-1, -1] ]

def solve(alphabet, users, common):
  lazy = []
  possible = []
  retValue = False
  for c in common:
    for user in users:
      userid = user[0]
      password = user[1]

      c = c.upper()

      if len(c) >= 6 and len(password) >= 6 and len(c) < len(password):
        if bool(re.match('^[a-zA-Z]+$', c)):
          matrix = didecode(c, password)
          if matrix != [[-1, -1], [-1, -1]]:
            decoded = decode(password, alphabet, matrix)
            evaluation = True
            if decoded != None:
              for i in range(len(c)):
                if c[i] != decoded[i]:
                  evaluation = False
                  break
              if evaluation:
                print("{} {} {}".format(userid, decoded, matrix))
                possible.append(matrix)
                lazy.append((userid, decoded, matrix))
                retValue = True
  return (retValue, lazy)

text = open("passwords.txt", "r")
commonwords = open("common.txt", "r")
users = [] #store in (userid, password) format
common = []
for line in text.readlines():
  line = line.strip()
  (u, p) = line.split()
  users.append((u, p))

for line in commonwords.readlines():
  line = line.strip()
  common.append(line)

alphabet = ""
for ascii in range(33, 94):
  alphabet += chr(ascii)
N = len(alphabet)

(test, lazy) = solve(alphabet, users, common)
if test:
  print(lazy)