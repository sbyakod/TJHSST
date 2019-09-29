from itertools import product
import time
import sys
import math

def printBoard(gme):
   print("\n".join([gme[x : x + 8] for x in range(0,64,8)]))

def indOpp(indT):
   if("x" in gme):
      if(indT != "x"):
         return("x")
      else:
         return("o")
   else:
      if(indT != "X"):
         return("X")
      else:
         return("O")

def indTurn(gme):
   cnt = 0
   for x in gme:
      if(x == "."):
         cnt = cnt + 1
   if(cnt % 2 != 0):
      if("x" not in gme):
         return("O")
      else:
         return("o")
   else:
      if("x" not in gme):
         return("X")
      else:
         return("x")

def param():      
   if(not(len(sys.argv) <= 1)):
      gme = sys.argv[1]
      if(not(len(sys.argv) != 3)):
         if("x" not in gme):
            indT = sys.argv[2].lower().upper()
         else:
            indT = sys.argv[2].upper().lower()
      else:
         indT = indTurn(gme)
   else:
      indT = "X"
      gme = "...........................OX......XO..........................."

def legalMoves(gme, p1, t1, t2):
   mvs = set()
   lst = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
   if(p1 != "O"):
      opp = "O"
   else:
      opp = "X"      
   for rUp, cUp in lst:  
      r = t1 + rUp
      c = t2 + cUp 
      while(not(gme[12 * r + c] != opp)):
         if(opp == "X" or opp == "O"):
            r += rUp
            c += cUp
         else:
            c += cUp
            r += rUp   
      if(not(gme[12 * r + c] != ".") and (not(abs(r - t1) < 2) or not(abs(c - t2) < 2))):
         mvs.add((r, c))
      else:
         pass   
   return(mvs)

def display():
   print(gme)
   print("")
   printBoard(gme)
   print("")
   param()
   print("")
   gme = list(gme)
   print("Possible Moves: ", end = "")
   mvs = posMoves(gme, indT)

   if len(mvs) != 0:
      print(mvs)
   else:
      print("No Moves")
   
   print("")

   for x in mvs:
      gme[x] = "*"
   
   print("")
   printBoard("".join(gme))
   
def posMoves(gme, indT):
   checkU, checkD, opp, pos = {0,6,7,8}, {(54,9), (55,8), (56,7), (63,1)}, indOpp(indT), set()
   for k in range(len(gme)):
      if(not(gme[k] != indT)):
         for x in checkU:
            if(not(k <= x)):
               if((((x == 0 or x == 8) and k % 8 != 0) or ((x == 6 and k % 8 != 7))) or (not(x == 0 or x == 8 or x == 6))):
                  if(not(gme[k - (x + 1)] != opp)):
                     tmp = k - (x + 1)
                     while(not(tmp < 0)):
                        if(not(gme[tmp] != indT) and tmp != k - (x + 1)):
                           break
                        else:
                           pass   
                        if(not(gme[tmp] != ".")):
                           pos.add(tmp)
                           break
                        else:
                           pass   
                        if(not(((x == 6 and tmp % 8 ==7)) or ((x == 0 or x == 8) and tmp % 8 == 0))):
                           if(not(gme[tmp] != ".")):
                              pos.add(tmp)
                              break
                           else:
                              pass   
                           tmp -= x + 1
                        else:
                           break
         for x in checkD:
            if(not(k >= x[0])):
               if((((x[0] == 63 or x[0] == 54) and k % 8 != 7) or ((x[0] == 56 and k % 8 != 0))) or (not(x[0] == 63 or x[0] == 54 or x[0] == 56))):
                  if(not(gme[k + x[1]] != opp)):
                     tmp = k + x[1]
                     while(not(tmp > 63)):
                        if(not(gme[tmp] != indT) and tmp != k + x[1]):
                           break
                        else:
                           pass   
                        if(gme[tmp] != "."):
                           pass
                        else:   
                           pos.add(tmp)
                           break
                        if(not(((x[0] == 56 and tmp % 8 == 0)) or ((x[0] == 63 or x[0] == 54) and tmp % 8 == 7))):
                           if(gme[tmp] != "."):
                              pass
                           else:   
                              pos.add(tmp)
                              break
                           tmp += x[1]
                        else:
                           break
   return pos      

def main():                    
   gme = ["*" for i in range(int(math.pow(12, 2)))]
   if(not(len(sys.argv) <= 1)):
      getIn = [c.lower().upper() for c in sys.argv[1]]
   elif(len(sys.argv) <= 1):
      getIn = "...........................OX......XO..........................."   
   else:
      pass   
   if(not(len(sys.argv) <= 2)):
      tokn = sys.argv[2].lower().upper()
   elif(len([c for c in getIn if not(c != ".")]) % 2):
      tokn = "O"
   else:
      tokn = "X"       
   x, o = set(), set()
   temp = gme
   for i, j in product(range(0, 8), range(0, 8)):
      temp[12 * (i + 2) + j + 2] = getIn[8 * i + j]
      if((getIn[8 * i + j] != "X") and (getIn[8 * i + j] == "O")):
         o.add((i + 2, j + 2))
      elif(not(getIn[8 * i + j] != "X")):
         x.add((i + 2, j + 2))
      else:
         pass   
   legal = set()
   if(tokn != "X"):
      for r, c in o:
         legal = legal | legalMoves(gme, tokn, r, c)
   else:
      for r, c in x:
         legal = legal | legalMoves(gme, tokn, r, c)  

   print("Legal Moves:")
   if(not legal):
      print("None")
   else:   
      for m in legal: 
         print(str(8 * (m[0] - 2) + m[1] - 2))
      
if __name__ == "__main__":
   main()