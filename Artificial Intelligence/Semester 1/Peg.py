import sys, collections, Queue, time, math

target = ""
template = {}
ref = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E"]
numsteps = 0
start = time.clock()

def swap(a, b, puz):
   temp = list(a)
   temp[i], temp[j] = temp[j], temp[i]
   return("".join(temp))
   
findDec(puz):
   