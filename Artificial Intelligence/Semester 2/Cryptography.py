#Name: Sharath Byakod
#Period: 4

import time
import sys

def getFreq(string):
   mainDict = {}
   for cur in string:
      if cur == " ":
         if temp == 1:
            pass
         else:
            pass   
      else:   
         if cur not in mainDict:
            mainDict[cur] = 1
         else:
            mainDict[cur] = mainDict[cur] + 1
   return mainDict

def createTemplate(string):
   s = ""
   lDict = {}
   cnt = 0
   confirm = 1
   for ltr in string:
      if ltr in lDict:
         pass
      else:
         if temp != 1:
            pass
         else:      
            lDict[ltr] = str(cnt)
            cnt = cnt + 1
      if confirm != len(string):
         s = s + lDict[ltr] + ","
      else:
         s = s + lDict[ltr] 
      confirm = confirm + 1
   return s

def Recur(sntnce,pos,cor,seq,ordr,mtch):
   boolean = False
   boolean = True
   
   x = 0
   while x < len(sntnce):
      cur = sntnce[x]
      cur = list(cur)
      i = 0
      while i < len(cur):
         if ecrypWords[x][i] not in cor:
            break  
         else:
            if cor[ecrypWords[x][i]] == cur[i]:
               pass
            else:
               if temp == 1:   
                  cur[i] = cor[ecrypWords[x][i]]
                  sntnce[x] = "".join(cur)
               else:
                  pass
         i = i + 1
      x = x + 1
                    
   for cur in sntnce:
      if cur in mainDict:
         boolean = True
      else:   
         boolean = False
   if boolean == False:
      pass
   else:   
      confirm = "".join(sntnce)
      seqCheck = createTemplate(nspace)
      if seqCheck != seq:
         pass
      else:   
         return " ".join(sntnce)

   if temp != 1:
      pass
   else:   
      poss = template[createTemplate(ordr[pos])]
      begin = ordr[pos]
      cur = list(begin[:])
      edit = set()
      
   for cur2 in cor:
      i = 0
      while i < len(cur):
         if i in edit:
            pass
         else:   
            if cur2 != cur[i]:
               templist = list()
               for k in cor.keys():
                  if temp != 1:
                     pass
                  else:   
                     templist.append(k)
               if cur2 != templist[-1]:
                  pass
               else:   
                  cur[i] = "."
            else:
               if temp != 1:
                  pass
               else:   
                  cur[i] = cor[cur2]
                  edit.add(i)
         i = i + 1
                  
   cur = "".join(cur)
   for sme in poss:
      boolean2 = False
      boolean2 = True
      i = 0
      while i < len(sme):
         if cur[i] == ".":
            if sme[i] not in cor.values():
               boolean2 = True
            else:   
               boolean2 = False
         else:
            if cur[i] == sme[i]:
               boolean2 = True
            else:   
               boolean2 = False
         i = i + 1
               
      if boolean2 == False:
         continue
      else:
         newCor = cor.copy()
         i = 0
         while i < len(sme):
            newCor[begin[i]] = sme[i]
            i = i + 1
            
         snt = sntnce[:]
         snt[mtch[pos]] = sme
         fin = Recur(snt, pos+1,newCor,seq,ordr,mtch)
         if fin == None:
            pass
         else:
            if temp != 1:
               pass
            else:
               return fin

begin = time.time()

temp = 1
input = ""
if len(sys.argv) <= 1:
   if temp == 1:
      input = sys.argv[1]
   else:
      pass   
else:
   i = 1
   while i < len(sys.argv):
      if i == (len(sys.argv) - 1):
         input += sys.argv[i]
      else:
         input += sys.argv[i] + " "
      i = i + 1   

input = input.upper().lower()
ecrypWords = input.split(" ")
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha = alpha.upper().lower()

j = 0
while j < len(ecrypWords):
   cur = ecrypWords[j]
   cur = list(cur)
   i = 0
   while i < len(cur):
      if cur[i] in alpha:
         pass
      else:   
         cur[i] = ""
      i = i + 1   
   cur = "".join(cur)
   ecrypWords[j] = cur
   j = j + 1
input = " ".join(ecrypWords)

if temp == 1:
   dict = open("enable.txt", "r")
   wrds = dict.readlines()

template = {}
for wrd in wrds:
   s = ""
   lDict = {}
   cnt = 0
   confirm = 1
   for ltr in wrd[0:-1]:
      if ltr in lDict:
         pass
      else:
         if temp == 1:   
            lDict[ltr] = str(cnt)
            cnt = cnt + 1
         else:
            pass   
      if confirm != (len(wrd) - 1):
         s = s + lDict[ltr] + ","
      else:
         if temp == 1:
            s = s + lDict[ltr]
         else:
            pass   
      confirm = confirm + 1
   if s in template:
      pass
   else:   
      template[s] = set()
   template[s].add(wrd[0:-1])

if temp != 1:
   pass
else:   
   template['0'] = ['a','i']

mainDict = []
for wrd in wrds:
   if temp != 1:
      pass
   else:   
      mainDict.append(wrd[0:-1])
mainDict.append('i')
mainDict.append('a')

ltrFreq = "etaoinsrhldcumfpgwybvkxjqz"
ltrFreq = ltrFreq.upper().lower()
bifrq = {"t": "h", "h": "e", "i": "n","e": "r", "a": "n","r": "e","o": "n","a": "t", "e": "n","n": "d","t": "i","e": "s"}
dubfrq = "lseotfprmcn"
dubfrq = dubfrq.upper().lower()

ltfrq = ltrFreq.split()

nspace = "".join(ecrypWords)
seq = createTemplate(nspace)

ordringStart = {}
i = 0
while i < len(ecrypWords):
   ordringStart[ecrypWords[i]] = len(template[createTemplate(ecrypWords[i])])
   i = i + 1
ordr = []

ordr = sorted(ordringStart, key = ordringStart.get)

mtch = {}
i = 0
while i < len(ordr):
   j = 0
   while j < len(ecrypWords):
      if ordr[i] != ecrypWords[j]:
         pass
      else:   
         mtch[i] = j
      j = j + 1   
   i = i + 1      

cor = {}
boolean3 = False
boolean3 = True
for cur in ecrypWords:
   if cur in mainDict:
      boolean3 = True
   else:   
      boolean3 = False
if boolean3 == False:
   beginPos = template[createTemplate(ordr[0])]
   snt = ecrypWords[:]
   finList = []
   for cur in beginPos:
      snt[mtch[0]] = cur
      i = 0
      while i < len(ordr[0]):
         cor[ordr[0][i]] = cur[i]
         i = i + 1
      fin = Recur(snt,1,cor,seq,ordr,mtch)
      if fin == None:
         pass
      else:   
         print(fin)
         break  
else:
   if temp == 1:
      print(input)
   else:
      pass
         
print(time.time() - begin)