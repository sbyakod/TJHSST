import sys

def printBoard(gme):
   print("\n".join([gme[i:i+8] for i in range(0,64,8)]))

def indTurn(gme):
   count = 0
   for each in gme:
      if each == ".":
         count += 1
   if count%2 == 0:
      if "x" in gme:
         return "x"
      else:
         return "X"
   else:
      if "x" in gme:
         return "o"
      else:
         return "O"

def indOpp(indT):
   if "x" not in gme:
      if indT == "X":
         return "O"
      else:
         return "X"
   else:
      if indT == "x":
         return "o"
      else:
         return "x"

def move(gme, p1, post):
   gme[post] = p1
   checkU, checkD, opp = {0,6,7,8}, {(54,9),(55,8),(56,7),(63,1)}, indOpp(p1)
   for x in checkU:
      if(post > x):
         if((((x == 6 and post%8 !=7)) or ((x == 0 or x == 8) and post%8 != 0)) or (not(x == 0 or x == 8 or x == 6))):
            if(not(gme[post - (x + 1)] != opp)):
               temp = post - (x + 1)
               pos = 0
               c = 0
               while(not(temp < 0)):
                  if(not(((x == 6 and temp%8 ==7)) or ((x == 0 or x == 8) and temp%8 == 0))):
                     if(gme[temp] != "." and gme[temp] == p1):
                        c = 1
                        pos = temp
                        break
                     elif(gme[temp] == "."):
                        break
                     else:
                        pass   
                  else:
                     if(gme[temp] != p1):
                        break
                     else:   
                        c = 1
                        pos = temp
                  temp -= (x + 1)
               pos = temp
               while(pos != post):
                  if(c == 1):
                     pass
                  else:
                     break
                  pos += (x + 1)
                  gme[pos] = p1
   for x in checkD:
      if(not(post >= x[0])):
         if((((x[0] == 63 or x[0] == 54) and post % 8 != 7) or ((x[0] == 56 and post % 8 != 0))) or (not(x[0] == 63 or x[0] == 54 or x[0] == 56))):
            if(not(gme[post+x[1]] != opp)):
               temp = post + x[1]
               pos = 0
               c = 0
               while(not(temp > 63)):
                  if(not(((x[0] == 56 and temp % 8 == 0)) or ((x[0] == 63 or x[0] == 54) and temp % 8 == 7))):
                     if(gme[temp] != "." and gme[temp] == p1):
                        c = 1
                        pos = temp
                        break
                     elif(gme[temp] == "."):                    
                        break
                     else:
                        pass   
                  else:
                     if(gme[temp] != p1):
                        break
                     else:   
                        c = 1
                        pos = temp
                        break
                  temp += x[1]
               pos = temp
               while(pos != post):
                  if(c == 1):
                     pass
                  else:   
                     break
                  pos -= x[1]
                  gme[pos] = p1
   gme = "".join(gme)
   return gme

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

def eval(brd, tkn):
   cnT = 0
   cnNT = 0
   
   for x in range(0, len(brd) - 1):
      if(brd[x] != tkn and brd[x] == indOpp(tkn)):
         cnNT = cnNT + 1
      elif(brd[x] == tkn):
         cnT = cnT + 1
      else:
         pass   
         
   num = cnT - cnNT
   return(num)

def negaMax(brd, tkn, lvl):
   if(not(lvl)):
      return [eval(brd, tkn)]

   lm = posMoves(brd, tkn)

   if(not(lm)):
      best = negaMax(brd, indOpp(tkn), lvl-1) + [-1]
   else:
      best = sorted([negaMax(move(list(brd), tkn, mv), indOpp(tkn), lvl-1) + [mv] for mv in lm])[0]
   return([-best[0]] + best[1:])


print(gme)
print(indT)

lvl = 5
nm = negaMax(gme,indT,lvl)
print("At level {} nm gives {} and I pick move {}".format(lvl, nm, nm[-1]))