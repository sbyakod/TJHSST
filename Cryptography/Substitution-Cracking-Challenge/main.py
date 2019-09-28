def c2i(c, alphabet):
  if c in alphabet:
    return alphabet.index(c)
  else:
    print(c + " does not exist in string: " + alphabet)
    return None

def i2c(i, alphabet):
  return alphabet[i]

def prepare_string(s, alphabet):
  temp = s
  for char in s:
    if char not in alphabet:
      temp = temp.replace(char, "")
  return temp

def subst_validate(alpha1, alpha2):
  if sorted(alpha1) == sorted(alpha2):
    return True
  else:
    return False

def substitution_cipher_encode(plaintext, alpha1, alpha2):
  output = ""
  text = prepare_string(plaintext, alpha2)
  if subst_validate(alpha1, alpha2) == True:
    for char in text:
      alphaIndex = c2i(char, alpha1)
      output += i2c(alphaIndex, alpha2)
    return output
  else:
    print("Alphabets do not validate! Please check them again.")
    return None 

def substitution_cipher_decode(ciphertext, alpha1, alpha2):
  output = ""
  text = prepare_string(ciphertext, alpha1)
  if subst_validate(alpha1, alpha2) == True:
    for char in text:
      alphaIndex = c2i(char, alpha2)
      output += i2c(alphaIndex, alpha1)
    return output
  else:
    print("Alphabets do not validate! Please check them again.")
    return None 

from collections import Counter

def frequent_letters(text):
  """ return a list of tuples of most common letters in 'text'"""
  text = prepare_string(text, alphabet)
  letters = []
  for index in range(len(text) - 1):
    letters.append(text[index:index + 1])
  c = Counter(letters)
  return c.most_common(5)

def frequent_bigraphs(text):
  text = prepare_string(text, alphabet)
  bigraphs = []
  for index in range(len(text) - 1):
    bigraphs.append(text[index:index + 2])
  c = Counter(bigraphs)
  return c.most_common(5)

def frequent_trigraphs(text):
  text = prepare_string(text, alphabet)
  trigraphs = []
  for index in range(len(text) - 1):
    trigraphs.append(text[index:index + 3])
  c = Counter(trigraphs)
  return c.most_common(5)

def frequent_double_letters(text):
  """ return a list of tuples of most common double letters in 'text'"""
  text = prepare_string(text, alphabet)
  doubles = []
  for index in range(len(text) - 1):
    if text[index] == text[index + 1]:
      doubles.append(text[index:index + 2])
  c = Counter(doubles)
  return c.most_common(5)

def upper_chars(plaintext, alphabet):
  uppers = []
  count = 0
  for index in plaintext:
    if index in alphabet:
      uppers.append(count)
    count += 1
  return uppers

def caesar_shift_encode_2(plaintext, shift, alphabet):
  output = ""
  text = plaintext
  uppers = upper_chars(plaintext, alphabet)
  text = text.upper()
  for char in text:
    if char in alphabet:
      alphaIndex = c2i(char, alphabet)
      newIndex = alphaIndex + shift
      output += i2c(newIndex - len(alphabet), alphabet)
    else:
      output += char
  output = output.lower()
  output = "".join(c.upper() if i in uppers else c for i, c in enumerate(output))
  return output

def caesar_shift_decode_2(ciphertext, shift, alphabet):
  output = ""
  text = ciphertext
  uppers = upper_chars(ciphertext, alphabet)
  text = text.upper()
  for char in text:
    if char in alphabet:
      alphaIndex = c2i(char, alphabet)
      output += i2c(alphaIndex - shift, alphabet)
    else:
      output += char
  output = output.lower()
  output = "".join(c.upper() if i in uppers else c for i, c in enumerate(output))
  return output

