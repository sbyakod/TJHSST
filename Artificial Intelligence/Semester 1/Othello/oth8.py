import sys
import random

class Strategy():
   def best_strategy(self, board, player, best_move, still_running):
      depth = 1
      brd = "".join(board).replace("?","").replace("@","X")
   
      token = "X" if player == "@" else "O"
   
      mv = bestMove(brd,token)
      move = 11 + (mv // 8) * 10 + (mv % 8)
   
      best_move.value = mv

def printBoard(gme):
   print("\n".join([gme[i:i+8] for i in range(0,64,8)]))

def indTurn(gme):
   count = 0
   for x in gme:
      if x == ".":
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

def norXC(mvset,indT):
   XC = {((1,6,8), 0), ((9,14,15), 7), ((48,49,57), 56), ((54,55,62), 63)}
   fnlmv = set(mvset)
   for x in XC:
      if(not(gme[x[1]] == indT)):
         for i in x[0]:
            if(i not in mvset):
               pass
            else:   
               fnlmv.remove(i)
      else:
         pass
                 
   return(fnlmv)

def notEdge(mvset):
   eU, eD, eL, eR  = {0,1,2,3,4,5,6,7}, {56,57,58,59,60,61,62,63}, {0,8,16,24,32,40,48,56}, {7,15,23,31,39,47,55,63}
   posMoves = set()
   for x in mvset:
      if(x not in eU or x not in eD or x not in eL or x not in eR):
         posMoves.add(x)
      else:
         pass   
   if(len(posMoves) != 0):
      return(posMoves)
   else:
      return(set())

def edgeMove(mvset,indT,gme):
   eU, eD, eL, eR  = {0,1,2,3,4,5,6,7}, {56,57,58,59,60,61,62,63}, {0,8,16,24,32,40,48,56}, {7,15,23,31,39,47,55,63}
   posMoves = set()
   cnt = 0
   for x in mvset:
      tempgme = gme[:]
      move(tempgme, indT, x, cnt)
      if(x in eL):
         if(not(tempgme[0] != indT)):
            temp = x
            while(not(temp < 0)):
               if(tempgme[temp] != indT):
                  break
               else:
                  if(temp != 0):
                     pass
                  else:   
                     posMoves.add(x)
               temp -= 8
         if(not(tempgme[56] != indT)):
            temp = x
            while(not(temp > 56)):
               if(tempgme[temp] != indT):
                  break
               else:
                  if(temp == 56):
                     posMoves.add(x)
               temp += 8
      if x in eR:
         if(not(tempgme[7] != indT)):
            temp = x
            while(not(temp < 7)):
               if(tempgme[temp] != indT):
                  break
               else:
                  if(temp != 7):
                     pass
                  else:   
                     posMoves.add(x)
               temp -= 8
         if(not(tempgme[63] != indT)):
            temp = x
            while(not(temp > 63)):
               if(tempgme[temp] != indT):
                  break
               else:
                  if(temp == 63):
                     posMoves.add(x)
               temp += 8
      if x in eU:
         if(not(tempgme[0] != indT)):
            temp = x
            while(not(temp < 0)):
               if(tempgme[temp] != indT):
                  break
               else:
                  if(temp != 0):
                     pass
                  else:   
                     posMoves.add(x)
               temp -= 1
         if(not(tempgme[7] != indT)):
            temp = x
            while(not(temp > 7)):
               if(tempgme[temp] != indT):
                  break
               else:
                  if(temp == 7):
                     posMoves.add(x)
               temp += 1
      if x in eD:
         if(not(tempgme[56] != indT)):
            temp = x
            while(not(temp < 56)):
               if(tempgme[temp] != indT):
                  break
               else:
                  if(temp != 56):
                     pass
                  else:   
                     posMoves.add(x)
               temp -= 1
         if(not(tempgme[63] != indT)):
            temp = x
            while(not(temp > 63)):
               if(tempgme[temp] != indT):
                  break
               else:
                  if(temp == 63):
                     posMoves.add(x)
               temp += 1
   if(len(posMoves) != 0):
      return(posMoves)
   else:
      return(set())

def spccnt(gme):
   count = 0
   for x in range(0,len(gme)-1):
      if gme[x] == ".":
         count+=1
   return count

def bestMove(gme, indT):
   if(spccnt(gme) > 8):
      print(gme)
      print("")
      printBoard(gme)
      print("")
   
      gme = list(gme)
      print("Possible Moves: ", end = "")
      mvs = possibleMoves(gme, indT)
      
      if(len(mvs) != 0):
         print(mvs)
      else:
         print("No Moves")
      print("")
      
      for x in mvs:
         gme[x] = "*"
      print("")
      
      printBoard("".join(gme))
      myMove = -1
      connEdges = edgeMove(moves, indT, gme)
      crnrMoves = crnrMove(moves)
      legal = norXC(moves,indT)
      notE = notEdge(legal)
   
      if(not(len(crnrMoves) <= 0)):
         myMove = (random.sample(list(crnrMoves), 1))
         print("Move: ", end = "")
         print(myMove)
      elif(not(len(connEdges) <= 0)):
         myMove = (random.sample(list(connEdges), 1))
         print("Move: ", end = "")
         print(myMove)
      elif(not(len(notE) <= 0)):
         myMove = (random.sample(list(notE), 1))
         print("Move: ", end = "")
         print(myMove)
      elif(not(len(legal) <= 0)):
         myMove = (random.sample(list(legal), 1))
         print("Move: ", end = "")
         print(myMove)
      else:
         print("Move: ", end = "")
         print ((random.sample(list(moves), 1)))
      return(myMove)
   else:
      print(gme)
      print(indT)
      lvl = 5
      nm = negamax(gme, indT, lvl)
      print("At level {} nm gives {} and I pick move {}".format(lvl,nm,nm[-1]))
      return(nm[-1])