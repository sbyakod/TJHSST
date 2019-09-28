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

def caesar_shift_encode(plaintext, shift, alphabet):
  output = ""
  text = prepare_string(plaintext, alphabet)
  for char in text:
    alphaIndex = c2i(char, alphabet)
    newIndex = alphaIndex + shift
    output += i2c(newIndex - len(alphabet), alphabet) #'''must change'''
  return output

def caesar_shift_decode(ciphertext, shift, alphabet):
  output = ""
  text = prepare_string(ciphertext, alphabet)
  for char in text:
    alphaIndex = c2i(char, alphabet)
    output += i2c(alphaIndex - shift, alphabet) #'''must change'''
  return output

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

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = "my coffee tastes like covfefe"
codebet = "QWERTYUIOPLKJHGFDSAZXCVBNM"
plaintext = plaintext.upper()
shift = 10
print("\n---Testing substitution-------")
ciphertext = substitution_cipher_encode(plaintext, alphabet, codebet)
recovered_text = substitution_cipher_decode(ciphertext, alphabet, codebet)
print("Plaintext = %s" % plaintext)
print("Ciphertext = %s" % ciphertext)
print("Recovered text = %s" % recovered_text)
print("\n---Testing Caesar-------")
ciphertext = caesar_shift_encode(plaintext, shift, alphabet)
recovered_text = caesar_shift_decode(ciphertext, shift, alphabet)
print("Plaintext = %s" % plaintext)
print("Ciphertext = %s" % ciphertext)
print("Recovered text = %s" % recovered_text)

''''''''''''''''''' PART 1: KEYWORD SUBSTITUTION '''''''''''''''''''

def make_cipher_alphabet(alphabet, keyword):
  temp = "".join(sorted(set(keyword), key = keyword.index))
  newAlpha = temp + alphabet
  newAlpha = "".join(sorted(set(newAlpha), key = newAlpha.index))
  return newAlpha


def keyword_substitution_cipher_encode(plaintext, keyword, alphabet_source):
  alpha2 = make_cipher_alphabet(alphabet_source, keyword) #cipheralpha
  alpha1 = alphabet_source #originalalpha
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

def keyword_substitution_cipher_decode(ciphertext, keyword, alphabet_source):
  alpha2 = make_cipher_alphabet(alphabet_source, keyword) #cipheralpha
  alpha1 = alphabet_source #originalalpha
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

print("\n---Testing Keyword Substitution-------")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = "To be or not to be, that is the question"
plaintext = plaintext.upper()
keyword = "SHAKESPEARE"
print("Cipher alphabet is " + make_cipher_alphabet(alphabet, keyword))
ciphertext = keyword_substitution_cipher_encode(plaintext, keyword, alphabet)
recovered_text = keyword_substitution_cipher_decode(ciphertext, keyword, alphabet)
print("Plaintext = %s" % plaintext)
print("Ciphertext = %s" % ciphertext)
print("Recovered text = %s" % recovered_text)

''''''''''''''''''' PART 2: ADDITIONAL CRACKING TOOLS '''''''''''''''''''
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

print("\n---Testing Additional Cracking Tools-------")
message = "Oak is strong and also gives shade. Cats and dogs each hate the other. The pipe began to rust while new. Open the crate but don't break the glass. Add the sum to the product of these three. Thieves who rob friends deserve jail. The ripe taste of cheese improves with age. Act on these orders with great speed. The hog crawled under the high fence. Move the vat over the hot fire."
message = message.upper()
print("Most common letters: " + str(frequent_letters(message)))
print("Most common letters: " + str(frequent_bigraphs(message)))
print("Most common letters: " + str(frequent_trigraphs(message)))
print("Most common letters: " + str(frequent_double_letters(message)))

''''''''''''''''''' EXTENSIONS '''''''''''''''''''

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
plaintext = "My CoFfEe, TaStEs LiKe CoVfEfE!"
codebet = "QWERTYUIOPLKJHGFDSAZXCVBNM"
#plaintext = plaintext.upper()
shift = 10
print("\n---Testing substitution [EXTENSIONS = 1 & 3]-------")
ciphertext = substitution_cipher_encode_2(plaintext, alphabet, codebet)
recovered_text = substitution_cipher_decode_2(ciphertext, alphabet, codebet)
print("Plaintext = %s" % plaintext)
print("Ciphertext = %s" % ciphertext)
print("Recovered text = %s" % recovered_text)
print("\n---Testing Caesar [EXTENSIONS = 1 & 3]-------")
ciphertext = caesar_shift_encode_2(plaintext, shift, alphabet)
recovered_text = caesar_shift_decode_2(ciphertext, shift, alphabet)
print("Plaintext = %s" % plaintext)
print("Ciphertext = %s" % ciphertext)
print("Recovered text = %s" % recovered_text)