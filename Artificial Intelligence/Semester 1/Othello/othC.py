import sys
import random
import time

def printBoard(gme):
   print("\n".join([gme[i : i + 8] for i in range(0, 64, 8)]))

def cnt(brd, tkn):
   CNT = 0
   nCNT = 0
   for x in range(0, len(brd)):
      if brd[x] == tkn:
         CNT += 1
      elif brd[x] == ".":
         nCNT += 1
   if CNT < nCNT:
      return(True)
   return(False)

def indTurn(gme): 
   cnt = 0
   for x in gme:
      if x == ".":
         cnt += 1
   if cnt%2 == 0:
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

def move(gme,  p1,  post):
   gme[post] = p1
   checkU,  checkD,  opp = {0, 6, 7, 8},  {(54, 9), (55, 8), (56, 7), (63, 1)},  indOpp(p1)
   for check in checkU:
      if post > check:
         if ((not(check == 0 or check == 8 or check == 6)) or (((check == 0 or check == 8) and post%8 != 0) or ((check == 6 and post%8 !=7)))):
            if gme[post-(check+1)] == opp:
               temp = post-(check+1)
               pos = 0
               c = 0
               while temp >= 0:
                  if(not(((check == 0 or check == 8) and temp%8 == 0) or ((check == 6 and temp%8 ==7)))):
                     if gme[temp] == ".":
                        break
                     elif gme[temp] == p1:
                        c = 1
                        pos = temp
                        break
                  else:
                     if gme[temp] == p1:
                        c = 1
                        pos = temp
                     break
                  temp = temp - (check+1)
               pos = temp
               while pos != post:
                  if c != 1:
                     break
                  pos = pos + (check+1)
                  gme[pos] = p1
   for check in checkD:
      if post < check[0]:
         if ((not(check[0] == 63 or check[0] == 54 or check[0] == 56)) or (((check[0] == 63 or check[0] == 54) and post%8 != 7) or ((check[0] == 56 and post%8 != 0)))):
            if gme[post+check[1]] == opp:
               temp = post+check[1]
               pos = 0
               c = 0
               while temp <= 63:
                  if(not(((check[0] == 63 or check[0] == 54) and temp%8 == 7) or ((check[0] == 56 and temp%8 == 0)))):
                     if gme[temp] == ".":
                        break
                     elif gme[temp] == p1:
                        c = 1
                        pos = temp
                        break
                  else:
                     if gme[temp] == p1:
                        c = 1
                        pos = temp
                     break
                  temp = temp + check[1]
               pos = temp
               while pos != post:
                  if c != 1:
                     break
                  pos = pos - check[1]
                  gme[pos] = p1
   gme = "".join(gme)
   return gme

if len(sys.argv) > 1:
   gme = sys.argv[1]
   if len(sys.argv) == 3:
      if "x" in gme:
         indT = sys.argv[2].upper().lower()
      else:
         indT = sys.argv[2].lower().upper()
   else:
      indT = indTurn(gme)
else:
   indT = "X"
   gme = "...........................OX......XO..........................."

