dodeca = {0:(1,2,3,4,5),1:(0,2,6,7,5),2:(0,3,1,7,8),3:(0,2,4,8,9),4:(0,3,5,9,10),
     5:(0,4,1,10,6),6:(11,1,5,10,7),7:(11,6,8,1,2),8:(11,2,3,7,9),9:(11,3,4,8,10),
     10:(11,4,5,9,6),11:(6,7,8,9,10)}
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
    for i in dodeca:
        for j in dodeca[i]:
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
        print toReturn
import sys
size = sys.argv[1]
start = "............"
print("Number of faces: " + size)
solution = bruteForce(start, int(size))
printThis(solution)