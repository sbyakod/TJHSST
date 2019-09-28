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