def posMoves(gme,  indT, lgls):
   bl = cnt(gme,  indT)
   if(bl):
      checkU,  checkD,  pos,  opp = {0, 6, 7, 8},  {(54, 9), (55, 8), (56, 7), (63, 1)},  set(),  indOpp(indT)
      for x in range(len(gme)):
         if gme[x] == indT:
            for check in checkU:
               if x > check:
                  if ((not(check == 0 or check == 8 or check == 6)) or (((check == 0 or check == 8) and x%8 != 0) or ((check == 6 and x%8 !=7)))):
                     if gme[x-(check+1)] == opp:
                        temp = x-(check+1)
                        while temp >= 0:
                           if gme[temp] == indT and temp != x-(check+1):
                              break
                           if gme[temp] == ".":
                              pos.add(temp)
                              break
                           if(not(((check == 0 or check == 8) and temp%8 == 0) or ((check == 6 and temp%8 ==7)))):
                              if gme[temp] == ".":
                                 pos.add(temp)
                                 break
                              temp = temp - (check+1)
                           else:
                              break
            for check in checkD:
               if x < check[0]:
                  if ((not(check[0] == 63 or check[0] == 54 or check[0] == 56)) or (((check[0] == 63 or check[0] == 54) and x%8 != 7) or ((check[0] == 56 and x%8 != 0)))):
                     if gme[x+check[1]] == opp:
                        temp = x+check[1]
                        while temp <= 63:
                           if gme[temp] == indT and temp != x+check[1]:
                              break
                           if gme[temp] == ".":
                              pos.add(temp)
                              break
                           if(not( ((check[0] == 63 or check[0] == 54) and temp%8 == 7) or ((check[0] == 56 and temp%8 == 0)))):
                              if gme[temp] == ".":
                                 pos.add(temp)
                                 break
                              temp = temp + check[1]
                           else:
                              break
   else:
      checkU,  checkD,  pos,  opp = {0, 6, 7, 8},  {(54, 9), (55, 8), (56, 7), (63, 1)},  set(),  indOpp(indT) ##
      for x in range(len(gme)):
         if gme[x] == ".":
            for check in checkU:
               if x > check:
                  if ((not(check == 0 or check == 8 or check == 6)) or (((check == 0 or check == 8) and x%8 != 0) or ((check == 6 and x%8 !=7)))):
                     if gme[x-(check+1)] == opp:
                        temp = x-(check+1)
                        while temp >= 0:
                           if gme[temp] == "." and temp != x-(check+1):
                              break
                           if gme[temp] == indT:
                              pos.add(x)
                              break
                           if(not(((check == 0 or check == 8) and temp%8 == 0) or ((check == 6 and temp%8 ==7)))):
                              if gme[temp] == indT:
                                 pos.add(x)
                                 break
                              temp = temp - (check+1)
                           else:
                              break
            for check in checkD:
               if x < check[0]:
                  if ((not(check[0] == 63 or check[0] == 54 or check[0] == 56)) or (((check[0] == 63 or check[0] == 54) and x%8 != 7) or ((check[0] == 56 and x%8 != 0)))):
                     if gme[x+check[1]] == opp:
                        temp = x+check[1]
                        while temp <= 63:
                           if gme[temp] == "." and temp != x+check[1]:
                              break
                           if gme[temp] == indT:
                              pos.add(x)
                              break
                           if(not( ((check[0] == 63 or check[0] == 54) and temp%8 == 7) or ((check[0] == 56 and temp%8 == 0)))):
                              if gme[temp] == indT:
                                 pos.add(x)
                                 break
                              temp = temp + check[1]
                           else:
                              break
   lgls[("".join(gme), indT)] = pos
   return(pos)

def eval(brd,  tkn):
   CNT = 0
   nCNT = 0
   for x in range(0, len(brd)):
      if brd[x] == tkn:
         CNT += 1
      elif brd[x] == indOpp(tkn):
         nCNT += 1
   nM = CNT - nCNT
   return(nM)

def negC(brd,  tkn,  imp,  bnd,  lgls):
   brd = "".join(brd)
   global negaG
   global holdval
   negaG += 1
   if((brd, tkn) in lgls):
      holdval += 1
      temp = lgls[(brd, tkn)]
   else:
      temp = posMoves(brd,  tkn, lgls)
   if not temp:
      if((brd, indOpp(tkn)) in lgls):
         holdval += 1
         temp = lgls[(brd, indOpp(tkn))]
      else:
         temp = posMoves(brd,  indOpp(tkn), lgls)
      brd = list(brd)
      if not temp:
         return[eval(brd, tkn), -3]  
      nM = negC(brd,  indOpp(tkn),  -bnd,  -imp, lgls) + [-1]
      return [-nM[0]] + nM[1:]
   brd = list(brd)
   bst = []  
   Nbnd = -imp
   for mv in temp:
      nM = negC(move(list(brd),  tkn,  mv),  indOpp(tkn),  -bnd,  Nbnd, lgls) + [mv]
      if not bst or nM[0] < Nbnd:    
         bst = nM
         if nM[0] < Nbnd:
            Nbnd = nM[0]
            if -Nbnd >= bnd: return [-bst[0]] + bst[1:]
   return [-bst[0]] + bst[1:]

def negaMax(brd,  tkn,  lvls):
   if not lvls:
      return [eval(brd,  tkn)]

   temp = posMoves(brd,  tkn)
   if not temp:
      bst = negaMax(brd,  indOpp(tkn),  lvls-1) + [-1]
   else:
      bst = sorted([negaMax(move(list(brd),  tkn,  mv, mvsD), indOpp(tkn),  lvls-1) + [mv] for mv in temp])[0]
   return [-bst[0]] + bst[1:]

def crnMove(mvset):
   crns = {0, 7, 56, 63}
   curcrn = set()
   for x in crns:
      if x in mvset:
         curcrn.add(x)
   if len(curcrn) == 0:
      return set()
   else:
      return curcrn

def noEdge(mvset):
   edgL,  edgR  = {0, 8, 16, 24, 32, 40, 48, 56},  {7, 15, 23, 31, 39, 47, 55, 63}
   edgUp,  edgD = {0, 1, 2, 3, 4, 5, 6, 7},  {56, 57, 58, 59, 60, 61, 62, 63}
   posMoves = set()
   for x in mvset:
      if x not in edgL or x not in edgR or x not in edgUp or x not in edgD:
         posMoves.add(x)
   if len(posMoves) == 0:
      return set()
   else:
      return posMoves

