#from subcipher import *
from math import gcd
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
  temp = s
  for char in s:
    if char not in alphabet:
      temp = temp.replace(char, "")
  return temp

def vigenere_encode(plaintext, key, alphabet):
  output = ""
  text = prepare_string(plaintext, alphabet)
  klen = len(key)
  count = 0
  for char in text:
    tval = c2i(char, alphabet)
    kval = c2i(key[count], alphabet)
    nval = (tval + kval) % len(alphabet)
    output += i2c(nval, alphabet)

    count += 1
    if count >= klen:
      count = 0
  
  return output

def vigenere_decode(ciphertext, key, alphabet):
  output = ""
  text = prepare_string(ciphertext, alphabet)
  klen = len(key)
  count = 0
  for char in text:
    tval = c2i(char, alphabet)
    kval = c2i(key[count], alphabet)
    nval = (tval - kval) % len(alphabet)
    output += i2c(nval, alphabet)

    count += 1
    if count >= klen:
      count = 0
  
  return output

def index_of_coincidence(ciphertext, alpha):
  text = prepare_string(ciphertext, alpha)
  tlen = len(text)
  ioc = 0
  for char in alpha:
    nchar = text.count(char)
    ioc += (nchar / tlen) * ((nchar - 1) / (tlen - 1))
  return ioc
    
def friedman_test(ciphertext, alpha):
  text = prepare_string(ciphertext, alpha)
  tlen = len(text)
  ioc = index_of_coincidence(ciphertext, alpha)
  klen = (.027 * tlen) / ((ioc * (tlen - 1)) + .0655 - (.0385 * tlen))
  return (klen)

def kasiski_test(ciphertext):  #Code partially provided
    # Here, write code to create the array of distances:
    text = ciphertext
    trigraphs = []
    distances = [0] * 1000000
    for index in range(len(text) - 1):
      if text[index:index + 3] in trigraphs:
        ind = trigraphs.index(text[index:index + 3])
        distances[ind] += abs(text.find(text[index:index + 3]) - index)
      else:
        trigraphs.append(text[index:index + 3])
    #c = Counter(trigraphs)
    #return c.most_common(5)
    # Code is provided to find the gcd of any common distances appearing at least twice, just add your array:
    dCount = Counter(distances)
    topCount = dCount.most_common(6)
    my_gcd = topCount[0][0]
    for index in range(1, len(topCount)):
        if topCount[index][1] > 1:
            my_gcd = gcd(my_gcd, topCount[index][0])
    return my_gcd
    
def run_key_tests(ciphertext, alphabet): #Code provided
    """Runs Friedman and Kasiski tests and formats the output nicely"""
    friedman = friedman_test(ciphertext, alphabet)
    kasiski = kasiski_test(ciphertext)
    out = "Friedman test gives: " + str(friedman) + " and Kasiski gives this as the most likely: " + str(kasiski);
    return out

def make_cosets(text, n):
  array = [""] * n
  count = 0
  for char in text:
    array[count] += char

    count += 1
    if count >= n:
      count = 0

  return array

def rotate_list(old_list):  #Code provided
    """Takes the given list, removes the first element, and appends it to the end of the list, then returns the
    new list"""
    new_list = old_list[:]
    new_list.append(old_list[0])
    del new_list[0]
    return new_list

def find_total_difference(list1, list2):
  diff = 0
  for i in range(0, len(list1)):
    diff += abs(list1[i] - list2[i])
  return diff

def find_likely_letters(coset, alpha, eng_freq):
    """Finds the most likely shifts for each coset and prints them
    Recommended strategy: make a list of the frequencies of each letter in the ciphertext, in order, A to Z."""
    cfreq = [0.0] * len(alpha)
    for i in range(0, len(alpha)):
      cfreq[i] = (coset.count(alpha[i])) / len(coset)
    #print(cfreq)
    """Then, alternate using the find total difference method (on your frequencies list and the standard english frequencies list) and the rotate list method to fill out a new list of differences. This makes a list of the total difference for each possible encryption letter, A to Z, in order."""
    ldiff = [0] * len(alpha)
    for i in range(0, len(alpha)):
      cfreq = rotate_list(cfreq)
      ldiff[i] = find_total_difference(cfreq, eng_freq)
    #print(ldiff)
    """Then, find the indices of the smallest values in the new list, and i2c them for the most likely letters."""
    temp = sorted(ldiff)
    letter1 = i2c((ldiff.index(temp[0]) + 1) % len(alpha), alpha)    #ldiff.index(min(ldiff))
    letter2 = i2c((ldiff.index(temp[1]) + 1) % len(alpha), alpha)

    #return statement provided.  feel free to replace "letter1" and "letter2" with other variable names.
    return ("the most likely letter is: " + letter1 + " followed by: " + letter2)

