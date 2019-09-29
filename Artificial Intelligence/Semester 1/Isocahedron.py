isoca = {0:(4,1,6),1:(0,2,8),2:(1,3,10),3:(2,4,12),4:(0,3,14),
     5:(14,6,15),6:(5,7,0),7:(6,8,16),8:(7,9,1),9:(8,10,17),
     10:(9,11,2),11:(10,12,18),12:(11,13,3),13:(12,14,19),
     14:(13,5,4),15:(19,16,5),16:(15,17,7),17:(16,18,9),
     18:(17,19,11),19:(18,15,13)}
def bruteForce(pzl, size):
    if isInvalid(pzl, size):
        return ""
    if isSolved(pzl, size):
        return pzl
    empties = [k for k in range(len(pzl)) if pzl[k] =="."]
    for i in empties:
        subPzl = pzl[:i] + "1" + pzl[i+1:]
        bF = bruteForce(subPzl, size)
        if bF: 
            return bF
    return ""
def isInvalid(pzl, size):
    for i in isoca:
        for j in isoca[i]:
            if pzl[i] is "1" and pzl[j] is "1":
                return True
    if oneCount(pzl) > size:
        return True
    return False
def isSolved(pzl, size):
    if oneCount(pzl) == size:
        return True
    return False
def oneCount(pzl):
    oneCount = 0
    for i in pzl:
        if i == "1":
            oneCount +=1
    return oneCount
def printThis(solution):
    if solution == "":
        print("No possible solution")
    else:
        toReturn = ""
        for i in range(len(solution)):
            if(solution[i] == '1'):
                toReturn += str(i) + " "
        print(toReturn)
import sys
size = sys.argv[1]
start = "...................."
print("Number of faces: " + size)
solution = bruteForce(start, int(size))
printThis(solution)