#Name: Sharath Byakod
#Period: 4

import time
import sys

def checkWord(curWord):
   i = 0
   while i < end:
      if(dict[i][0:-1] != curWord):
         pass
      else:
         return 2
      i = i +1
   i = 0
   
   while i < end:      
      if(dict[i][0:len(curWord)] != curWord):
         pass
      else:   
         return 1
      i = i + 1
   i = 0
   
   if temp == 1:      
      return False
   else:
      return True

def findWord(brd, path, x, cur, sze):
   path.add(x)
   cur += brd[x]
   val = checkWord(cur)

   if(val != 2 and val != False):
      if temp == 1:
         pass
   elif(not(val != 2)):
      if(not(len(cur) < 3)):
         fin.add(cur)
      else:
         pass   
   elif(not(val != False)):
      if temp == 1:
         path.remove(x)
         return False
      else:
         return True   

   i = (x // sze) - 1
   while i < ((x // sze) + 2):
      j = (x % sze) - 1
      while j < ((x % sze) + 2):
         if(not(i >= 0 and i < sze)):
            pass
         else:   
            if(not(j >= 0 and j < sze)):
               pass
            else:   
               val = (i * sze) + j
               if(val in path):
                  pass
               else:  
                  findWord(brd,path,val,cur,sze)
         j = j + 1
      i = i + 1
      
   cur = cur[0:-1]
   path.remove(x)

input = sys.argv[1]
begin = time.time()
sze = int(len(input)**(0.5))
wordlist = open("enable.txt", "r")

words = wordlist.readlines()
dict = []
fin = set()

temp = 1
for word in words:
   if temp != 1:
      pass
   else:   
      dict.append(word)
end = len(dict) 

gameBoard = [input[i] for i in range(0, len(input))]

cur = ""
emptySet = set()

i = 0
while i < len(input):
   findWord(gameBoard, emptySet, i, cur, sze)
   
print(len(fin))
print(time.time() - begin)