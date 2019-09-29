import sys

def printBoard(gme):
   print("\n".join([gme[x : x + 8] for x in range(0,64,8)]))

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

if(len(sys.argv) > 1):
   gme = sys.argv[1]
   if(len(sys.argv) == 3):
      if("x" not in gme):
         indT = sys.argv[2].lower().upper()
      else:
         indT = sys.argv[2].upper().lower()
   else:
      indT = indTurn(gme)
else:
   indT = "X"
   gme = "...........................OX......XO..........................."

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

print(gme)
print("")
printBoard(gme)
print("")

gme = list(gme)
print("Possible Moves: ", end = "")

mvs = posMoves(gme, indT)
if len(mvs) == 0:
   print("No Moves")
else:
   print(mvs)
    
print("")

for x in mvs:
   gme[x] = "*"
    
print("")
printBoard("".join(gme))
print("Move: ", end = "")
print(mvs.pop())