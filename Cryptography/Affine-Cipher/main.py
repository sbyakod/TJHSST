from math import gcd as bltin_gcd
import re

def c2i(c, alphabet): #from subcipher
  if c in alphabet:
    return alphabet.index(c)
  else:
    print(c + " does not exist in string: " + alphabet)
    return None

def i2c(i, alphabet): #from subcipher
  return alphabet[i]

def prepare_string(s, alphabet): #from subcipher
  '''temp = s.upper()
  for char in s:
    if char not in alphabet:
      temp = temp.replace(char, "")'''
  temp = s
  return temp

def mod_inverse(a, m):
  for i in range(m):
    if (a * i) % m == 1:
      return i
  
  print("There is no inverse of (mod " + str(m) + ")")
  return -1

def affine_encode(plaintext, alphabet, a, b):
  output = ""
  text = prepare_string(plaintext, alphabet)

  for char in text:
    y = (a * c2i(char, alphabet) + b) % len(alphabet)
    output += i2c(y, alphabet)
  return output

def affine_decode(ciphertext, alphabet, a, b):
  output = ""
  text = prepare_string(ciphertext, alphabet)
  inverse = mod_inverse(a, len(alphabet))
  if inverse == -1:
    print("Cannot decode this message using Affine Cipher - no inverse!")
    return -1

  for char in text:
    y = (inverse * c2i(char, alphabet) - inverse * b) % len(alphabet)
    output += i2c(y, alphabet)
  return output

def print_Table(lower, upper):
  a = 0
  size = []
  a_vals = []
  b_vals = []
  t_vals = []

  for i in range(lower, upper + 1):
    size.append(i)
    b_vals.append(i)
    for j in range(1, i):
      if bltin_gcd(j, i) == 1:
        a += 1
    a_vals.append(a)
    t_vals.append((a * i) - 1)
    a = 0

  titles = ['Alpha Size', 'A Values', 'B Values', 'Transformations']
  data = [titles] + list(zip(size, a_vals, b_vals, t_vals))

  for i, d in enumerate(data):
    line = '|'.join(str(x).ljust(12) for x in d)
    print(line)
    if i == 0:
      print('-' * len(line))

def d2i(d, alphabet):
  chars = list(d)
  val1 = c2i(chars[0], alphabet)
  val2 = c2i(chars[1], alphabet)
  return (val1 * len(alphabet)) + val2

def i2d(i, alphabet):
  return i2c(i // len(alphabet), alphabet) + i2c(i % len(alphabet), alphabet)

def affine_encode_digraphs(plaintext, alphabet, a, b):
  output = ""
  text = prepare_string(plaintext, alphabet)
  if len(text) % 2 != 0:
    text += "X"
  
  digraphs = re.findall('..', text)
  for each in digraphs:
    y = (a * d2i(each, alphabet) + b) % (len(alphabet) * len(alphabet))
    output += i2d(y, alphabet)
  return output

def affine_decode_digraphs(ciphertext, alphabet, a, b):
  output = ""
  text = prepare_string(ciphertext, alphabet)
  inverse = mod_inverse(a, len(alphabet) * len(alphabet))
  if inverse == -1:
    print("Cannot decode this message using Affine Cipher - no inverse!")
    return -1

  digraphs = re.findall('..', text)
  for each in digraphs:
    y = (inverse * d2i(each, alphabet) - inverse * b) % (len(alphabet) * len(alphabet))
    output += i2d(y, alphabet)
  return output

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alpha_exam = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ':"

'''print(affine_encode("THISISATEST", alpha, 17, 4))
print(affine_decode("WIGZEYYPTUPUYP", alpha, 17, 4))
print("------------------------------------------")
print(affine_encode("THISISATEST", alpha2, 17, 4))
print(affine_decode("DP6W6WEDAWD", alpha2, 17, 4))
print("------------------------------------------")
print_Table(20, 60)
print("------------------------------------------")
print(affine_encode_digraphs("THISISANOTHERTEST", alpha, 81, 119))
print(affine_decode_digraphs("QFHIIRTBUUYNNUURJPXDYWFG", alpha, 81, 119))
print("------------------------------------------")'''

#print(130 % 26)
#print(237 % 26)

'''print(i2c(21, alpha))
print(i2c(0, alpha))
print(i2c(13, alpha))
print(i2c(3, alpha))
print(i2c(0, alpha))
print(i2c(11, alpha))'''

print(alpha_exam)
print(affine_encode_digraphs("YOUPASSEDTHISTESTASWELLX", alpha, 81, 119))
print(affine_decode_digraphs("QFHIIRTBUUYNNUURJPXDYWFG", alpha, 81, 119))

print(affine_encode_digraphs("I'm playing time against my troubles", alpha_exam, 137, 241))
print(affine_decode_digraphs("qsd'TzOMjzHEuTUL'nbg'TuTULoJYBKzWEuTfbTzoqZ!WE", alpha_exam, 91, 1091))