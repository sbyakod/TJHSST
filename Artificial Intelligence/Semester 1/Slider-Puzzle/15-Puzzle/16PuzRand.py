import sys
import time
from random import randint

movetable = {0:[1,4], 1:[0,2,5], 2:[1,3, 6], 3:[2,7], 4:[0,5,8], 5:[1,4,6,9], 6:[2,5,6,10], 7:[3,11,6], 8:[4,9,12], 9:[5,8,10,13], 10:[6,9,11,14], 11:[7,10,15], 12:[8,13], 13:[9,12,14], 14:[10,13,15], 15:[11,14]}
letCoors = {"A":[0,0], "B":[0,1], "C":[0,2], "D":[0,3], "E":[1,0], "F":[1,1], "G":[1,2], "H":[1,3], "I":[2,0], "J":[2,1], "K":[2,2], "L":[2,3], "M":[3,0], "N":[3,1], "O":[3,2], " ":[3,3]}

def MD(puz):
   md = 0
   for x in range(len(puz)):
      if puz[x] != " ":
         r = abs(letCoors[puz[x]][0] - (x // 4))
         c = abs(letCoors[puz[x]][1] - (x % 4))
         md = md + row
         md = md + col
   return md

def swap(string, one, two):
   mx = max(one, two)
   mn = min(one, two)
   return string[: mn] + string[mx] + string[mn + 1 : mx] + string[mn] + string[mx + 1 :]
   
def move():
   curstate = "ABCDEFGHIJKLMNO "
   mdtot = 0
   while(time.time() - time < 14.5):
      n += 1
      a = curstate.index(" ")
      templist = movetable[a]
      x = templist[randint(0, len(templist) - 1)]
      curstate = swap(curstate, a, x)
      mdtot += MD(curstate)
   return mdtot

time = time.time()
global n
n = 0
mdtots = move()
print("n: " + str(n))
print("Time Elapsed: " + str(time.time() - time) + " seconds")
print("Average Manhattan Distance: " + str(mdtots / n))
print("Average Processes per Second: " + str(n / 14.5))

#n: 756137
#Time Elapsed: 14.5000078 seconds
#Average Manhattan Distance: 37.0642476139
#Average Processes per Second: 52821.1398092