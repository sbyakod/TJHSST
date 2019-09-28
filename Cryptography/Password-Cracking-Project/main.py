from math import gcd as bltin_gcd
import re
import numpy
from collections import Counter

def c2i(c, alphabet): #from subcipher
  if c in alphabet:
    return alphabet.index(c)
  else:
    print(c + " does not exist in string: " + alphabet)
    return None

def i2c(i, alphabet): #from subcipher
  return alphabet[i]

def prepare_string(s, alphabet): #from subcipher
  temp = s.upper()
  for char in s:
    if char not in alphabet:
      temp = temp.replace(char, "")
  return temp

def mod_inverse(a, m): #from hillcipher
  for i in range(m):
    if (a * i) % m == 1:
      return i
  
  #print("There is no inverse of (mod " + str(m) + ")")
  return -1

def mat_inverse(matrix, alphabet): #from hillcipher
  det = int(round(numpy.linalg.det(matrix)))
  det_inv = mod_inverse(det, len(alphabet))

  if det_inv == -1:
    #print("There is no inverse matrix!")
    return -1
  
  invmat = [[(matrix[1][1] * det_inv) % len(alphabet), (matrix[0][1] * -1 * det_inv) % len(alphabet)],
            [(matrix[1][0] * -1 * det_inv) % len(alphabet), (matrix[0][0] * det_inv) % len(alphabet)]]
  return invmat

def mat_mult(a, b, alphabet): #from hillcipher
  output = numpy.dot(a, b)
  output = output.tolist()

  if len(output[0]) == 2:
    output = [[output[0][0] % len(alphabet), output[0][1] % len(alphabet)],
              [output[1][0] % len(alphabet), output[1][1] % len(alphabet)]]
  else:
    output = [[output[0][0] % len(alphabet)],
              [output[1][0] % len(alphabet)]]

  return output

def hill_encode(matrix, plaintext, alphabet): #from hillcipher
  output = ""
  text = prepare_string(plaintext, alphabet)
  if len(text) % 2 != 0:
    text += "X"
  if mat_inverse(matrix, alphabet) == -1:
    return "Non-invertible encoding matrix given!"

  digraphs = re.findall('..', text)
  for each in digraphs:
    each_mat = [[c2i(each[0], alphabet)], [c2i(each[1], alphabet)]]
    each_mat = mat_mult(matrix, each_mat, alphabet)
    each_mat = [each_mat[0][0], each_mat[1][0]]
    each_mat = [i2c(each_mat[0], alphabet), i2c(each_mat[1], alphabet)]
    output += ''.join(each_mat)
  return output

def hill_decode(matrix, ciphertext, alphabet): #from hillcipher #edited
  output = ""
  text = prepare_string(ciphertext, alphabet)
  if len(text) % 2 != 0:
    text += "X"
  if mat_inverse(matrix, alphabet) == -1:
    return -1
  
  inv_mat = mat_inverse(matrix, alphabet)
  digraphs = re.findall('..', text)
  for each in digraphs:
    each_mat = [[c2i(each[0], alphabet)], [c2i(each[1], alphabet)]]
    each_mat = mat_mult(inv_mat, each_mat, alphabet)
    each_mat = [each_mat[0][0], each_mat[1][0]]
    each_mat = [i2c(each_mat[0], alphabet), i2c(each_mat[1], alphabet)]
    output += ''.join(each_mat)
  return output

def digraph_selfmap(matrix, alphabet): #from hillcipher
  output = 0

  for i in alphabet:
    for j in alphabet:
      temp_mat = [[c2i(i, alphabet)], [c2i(j, alphabet)]]
      each_mat = mat_mult(matrix, temp_mat, alphabet)
      each_mat = [each_mat[0][0], each_mat[1][0]]
      each_mat = [i2c(each_mat[0], alphabet), i2c(each_mat[1], alphabet)]
      temp_mat = [i, j]

      if temp_mat == each_mat:
        output += 1
        print(temp_mat)

  return output

