import sys

indT = None
gme = None
makemove = None

A1 = "abcdefgh"
tblA1 = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}

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

def possMoves(gme, indT):
   checkD, checkU, opp, poss = {(54,9),(55,8),(56,7),(63,1)}, {0,6,7,8}, indOpp(indT), set()
   for x in range(len(gme)):
      if(gme[x] == indT):
         for i in checkU:
            if(x > i):
               if((not(i == 0 or i == 8 or i == 6)) or ((not(i == 6 and x % 8 ==7)) or ((i == 0 or i == 8) and x % 8 != 0))):
                  if(gme[x -(i + 1)] == opp):
                     temp = x - (i + 1)
                     while(temp >= i + 1):
                        if(((i == 6 and temp % 8 == 7)) or ((i == 0 or i == 8) and temp % 8 == 0)):
                           break
                        else:
                           if(gme[temp] != indT):
                              pass
                           else:
                              break   
                           if(gme[temp] == "."):
                              poss.add(temp)
                              break
                           else:   
                              temp = temp - (i + 1)
                           if(gme[temp] == "."):
                              poss.add(temp)
                              break
                           else:
                              pass   
         for i in checkD:
            if x < i[0]:
               if(((not(i[0] == 56 and x%8 == 0)) or ((i[0] == 63 or i[0] == 54) and x%8 != 7)) or (not(i[0] == 63 or i[0] == 54 or i[0] == 56))):
                  if(gme[x + i[1]] == opp):
                     temp = x + i[1]
                     while temp <= i[0]:
                        if(not(((i[0] == 63 or i[0] == 54) and temp%8 == 7) or ((i[0] == 56 and temp%8 == 0)))):
                           if(gme[temp] != indT):
                              pass
                           else:   
                              break
                           if(gme[temp] != "."):
                              pass
                           else:   
                              poss.add(temp)
                              break
                           temp = temp + i[1]
                           if(gme[temp] != "."):
                              pass
                           else:   
                              poss.add(temp)
                              break
                        else:
                           break
   return(poss)

def param(indT, gme, makemove):
   if(len(sys.argv) > 1):
      if(len(sys.argv) == 4):
         gme = sys.argv[1].lower().upper()
         indT = sys.argv[2].lower().upper()
         if(sys.argv[3][0].upper().lower() not in A1):
            makemove = int(sys.argv[3])  
         else:
            t1 = tblA1[sys.argv[3][0].upper().lower()]
            t2 = int(sys.argv[3][1])
            makemove = ((t2 - 1) * 8) + t1
      elif(len(sys.argv) == 2):
         if(len(sys.argv[1]) > 3):
            gme = sys.argv[1].lower().upper()
            indT = indTurn(gme)
            makemove = -1
         elif(len(sys.argv[1]) == 1 and (sys.argv[1].upper() == "O" or sys.argv[1].upper() == "X")):
            indT = sys.argv[1].lower().upper()
            gme = "...........................OX......XO..........................."
            makemove = -1
         else:
            if(sys.argv[1][0].upper().lower() not in A1):
               makemove = int(sys.argv[1])
            else:
               t1 = tblA1[sys.argv[1][0].upper().lower()]
               t2 = int(sys.argv[1][1])
               makemove = ((t2 - 1) * 8) + t1
            indT = "X"
            gme = "...........................OX......XO..........................."
      elif(len(sys.argv) == 3):
         if(len(sys.argv[1]) > 3):
            gme = sys.argv[1].lower().upper()
            if(len(sys.argv[2]) == 1 and (sys.argv[1].upper() == "O" or sys.argv[2].upper() == "X")):
               indT = sys.argv[2].lower().upper()
               makemove = -1
            else:
               if(sys.argv[2][0].lower() not in A1):
                  makemove = int(sys.argv[2])
               else:
                  t1 = tblA1[sys.argv[2][0].upper().lower()]
                  t2 = int(sys.argv[2][1])
                  makemove = ((t2 - 1) * 8) + t1
               indT = indTurn(gme)
         elif(len(sys.argv[1]) == 1 and (sys.argv[1].upper() == "O" or sys.argv[1].upper() == "X")):
            indT = sys.argv[1].lower().upper()
            if(len(sys.argv[2]) > 3):
               gme = sys.argv[2].lower().upper()
               makemove = -1
            else:
               if(sys.argv[2][0].lower() not in A1):
                  makemove = int(sys.argv[2])
               else:
                  t1 = tblA1[sys.argv[2][0].upper().lower()]
                  t2 = int(sys.argv[2][1])
                  makemove = ((t2 - 1) * 8) + t1
               gme = "...........................OX......XO..........................."
         else:
            if(sys.argv[1][0].lower() not in A1):
               makemove = int(sys.argv[2])
            else:
               t1 = tblA1[sys.argv[1][0].upper().lower()]
               t2 = int(sys.argv[1][1])
               makemove = ((t2 - 1) * 8) + t1
            if(len(sys.argv[2]) <= 3):
               indT = sys.argv[2].lower().upper()
               gme = "...........................OX......XO..........................."
            else:
               gme = sys.argv[2].lower().upper()
               indT = indTurn(gme)
   else:
      indT = "X"
      gme = "...........................OX......XO..........................."
      makemove = -1

   return(indT, gme, makemove)