def substitution_cipher_encode_2(plaintext, alpha1, alpha2):
  output = ""
  text = plaintext
  uppers = upper_chars(plaintext, alpha1)
  text = text.upper()
  if subst_validate(alpha1, alpha2) == True:
    for char in text:
      if char in alpha1:
        alphaIndex = c2i(char, alpha1)
        output += i2c(alphaIndex, alpha2)
      else:
        output += char
    output = output.lower()
    output = "".join(c.upper() if i in uppers else c for i, c in enumerate(output))
    return output
  else:
    print("Alphabets do not validate! Please check them again.")
    return None 

def substitution_cipher_decode_2(ciphertext, alpha1, alpha2):
  output = ""
  text = ciphertext
  uppers = upper_chars(ciphertext, alpha1)
  text = text.upper()
  if subst_validate(alpha1, alpha2) == True:
    for char in text:
      if char in alpha2:
        alphaIndex = c2i(char, alpha2)
        output += i2c(alphaIndex, alpha1)
      else:
        output += char
    output = output.lower()
    output = "".join(c.upper() if i in uppers else c for i, c in enumerate(output))
    return output
  else:
    print("Alphabets do not validate! Please check them again.")
    return None 

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = "STHTGHTCTITGHTUSKSTHHTOBTGUKTETIWSTBITSQTWKTESTKWSSTYTGUTGETHHTHHTCTETETWHSTESTUSBTUSKHTGSTHWBTGTWTWTGUTGHTIMOTYTGTHITUTKHTGHTIMTBBTWTKTFTHJFTUTIYTRTCTWGTW"
#message = "aEuHjRhEfl jlEbl, EbeEjR HER RhERioEs: 'jEHEhHj - sEjRoEs, iEhRoEs, jEhdsEj oEbrEj!'"

message = message.upper()
print("Most common letters: " + str(frequent_letters(message)))
print("Most common bigraphs: " + str(frequent_bigraphs(message)))
print("Most common trigraphs: " + str(frequent_trigraphs(message)))
print("Most common frequent double letters: " + str(frequent_double_letters(message)))
message = message.lower()
message = message.replace("t","A")
#message = message.replace("","")
#message = message.replace("","") 
#message = message.replace("x","L") 
#message = message.replace("s","S") 
#message = message.replace("o","E") 



print()
print(message)

#e t a o i n s r h l d c u m f p g w y b v k x j q z
'''
TH :  2.71        EN :  1.13        NG :  0.89
HE :  2.33        AT :  1.12        AL :  0.88
IN :  2.03        ED :  1.08        IT :  0.88
ER :  1.78        ND :  1.07        AS :  0.87
AN :  1.61        TO :  1.07        IS :  0.86
RE :  1.41        OR :  1.06        HA :  0.83
ES :  1.32        EA :  1.00        ET :  0.76
ON :  1.32        TI :  0.99        SE :  0.73
ST :  1.25        AR :  0.98        OU :  0.72
NT :  1.17        TE :  0.98        OF :  0.71
'''
'''
THE :  1.81        ERE :  0.31        HES :  0.24
AND :  0.73        TIO :  0.31        VER :  0.24
ING :  0.72        TER :  0.30        HIS :  0.24
ENT :  0.42        EST :  0.28        OFT :  0.22
ION :  0.42        ERS :  0.28        ITH :  0.21
HER :  0.36        ATI :  0.26        FTH :  0.21
FOR :  0.34        HAT :  0.26        STH :  0.21
THA :  0.33        ATE :  0.25        OTH :  0.21
NTH :  0.33        ALL :  0.25        RES :  0.21
INT :  0.32        ETH :  0.24        ONT :  0.20
'''

#Affine Ciphers: Solving with Cribs (10/18/18)
cipher = "Rta linawrun’c wgr up Rirsfiw najbswal rta fietr cmo kirt s wunnawr ufa"
print(frequent_letters(prepare_string(cipher.upper(), alphabet)))
print(frequent_bigraphs(prepare_string(cipher.upper(), alphabet)))
print(frequent_trigraphs(prepare_string(cipher.upper(), alphabet)))