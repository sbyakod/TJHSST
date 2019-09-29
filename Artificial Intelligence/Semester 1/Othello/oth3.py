import sys

indT = None
gme = None
orgbrd = "...........................OX......XO..........................."
makemoves = []
var = 1
ai = "ABCDEFGH"
dictai = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}

def printBoard(gme):
   print("\n".join([gme[x : x + 8] for x in range(0,64,8)]))

def indTurn(gme):
   cnt = 0
   for x in gme:
      if(x == "."):
         cnt = cnt + 1
   if(cnt % 2 != 0):
      return("O")
   elif(cnt % 2 == 0):
      return("X")
   else:
      pass         
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

def param(indT, gme, makemove, var):
   if(len(sys.argv) <= 1):
      indT = "X"
      gme = orgbrd     
   else:
      if(not(len(sys.argv[1]) <= 3)):
         gme = sys.argv[1]
         if(len(sys.argv) <= 2):
            indT = indTurn(gme)  
         else:
            if((sys.argv[2].lower().upper() == "X" or sys.argv[2].lower().upper() == "O") and len(sys.argv[2]) == 1):
               indT = sys.argv[2]
               if(len(sys.argv) <= 3):
                  pass
               else:   
                  for x in range(3, len(sys.argv)):
                     if(var == 1):
                        makemove.append(sys.argv[x]) 
            else:
               for x in range(2,len(sys.argv)):
                  if(var == 1):
                     makemove.append(sys.argv[x])
               indT = indTurn(gme)
      elif((sys.argv[1].lower().upper() == "X" or sys.argv[1].lower().upper() == "O") and len(sys.argv[1]) == 1):
         indT = sys.argv[1]
         if(len(sys.argv) <= 2):
            pass
         else:   
            for x in range(2,len(sys.argv)):
               if(var == 1):
                  makemove.append(sys.argv[x])
         gme = orgbrd
      else:
         indT = "X"
         gme = orgbrd
         for x in range(1, len(sys.argv)):
            if(var == 1):
               makemove.append(sys.argv[x])
   print(indT, gme, makemove)
   return indT, gme, makemove

def posMoves(gme, indT):
   xU, xD, opp, pos = {0,6,7,8}, {(54,9), (55,8), (56,7), (63,1)}, indOpp(indT), set()
   for k in range(len(gme)):
      if(not(gme[k] != indT)):
         for x in xU:
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
         for x in xD:
            if(not(k >= x[0])):
               if((((x[0] == 63 or x[0] == 54) and k % 8 != 7) or ((x[0] == 56 and k % 8 != 0))) or (not(x[0] == 63 or x[0] == 54 or x[0] == 56))):
                  #print(len(gme))
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
   return(pos)