def move(gme, p1, post, cnt):
   if(post not in possMoves(gme,p1) and post != -1):
      print("Move not possible.")
      cnt+=1
      if(cnt == 2):
         print("Game Over")
         return
      else:
         pass   
      print(indOpp(p1), end = "")
      print(" => ", end = "")
      print(makemove)
      move(gme, indOpp(p1), post, cnt)
   elif(post == -1):
      print("No move given.")
   else:
      gme[post] = p1
      checkD, checkU, opp = {(54,9),(55,8),(56,7),(63,1)}, {0,6,7,8}, indOpp(indT)
      for x in checkU:
         if(not(post <= x)):
            if((not(x == 0 or x == 8 or x == 6)) or (((x == 6 and post % 8 != 7)) or ((x == 0 or x == 8) and post % 8 != 0))):
               if(not(gme[post - (x + 1)] != opp)):
                  temp = post - (x + 1)
                  pos = 0
                  c = 0
                  while(not(temp < 0)):
                     print(temp)
                     if(not(((x == 0 or x == 8) and temp%8 == 0) or ((x == 6 and temp%8 ==7)))):
                        if(gme[temp] != "." and gme[temp == "."]):
                           c = 1
                           pos = temp
                           break
                        elif(gme[temp] == "."):
                           break
                        else:
                           pass   
                     else:
                        if(gme[temp] == p1):
                           c = 1
                           pos = temp
                        else:   
                           break
                     temp -= x + 1
                     print(temp)
                  pos = temp
                  while(pos != post):
                     if(c == 1):
                        pass
                     else:   
                        break
                     pos += x + 1
                     gme[pos] = p1
      for x in checkD:
         if(post < x[0]):
            if((((x[0] == 56 and post % 8 != 0)) or ((x[0] == 63 or x[0] == 54) and post % 8 != 7)) or (not(x[0] == 63 or x[0] == 54 or x[0] == 56))):
               if(not(gme[post + x[1]] != opp)):
                  temp = post + x[1]
                  pos = 0
                  c = 0
                  while(not(temp > 63)):
                     print(temp)
                     if(not(((x[0] == 56 and temp%8 == 0)) or ((x[0] == 63 or x[0] == 54) and temp%8 == 7))):
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
                  print("")

indT, gme, makemove = param(indT, gme, makemove)

print("")
print(gme)
print("")

gme = list(gme)
print("Possible Moves: ", end = "")
mvs = possMoves(gme,indT)
print(mvs)
temp = gme[:]

for x in mvs:
   temp[x] = "*"
    
print("")
print(indT, end = "")
print(" => ", end = "")
print(makemove)
print("")
printBoard("".join(temp))
print("")

move(gme,indT,makemove,0)
temp = gme[:]

print("")
print("".join(temp))
print("")

cntX = 0
cntO = 0
for x in temp:
   if(x == "X"):
      cntX = cntX + 1
   elif(x == "O"):
      cntO =cntO + 1
   else:
      pass

printBoard("".join(temp))
print("")
print("X: " , end = "")
print(cntX, end = "")
print(" O: ", end = "")
print(cntO)