def crack(ciphertext, alpha, eng_freq):  #Code provided
    """User-friendly walkthrough of decoding methods"""
    print("Your cipher text is: " + ciphertext)
    out = run_key_tests(ciphertext, alpha)
    print(out)
    x = int(input("Choose the key length you'd like to try: "))
    cosets = make_cosets(ciphertext, x)
    for index in range(len(cosets)):
        print("For coset " + str(index + 1) + ", " + find_likely_letters(cosets[index], alpha, eng_freq) + ".")
    s = input("Type the key you would like to use to decipher: ")
    print(vigenere_decode(ciphertext, s, alpha))
    print()

#============================================================#
#============================================================#
#============================================================#

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

eng_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751, .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]

example = "UZRZEGNJENVLISEXRHLYPYEGTESBJHJCSBPTGDYFXXBHEEIFTCCHVRKPNHWXPCTUQTGDJHTBIPRFEMJCNHVTCFSAIIJENREGSALHXHWZWRZXGTTVWGDHTEYXISAGQTCJPRSIAPTUMGZALHXHHSOHPWCZLBRZTCBRGHCDIQIKTOAAEFTOPYEGTENRAIALNRXLPCEPYKGPNGPRQPIAKWXDCBZXGPDNRWXEIFZXGJLVOXAJTUEMBLNLQHGPWVPEQPIAXATYENVYJEUEI"

'''SELF TESTS'''
'''print(vigenere_encode("EXAMPLEMESSAGE", "WORD", alpha))
print(vigenere_decode("ALRPLZVPAGJDCS", "WORD", alpha))
print(index_of_coincidence("ALPHA", alpha)) #NEED TO CHECK
print(friedman_test(example, alpha)) #NEED TO CHECK
print(kasiski_test(example)) #NEED TO CHECK
print(make_cosets("EXAMPLES!", 3))
print(find_total_difference([1, 1, 1], [1, 1, 1]))
print(find_likely_letters("EME", alpha, eng_freq))'''


# For the example, the key is "PLANET" and the plaintext is:
# "For many years the known planets of our solar system were mercury, venus, earth, mars, jupiter, saturn, uranus, neputne, and pluto.  However, it is now true that many people think pluto should no longer be considered a named planet.  New planets are currently being discovered, and it is very likely that many more will be in the near future."

#Try this:
crack(example, alpha, eng_freq) #KEYWORD: PLANET