def norXC(mvset, indT):
   XC = {((1, 6, 8), 0), ((9, 14, 15), 7), ((48, 49, 57), 56), ((54, 55, 62), 63)}
   fnlmv = set(mvset)
   for x in XC:
      if gme[x[1]] != indT:
         for some in x[0]:
            if some in mvset:
               fnlmv.remove(some)
   return fnlmv

def edgeMove(mvset, indT, gme):
   edgL,  edgR  = {0, 8, 16, 24, 32, 40, 48, 56},  {7, 15, 23, 31, 39, 47, 55, 63}
   edgUp,  edgD = {0, 1, 2, 3, 4, 5, 6, 7},  {56, 57, 58, 59, 60, 61, 62, 63}
   posMoves = set()
   cnt = 0
   for x in mvset:
      tempGame = gme[:]
      move(tempGame, indT, x)
      if x in edgL:
         if tempGame[0] == indT:
            temp = x
            while temp >= 0:
               if tempGame[temp] == indT:
                  if temp == 0:
                     posMoves.add(x)
               else:
                  break
               temp = temp - 8
         if tempGame[56] == indT:
            temp = x
            while temp <= 56:
               if tempGame[temp] == indT:
                  if temp == 56:
                     posMoves.add(x)
               else:
                  break
               temp = temp + 8
      if x in edgR:
         if tempGame[7] == indT:
            temp = x
            while temp >= 7:
               if tempGame[temp] == indT:
                  if temp == 7:
                     posMoves.add(x)
               else:
                  break
               temp = temp - 8
         if tempGame[63] == indT:
            temp = x
            while temp <= 63:
               if tempGame[temp] == indT:
                  if temp == 63:
                     posMoves.add(x)
               else:
                  break
               temp = temp + 8
      if x in edgUp:
         if tempGame[0] == indT:
            temp = x
            while temp >= 0:
               if tempGame[temp] == indT:
                  if temp == 0:
                     posMoves.add(x)
               else:
                  break
               temp = temp - 1
         if tempGame[7] == indT:
            temp = x
            while temp <= 7:
               if tempGame[temp] == indT:
                  if temp == 7:
                     posMoves.add(x)
               else:
                  break
               temp = temp + 1
      if x in edgD:
         if tempGame[56] == indT:
            temp = x
            while temp >= 56:
               if tempGame[temp] == indT:
                  if temp == 56:
                     posMoves.add(x)
               else:
                  break
               temp = temp - 1
         if tempGame[63] == indT:
            temp = x
            while temp <= 63:
               if tempGame[temp] == indT:
                  if temp == 63:
                     posMoves.add(x)
               else:
                  break
               temp = temp + 1
   if len(posMoves) == 0:
      return set()
   else:
      return posMoves

def spccnt(gme):
   cnt = 0
   for x in range(0, len(gme)-1):
      if gme[x] == ".":
         cnt+=1
   return cnt

def bestMove(gme,  indT, lgls):
   gme = list(gme)
   mvs = posMoves(gme,  indT, lgls)
   p1mv = -1
   crnmv = crnMove(mvs)
   cnEdg = edgeMove(mvs, indT, gme)
   legal = norXC(mvs, indT)
   noEdg = noEdge(legal)
   if len(crnmv) > 0:
      p1mv = (random.sample(list(crnmv), 1))
      print("Heuristic Move: ",  end="")
      print(p1mv)
   elif len(cnEdg) > 0:
      p1mv = (random.sample(list(cnEdg), 1))
      print("Heuristic Move: ",  end="")
      print(p1mv)
   elif len(noEdg) > 0:
      p1mv = (random.sample(list(noEdg), 1))
      print("Heuristic Move: ",  end="")
      print(p1mv)
   elif len(legal) > 0:
      p1mv = (random.sample(list(legal), 1))
      print("Heuristic Move: ",  end="")
      print(p1mv)
   else:
      print("Heuristic Move: ",  end="")
      print ((random.sample(list(mvs), 1)))
   if(spccnt(gme) <= 14):
      lvls = 7
      nM = negC(gme, indT, -65, 65, lgls)
      print("Negamax (AlphBeta):",  end="")
      return(nM)
   return(p1mv)

holdval = 0
negaG = 0
print("")
printBoard("".join(gme))
print("Possible Moves: ",  end="")
lgls = {}
print(posMoves(gme, indT, lgls))
print(bestMove(gme, indT, lgls))