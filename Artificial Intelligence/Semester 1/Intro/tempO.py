from itertools import product
import time
import sys
         
def possMoves(brd, pce, rstart, cstart):
   mvs = set()
   opp = 'X' if pce == 'O' else 'O'
   for incr, incc in [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:  
      r, c = rstart + incr, cstart + incc 
      while brd[12 * r + c] == opp:
         r, c = r + incr, c + incc
      if brd[12 * r + c] == '.' and (abs(r - rstart) >= 2 or abs(c - cstart) >= 2):
         mvs.add( (r, c) )
   return mvs
                    
brd = ['*' for i in range(144)]
inp = [c.upper() for c in sys.argv[1]] if len(sys.argv) > 1 else "...........................OX......XO..........................."
tkn = sys.argv[2].upper() if len(sys.argv) > 2 else 'O' if len([c for c in inp if c=='.']) % 2 else 'X'
x = set()
o = set()
for i, j in product(range(8), range(8)):
   brd[12 * (i + 2) + j + 2] = inp[8 * i + j]
   if inp[8 * i + j] == 'X':
      x.add((i + 2, j + 2));
   elif inp[8 * i + j] == 'O':
      o.add((i + 2, j + 2));
vld = set()
for r, c in x if tkn == 'X' else o:
   vld = vld | possMoves(brd, tkn, r, c)   
##### print set of moves #####
print inp
print("Valid Moves:"),
if(not vld):
   print("None")
for m in vld: 
   print str(8 * (m[0] - 2) + m[1] - 2),