#Once everything works, uncomment the following six lines and crack some ciphertexts!
c1 = "RVCQWMYFULRIKPFMQEMTJJOCLHYVHNFONGOGUFCRWHEPYAOOQSQCBYCRGMFYRSMRQUQSMYBXGKULHCRHIZSMSTZGQCCBNJMFMBARVURHBGGQFCFCHBGBAUCLIGQGHBMINPSFWWHECHPOHBCGAVULQYRCJPCXSQYECIBRCQHLGPORWILGQGHBQAUJZVGHMMTNCLNGHNPIFWBYCRMRCVCEOGHYJCHEWHMHBCFYYFFGSLRSMRGGWDFYWHRSRRKUQHIMGBMFNYBXGHGYRYZCNFTLGSXKOHYBXIOMGGEGTLCOEMINYBXEWPCHYPFCZZYYBMUSLQ"
c2 = "EFMREXHTGRQQVDODIPQSIVVNURSUVVNGNXRRIOIBEPOZNISWDRIOEOWVVYAVVIDFJFTYQDPFRKQMQCCFQBQXNRTKYRRHRCQWTXVZNIZVRDCEODSHZVCWDEENVCQWTXVVRRBSJTRMUZVRIIAOWMQIZNXYPYGJAEDMYKKIGCWXEYAUKRDNPSKCHHXVLQZMQILNFOVVVRNFSRJIVNGBEWKEGCVKRTZTJWWYGIIHSGDVZOPYJUGHUKBIPGETUYJDNXOTSXKOJIPMPXFZNIDLHKICQBVHEKNGCWDPURGCSXTTEUMSQULMRDMRPRNFSQSNVMGXXDVZOPMSPOFNNIVHHVRTOHWQRSEYHLPXOHKPJQIIVRQVKEAVKVJGKPTYKUCDMKXKOCEGWKKHUFUTMIFQUEKCAUKKTGXMQQEEQBQRTVPTYKUCDMKXKOCEGWKKHUKHGZYURFSGYJSTFGTKQPKEGKCXRHZNFKWHSLEPMIRHZNUDVXEKIQXWWJRTYSPOCLTQWEWGGETPSUOZNIKWSGTIHSGWCJKQBWRNMIPQEJKMEPZVRDCEODLHRIOEOWVQWPTYKUCDMKXKWJLSQPXHPIESEMUGJEZZIUVZSGSRPCEYFSJIGIEPDWXDAEEDWLPTLWNMQIBNQGPHFXEQPXKGRPRVMFCKIQXHRORIPCTHEZANSDHFRLIYVLVYMUKRGHFROKPOQXIEBIOCKEFDEVMJIPMPXFVTGCXLPXDGLYJIZNIKRGORIPDELPZNIDLHUFUTMIFQUEKWTOGDEPDEWKFNQPXKGSUKVHVAJTGWEQFDAPKKHOVNVYJGGIIXOHDTKIHKGWUJUEREVORCJSRHEFDGYJFQDPWDIURIOIBEPUKHGCIPKXHVLIFQESKNIUGUPCBXRHKHGZVRIIAOWMQIGRQMIVUSUVYJWGETJOXHTDSQPXZCIEFOZHNFPOORWKJUUOHIQITJSWOCIGGBTUQTEUCALVYTJOXHTDPTYKUCDMKXKLOGLGWIQVRTKYRRTTOFSRJTVSGBZHFWOTDLHCTTWKPZTZTKXKRHJOWBGHEFDGCSIVNATOIQIZNGOVLPXCQWFLPVSGXKLPVETSRJVVCJXMTWVSYSXKUFFVGEUGUEXOPRRDEPDTUCTTKMIV"
c3 = "OPKLNPCAVGYQRPKSAJUMYIUGVJHETIRRYWRHEEXQVBYEGSEIZVJSSMKEXWRSHVVHKWYXRVKSJTGVTIWSMQTHBSIHDAVPNCYEYJKIAXRGFMJXBXYIRIRPVXUIKQIXRHJMHXRCNRVRJZSSHWWEXMSSEIKLVVGQRXIIRQJIGLVJVKKSSEDEIWLEOSLXAWXXLJZZZEOXUEYIVDEFYETOHWAWGETLZITHEYXKZLRCUEEHNWSISIRXPZKWJMEWOWTQNHVJJZZLRWKEDZYMGARWIWAWRXICDVMXUICMABKZRRRXOPKFRWKSABOQRWZXRIYWRPUSHEUVXMEKVVJEGTIINMTXGLVIGMIXEMTGPZXIAXNENKAXBJWHPZORTHRCGQMLGLFYMAOXJEJTVZZSSXYIZKURBQPHMQBIVRGVZXGVNXZSINUVUEKIRMKOGLVJGIZANWJIQMTJYMXLOAATNRUADVYXBRNLJEGWGLZVOGTMAIRRYPGHNZRVDKUWRYCGZZGFBZVLDAXMTLKEISRIJIEXNTUAYCIINBORTWVZZZGPGMDINWTXUINETWTINGYPVVJMAKFTKWYMGIKLZTOJGWYEABZLRTFWOMXAVXYXCMKRBVDSPALEPIXEUMJJESDXCMCEYPZXRIYSAIFJOPUWRTZGOCXIFAYMXPGVRWFGJVZVVZVHOPGXGLVITMYJBPCSRGUYNFFYOENIACFYHWBIOMXFMWZLRVZWRIZGUMEKTWAXUITEKBOSAFVRZIZLVXIEI"
crack(c1, alpha, eng_freq) #KEYWORD: YOU
crack(c2, alpha, eng_freq) #KEYWORD: CRACKED
crack(c3, alpha, eng_freq) #KEYWORD: VIGENERE