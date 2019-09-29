from random import randint
from time import time
import sys

def build(line):
  puz = []
  i = 0
  while i < 9:
    j = 0
    temp = []
    while j < 9:
      temp.append(line.pop(0))
      j = j + 1
    puz.append(temp)
    i = i +1
  return puz

def neighbors(row, col):
  neighbors = set()
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if i == int(row) and j != int(col):
	neighbors.add(str(i) + ' ' + str(j))
      elif i != int(row) and j == int(col):
	neighbors.add(str(i) + ' ' + str(j))
      elif i/3 == int(row)/3 and j/3 == int(col)/3:
	if i != int(row) and j != int(col):
	  neighbors.add(str(i) + ' ' + str(j))
      j = j + 1
    i = i + 1
  return  neighbors   

def allNeigh(puz):
  allN = []
  i = 0
  while i < 9:
    j = 0
    temp =[]
    while j < 9:
      temp.append(neighbors(i, j))
      j = j +1
    allN.append(temp)
    i = i + 1
  return allN
  
def displayPuzzle(puz):
  for row in puz:
    print(" ".join(row))
  print
 
def needToSolve(puz):
  empty = set()
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if puz[i][j] == '.':
	empty.add(str(i) + ' ' + str(j))
      j = j + 1
    i = i + 1
  return empty
  
  
def assign(puz, nList, empty):
  assigned = {}
  possible = {}
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if puz[i][j] != '.':
	assigned[str(i) + ' ' + str(j)] = puz[i][j]
	possible[str(i) + ' ' + str(j)] = []
      j = j + 1
    i = i + 1

  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if puz[i][j] == '.':
    	possible[str(i) + ' ' + str(j)] = {'1','2','3','4','5','6','7','8','9'}
	possible[str(i) + ' ' + str(j)] = possibleNumbers(possible, str(i) +  ' '+ str(j), nList, assigned)
      j = j +1
    i = i + 1
    
  current = '0 0'
  i = 0
  j = 0
  while current in empty:
    if j%8 == 0:
      i = i + 1
      j = 0
    else:
      j = j +1
    current = str(i) + ' ' + str(j)  
  print assignNumber(puz,nList,assigned,possible,current)
  #
  # update puz from assigned
  #
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      puz[i][j] = str(assigned[str(i) + ' ' + str(j)])
      j = j +1
    i = i + 1
    
def possibleNumbers(possible, current, nList, assigned):
  n = []
  row = int(current[0])
  col = int(current[-1])
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      if i == row and j == col:
	n = nList[i][j]
      j = j + 1
    i = i + 1
  nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
  for neighbor in n:
    if neighbor in assigned:
      if assigned[neighbor] in nums:
	nums.remove(assigned[neighbor])
  return nums
  
def pickNext(current, possible, assigned):
  lowest = current
  val = 10
  i = 0
  while i < 9:
    j = 0
    while j < 9:
      space = str(i) + ' '+ str(j)
      if space in assigned.keys():
	pass
      elif len(possible[space]) < val and len(possible[space]) >= 0:
	lowest = space
	val = len(possible[space])
      j = j + 1
    i = i + 1
  return lowest
   
def assignNumber(puz, nList, assigned, possible, current):
  if len(assigned) == 81:
    return True
  else:
    nextspace = pickNext(current, possible, assigned)
    if nextspace == current:
      return False
    for num in possible[nextspace]:
      assigned[nextspace] = num
      n = neighbors(nextspace[0], nextspace[-1])
#      p = possible.copy()
      for item in n:
	if item in assigned:
	  continue
	possible[item] = possibleNumbers(possible, item, nList, assigned)
      #
      retval=assignNumber(puz,nList,assigned,possible,nextspace)
      if retval == True:
	return True
      #
      # undo
      #
      #for item in n:
	#possible[item] = p[item]
      del assigned[nextspace]
      for item in n:
	if item in assigned:
	  continue
	possible[item] = possibleNumbers(possible, item, nList, assigned)
      #
    #del assigned[nextspace]
  return False
    
    
def bruteForce(file):
  puz = []
  user = file
  file=open(user,'r').read().split()
  num = 1
  tic = time()
  while num < 51:
    #print 'Puzzle #' + str(num) 
    puz = build(list(file.pop(0)))
    nList = allNeigh(puz)
    empty = needToSolve(puz)
    #displayPuzzle(puz)
    #print "Now to bruteForce..."
    assign(puz, nList, empty)
    displayPuzzle(puz)
    num = num + 1
  i = 51
  while i < 122:
    file.pop(0)
    i = i + 1
  num = 123
  tic = time()
  while num < 130:
    #print 'Puzzle #' + str(num) 
    puz = build(list(file.pop(0)))
    nList = allNeigh(puz)
    empty = needToSolve(puz)
    #displayPuzzle(puz)
    #print "Now to bruteForce..."
    assign(puz, nList, empty)
    displayPuzzle(puz)
    num = num + 1
  print 'Overall Time: ' + (str(time() - tic) + ' seconds')
	 
  
bruteForce(sys.argv[1])