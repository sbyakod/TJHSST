from math import gcd as bltin_gcd
import re
import numpy

def c2i(c, alphabet): #from subcipher
  if c in alphabet:
    return alphabet.index(c)
  else:
    print(c + " does not exist in string: " + alphabet)
    return None

def i2c(i, alphabet): #from subcipher
  return alphabet[i]

def prepare_string(s, alphabet): #from subcipher
  """temp = s.upper()
  for char in s:
    if char not in alphabet:
      temp = temp.replace(char, "")"""
  temp = s
  return temp

def mod_inverse(a, m):
  for i in range(m):
    if (a * i) % m == 1:
      return i
  
  #print("There is no inverse of (mod " + str(m) + ")")
  return -1

def mat_inverse(matrix, alphabet):
  det = int(round(numpy.linalg.det(matrix)))
  det_inv = mod_inverse(det, len(alphabet))
  #print(det_inv)

  if det_inv == -1:
    #print("There is no inverse matrix!")
    return -1
  
  invmat = [[(matrix[1][1] * det_inv) % len(alphabet), (matrix[0][1] * -1 * det_inv) % len(alphabet)],
            [(matrix[1][0] * -1 * det_inv) % len(alphabet), (matrix[0][0] * det_inv) % len(alphabet)]]
  return invmat

def mat_mult(a, b, alphabet):
  output = numpy.dot(a, b)
  output = output.tolist()

  if len(output[0]) == 2:
    output = [[output[0][0] % len(alphabet), output[0][1] % len(alphabet)],
              [output[1][0] % len(alphabet), output[1][1] % len(alphabet)]]
  else:
    output = [[output[0][0] % len(alphabet)],
              [output[1][0] % len(alphabet)]]

  return output

def hill_encode(matrix, plaintext, alphabet):
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

def hill_decode(matrix, ciphertext, alphabet):
  output = ""
  text = prepare_string(ciphertext, alphabet)
  if len(text) % 2 != 0:
    text += "X"
  if mat_inverse(matrix, alphabet) == -1:
    return "Non-invertible encoding matrix given!"
  
  inv_mat = mat_inverse(matrix, alphabet)
  digraphs = re.findall('..', text)
  for each in digraphs:
    each_mat = [[c2i(each[0], alphabet)], [c2i(each[1], alphabet)]]
    each_mat = mat_mult(inv_mat, each_mat, alphabet)
    each_mat = [each_mat[0][0], each_mat[1][0]]
    each_mat = [i2c(each_mat[0], alphabet), i2c(each_mat[1], alphabet)]
    output += ''.join(each_mat)
  return output

def digraph_selfmap(matrix, alphabet):
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

def mat_inverse_count(alphabet):
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

def hill_crib_crack(ciphertext, crib, alphabet):
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
  
  print("No encoding matrix found... NOT POSSIBLE!")
  return -1
    
encoded_mat_zero = [[0, 0], 
                    [0, 0]]
encoded_mat = [[7, 6], [4, 13]]
encoded_mat2 = [[0], [12]] #[[1, 0], [0, 1]]
encoded_mat_Q2 = [[4, 3], [5, 6]]
encoded_mat_exam = [[27, 13], [5, 14]] 
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #26
alpha_27 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!"
alpha_new = "ABCDEFGHIJKLMNOPQRSTUVWXY" #25
alpha_exam = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ':"

#print(mat_inverse(encoded_mat, alpha))
#print(mat_inverse([[3, 2], [15, 9]], alpha))
#print(mat_inverse(encoded_mat2, alpha))
#print("-----------------------------------------------")
#print(mat_mult([[3, 2], [15, 9]], [[2], [8]], alpha))
#print(mat_mult(encoded_mat, encoded_mat2, alpha))
#print("-----------------------------------------------")
'''print(hill_encode(encoded_mat, "AMERICAN", alpha))
print(hill_decode(encoded_mat, "UAADQGAN", alpha))
print(hill_encode(encoded_mat, "VANDAL", alpha))
print(hill_decode(encoded_mat, "RGFNON", alpha))
print("-----------------------------------------------")
print(mat_inverse(encoded_mat_Q2, alpha))
print(hill_encode(encoded_mat_Q2, "Lester S. Hill had a brilliant idea for a cipher", alpha))
print(hill_decode(encoded_mat_Q2, "MVTHVEQHWAIKZRBIPGQTQBVEODDATWKFSVYR", alpha))
print("-----------------------------------------------")
print(digraph_selfmap(encoded_mat, alpha))
print("-----------------------------------------------")
#print(mat_inverse_count(alpha))  #157247
print("-----------------------------------------------")
#print(mat_inverse_count(alpha_27))  #314927
print("-----------------------------------------------")
print(hill_encode(encoded_mat, "CRYPTO", alpha_new))
print(hill_decode(encoded_mat, "QEIQRI", alpha_new))
print("-----------------------------------------------")
print(hill_crib_crack("XBDYMNLMFEMAMCYXIEUGUIWKXEFZODSO", "DEAR", alpha))
print(hill_crib_crack("GXIGBKYPCIGAKKRAUSFEVBGG", "FLEWIN", alpha))
print(hill_crib_crack("DQJIFHSMBMSMTFSTWEPPWHJWOSULQE", "ITOLDY", alpha))
print(hill_crib_crack("RMYAAMRHMYRSDPSAMRRCXCBIFBFNMRBYQAFLJSNUAC", "ILOOKATY", alpha))'''

print(hill_encode(encoded_mat_exam, "I will go in this way, and find my own way out", alpha_exam))
print(hill_decode(encoded_mat_exam, "CnzHbKasnOnbeznbhtmHAcv,Xlnbro?M", alpha_exam))
print(hill_crib_crack("JYnbMGhQXyUo?OAUuCtwWFPNckxtjsANHeJ.uyCFDSMGZvuCvKJYnbMGhQXyUo?Of!'',BAI.G'd''Z.SpvHfqz:erXy'GWFHWeoTfNXZ:yqcSfteWPBPQUowF", "Why won't", alpha_exam))

#print(mod_inverse(89,99))