def mat_inverse_count(alphabet): #from hillcipher
  output = 0
  loop = len(alphabet)

  for a in range(loop):
    for b in range(loop):
      for c in range(loop):
        for d in range(loop):
          cur_mat = [[a, b],
                     [c, d]]
          if mat_inverse(cur_mat, alphabet) != -1:
            output += 1
  
  if output > 0:
    output = output - 1
  
  return output

def hill_crib_crack(ciphertext, crib, alphabet): #from hillcipher
  text = prepare_string(ciphertext, alphabet)
  ctext = prepare_string(crib, alphabet)
  if len(text) % 2 != 0:
    text += "X"

  cipherDG = re.findall('..', text)
  cribDG = re.findall('..', ctext)
  for i in range(len(cribDG)):
    for j in range(i + 1, len(cribDG)):
      crib_mat = [[c2i(cribDG[i][0], alphabet), c2i(cribDG[j][0], alphabet)],
                  [c2i(cribDG[i][1], alphabet), c2i(cribDG[j][1], alphabet)]]
      if mat_inverse(crib_mat, alphabet) != -1:
        crib_mat = mat_inverse(crib_mat, alphabet)
        cipher_mat = [[c2i(cipherDG[i][0], alphabet), c2i(cipherDG[j][0], alphabet)],
                      [c2i(cipherDG[i][1], alphabet), c2i(cipherDG[j][1], alphabet)]]
        encoded_mat = mat_mult(cipher_mat, crib_mat, alphabet)
        plaintext = hill_decode(encoded_mat, ciphertext, alphabet)
        return encoded_mat, plaintext
  
  #print("No encoding matrix found... NOT POSSIBLE!")
  return -1

def crack_passwords(alphabet, user_pass, words):
  alpha_len = len(alphabet)
  pass_list = []
  for i in range(len(user_pass)):
    pass_list.append(user_pass[i][1])
  passwords_len = len(pass_list)

  #pass_list = ["!3!VDCH#Y6", ">U??%\"1R@YX$", "\\?HE8IN$PK"]

  for i in range(len(pass_list)):
    for j in range(len(words)):
      temp = hill_crib_crack(pass_list[i], words[j], alphabet)
      if temp != -1:
        for each in words:
          if str(each) in str(temp[1]):
            print(temp, user_pass[i])
        #print(temp[1])
        #print(hill_crib_crack(pass_list[i], words[j], alphabet))
  return -1

  '''for a in range(alpha_len):
    for b in range(alpha_len):
      for c in range(alpha_len):
        print(c)
        for d in range(alpha_len):
          for e in range(passwords_len):
            cur_mat = [[a, b],
                       [c, d]]
            det = int(round(numpy.linalg.det(cur_mat)))
            if det == 0:
              break
            if mod_inverse(det, len(alphabet)) == -1:
              break
            plain_pass = hill_decode(cur_mat, pass_list[e], alphabet)
            if plain_pass != -1:
              if plain_pass in words:
                return(cur_mat, user_pass[e], pass_list[e])
              #####for f in range(passwords_len):
                if plain_pass in pass_list[f]:
                  return(cur_mat, user_pass[f], pass_list[f])'''


infile = open("TJ' 18 User - Pass.txt","r")
user_pass = []
for line in infile.readlines():
      line = line.strip()
      user_pass.append(line.split())
infile.close()
#print(user_pass)

infile = open("1000 Common Passwords.txt","r")
commonWords = []
for line in infile.readlines():
      line = line.strip()
      if len(line) >= 6:
        #if not any(c.isdigit() for c in line):
        commonWords.append(line.upper())
infile.close()
#print(commonWords)

alpha = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]"

print(crack_passwords(alpha, user_pass, commonWords))
'''for i in range(len(user_pass)):
  print(hill_decode([[60, 2], [11, 6]], user_pass[i][1], alpha), user_pass[i])'''

#print(hill_decode([[60, 2], [11, 6]], "8B&\\&E<O", alpha))
#print("8B&\\&E<O")