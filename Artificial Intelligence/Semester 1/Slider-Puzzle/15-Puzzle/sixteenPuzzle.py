import sys
import time
import Queue

starttime = time.time()
#use a lookup table to precompute the spaces
tbl = {0:[1,4],1:[0,2,5],2:[1,3, 6],3:[2,7],4:[0,5,8],5:[1,4,6,9],6:[2,5,6,10],7:[3, 11, 6],8:[4, 9, 12], 9:[5,8,10,13], 10:[6,9,11,14], 11:[7,10,15], 12:[8,13], 13:[9,12, 14], 14:[10, 13, 15], 15:[11,14]}
fin = sys.argv[1]

indexCoors = {0: [0,0], 1: [1,0], 2: [2,0], 3: [3,0], 4: [0,1], 5: [1,1], 6: [2,1], 7: [3,1], 8: [0,2], 9: [1,2], 10: [2,2], 11: [3,2], 12: [0,3], 13: [1,3], 14: [2,3], 15: [3,3]}
letCoors = {"A": [0,0], "B": [1,0], "C": [2,0], "D": [3,0], "E": [0,1], "F": [1,1], "G": [2,1], "H": [3,1], "I": [0,2], "J": [1,2], "K": [2,2], "L": [3,2], "M": [0,3], "N": [1,3], "O": [2,3], "_": [3,3]}


def mDistance(string, index):
    letter = string[index]
    if(indexCoors[index][0] == letCoors[letter][0] and indexCoors[index][1] == letCoors[letter][1]):
        return 0
    else:
        count = abs(indexCoors[index][0] - letCoors[letter][0]) + abs(indexCoors[index][1] - letCoors[letter][1])
        return count

def totalMDistance(string):
    count = 0
    for i in range(0, 16):
        count += mDistance(string, i)
    return count

def removeBlank(myStr):
    return myStr.replace("_", "")

def inversionCt(myStr):
    myStr = removeBlank(myStr)
    return sum([1 for i in range(len(myStr)-1) for j in range(i+1, len(myStr)) if myStr[i]>myStr[j]])

def rowDif(myStr):
    index = myStr.index("_")
    if(index >= 0 and index < 4):
        return 3
    if(index >= 4 and index < 8):
        return 2
    if(index >= 8 and index < 12):
        return 1
    else:
        return 0

def parity(num):
    return num % 2

def retSwitches(myStr):
    ret = []
    index = myStr.index("_")
    for i in tbl[index]:
        ret.append(swap(myStr, index, i))
    return ret

def swap(str, one, two):
    myStr = list(str)
    temp = myStr[two]
    myStr[two] = myStr[one]
    myStr[one] = temp
    return myStr

def checkSol(myStr):
    return (parity(inversionCt(myStr)+rowDif(myStr)) == 0)

def pRight(string):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    lis = list(string)
    for i in range(0, 4):
        line1 += lis[i] + " "
    for i in range(4, 8):
        line2 += lis[i] + " "
    for i in range(8, 12):
        line3 += lis[i] + " "
    for i in range(12, 16):
        line4 += lis[i] + " "
    print ""
    print line1
    print line2
    print line3
    print line4
    print ""

def pop(md):
    count = 0
    index = 0
    lowest = 10000
    for i in md:
        if(i < lowest):
            i = lowest
            index = count
        count += 1
    print index
    return index

def toString(array):
    ret = ""
    arr = array
    for i in array:
        ret = ret + i
    return ret

def solve(fin):
    goal = "ABCDEFGHIJKLMNO_"
    alreadySeen = {}
    if(checkSol(fin)):
        if(fin == goal):
            return;
        else:
            pq = Queue.PriorityQueue()
            b = 0
            pq.put((totalMDistance(fin), fin, 0))
            thing = ""
            times = 0
            while(not pq.empty()):
                current = pq.get()
                current0 = current[0]
                pzzls = retSwitches(toString(current[1]))

                for i in pzzls:
                    temp = toString(i)
                    if(temp == goal):
                        b = 1
                        alreadySeen[temp] = toString(current[1])
                        break;
                    else:
                        if(temp not in alreadySeen.keys()):
                            alreadySeen[temp] = toString(current[1])
                            distance = totalMDistance(temp)
                            pq.put((distance + current[2], toString(temp), current[2]+1))
                times += 1
                if(b == 1):
                    break;
        print("Solved")
        print("Number of times popped: " + str(times))
        return alreadySeen
    else:
        print("No Solution")
        return None

def showSteps(dict, fin):
   if dict == None:
       return None
   goal = "ABCDEFGHIJKLMNO_"
   parent = dict.get(goal)
   steps = []
   steps.append(goal)
   steps.append(parent)
   while(parent != fin):
       parent = dict.get(parent)
       steps.append(parent)
   steps = steps[::-1]
   if(fin == "ABCDEFGHIJKLMNO_"):
       pRight(fin)
       print("Steps: 0")
   else:
       for i in steps:
           pRight(i)
       print("Steps: " + str(len(steps)-1))
showSteps(solve(fin), fin)
endtime = time.time()
print("Time to Solve: " + str(endtime - starttime))