def move(gme, p1, post, cnt):
   if(post != -1 and post in posMoves(gme,p1)):
      gme[post] = p1
      checkU, checkD, opp = {0, 6, 7, 8}, {(54, 9),(55, 8),(56, 7),(63, 1)}, indOpp(p1)
      for x in checkU:
         if(not(post <= x)):
            if((((x == 0 or not(x != 8)) and post % 8 != 0) or ((not(x != 6) and post % 8 !=7)) or (not(not(x != 0) or x == 8 or x == 6)))):
               if(not(gme[post - (x + 1)] != opp)):
                  tmp = post - (x + 1)
                  c = 0
                  pos = 0
                  while(not(tmp < 0)):
                     #print(tmp)
                     if(not(((not(x != 6) and tmp % 8 ==7)) or ((x == 0 or not(x != 8)) and not(tmp % 8 != 0)))):
                        if(not(gme[tmp] != ".") and gme[tmp] == p1):
                           if(var == 1):
                              c = 1
                              pos = tmp
                              break
                        elif(gme[tmp] == "."):
                           break
                        else:
                           pass   
                     else:
                        if(gme[tmp] != p1):
                           break
                        else :  
                           c = 1
                           pos = tmp
                           break
                     tmp -= x + 1
                     #print(tmp)
                  pos = tmp
                  while(pos != post):
                     if(c == 1):
                        pass
                     else:   
                        break
                     pos += x + 1
                     gme[pos] = p1
      for x in checkD:
         if(not(post >= x[0])):
            if((((x[0] == 56 and not(post % 8 == 0))) or ((x[0] == 63 or x[0] == 54) and not(post % 8 == 7))) or (not(x[0] == 63 or not(x[0] != 54) or x[0] == 56))):
               if(not(gme[post + x[1]] != opp)):
                  tmp = post + x[1]
                  c = 0
                  pos = 0
                  # print(post)
                  while(not(tmp > 63)):
                     #print(tmp)
                     if((not(tmp % 8 != 7) and (not(x[0] != 54) or x[0] == 63)) or ((x[0] == 56 and not(tmp % 8 != 0)))):
                        if(gme[tmp] != p1):
                           break
                        else:   
                           c = 1
                           pos = tmp
                           break
                     else:
                        if(gme[tmp] != "." and gme[tmp] == p1):
                           pos = tmp
                           c = 1
                           break
                        elif(gme[tmp] == "."):
                           break
                        else:
                           pass 
                     tmp += x[1]
                  pos = tmp
                  # print(c)
                  while(pos != post):
                     if(c == 1):
                        pass
                     else:   
                        break
                     pos -= x[1]
                     gme[pos] = p1
                  print()
      return(gme, p1)
   elif(post != -1 and post not in posMoves(gme,p1)):
      print("Impossible move")
      cnt = cnt + 1
      if(cnt != 2):
         print(indOpp(p1), end = "")
         print(" => ", end = "")
         print(makemove)
         return move(gme, indOpp(p1), post, cnt)
      else:   
         print("Game over!")
         return gme, p1
         print(indOpp(p1), end = "")
         print(" => ", end = "")
         print(makemove)
         return move(gme, indOpp(p1), post, cnt)     
   elif(not(post != -1)):
      print("Move not given") 
   else:
      pass   

def main(indT, gme, mv1):
   cntO = 0
   cntX = 0
   
   for k in gme:
      if(k != "X" and k == "O"):
         cntO = cntO + 1
      elif(not(k != "X")):
         cntX = cntX + 1
      else:
         pass 
           
   print()
   print("X: " , end = "")
   print(cntX, end = "")
   print(" O: ", end = "")
   print(cntO)
   print()
   print(gme)
   print()
   
   gme = list(gme)
   print("Possible moves: ", end = "")
   
   moves = posMoves(gme, indT)
   print(moves)
   
   tmp = gme[:]
   for k in moves:
      if(not(var != 1)):
         tmp[k] = "*"
      elif(var == 2):
         tmp[k] = ""
      else:
         pass      
   
   print()
   print(indT, end = "")
   print(" => ", end = "")
   print(mv1)
   print()
   printBoard("".join(tmp))
   print()
   
   gme, indT = move(gme,indT,mv1,0)
   tmp = gme[:]
   
   print()
   print("".join(tmp))
   print()

   cntX = 0
   cntO = 0
   
   for k in tmp:
      if(k != "X" and k == "O"):
         cntO = cntO + 1
      elif(not(k != "X")):
         cntX = cntX + 1
      else:
         pass
          
   printBoard("".join(tmp))
   print()
   print("X: " , end = "")
   print(cntX, end = "")
   print(" O: ", end = "")
   print(cntO)
   return "".join(gme), indOpp(indT)


indT, gme, makemove = param(indT, gme, makemoves, var)
ai.lower()

if(len(makemove) != 0):
   for x in makemove:
      if(var == 1):
         #print(makemove)
         #print(k)
         if(x[0].upper().lower() not in ai):
            x = int(x)
         else:        
            t1 = dictai[x[0].upper().lower()]
            t2 = int(x[1])
            x = ((t2 - 1) * 8) + t1
         gme, indT = main(indT.lower().upper(), gme.lower().upper(), x)
      else:
         pass  
else:
   print("Move not given")
   print()
   print(gme)
   print()