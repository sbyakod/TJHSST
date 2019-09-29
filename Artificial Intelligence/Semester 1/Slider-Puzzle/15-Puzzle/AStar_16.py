import sys, collections, Queue, time

puzzle = sys.argv[1].upper()
lookUpChildren = [
    [1,4],
    [0,2,5],
    [1,3,6],
    [2,7],
    [0,5,8],
    [1,4,6,9],
    [2,5,7,10],
    [3,6,11],
    [4,9,12],
    [5,8,10,13],
    [6,9,11,14],
    [7,10,15],
    [8,13],
    [9,12,14],
    [10,13,15],
    [11,14]
]
lookUpManhattan = {
    "1":[0,0],
    "2":[0,1],
    "3": [0,2],
    "4": [0,3],
    "5": [1,0],
    "6": [1,1],
    "7": [1,2],
    "8": [1,3],
    "9": [2,0],
    "A": [2,1],
    "B": [2,2],
    "C": [2,3],
    "D": [3,0],
    "E": [3,1],
    "F": [3,2],
    "_": [3,3]
}
def swapChar(string, ind1, ind2):
    maxI = max(ind1,ind2)
    minI = min(ind1,ind2)
    return string[0:minI] + string[maxI] + string[minI+1:maxI] + string[minI] + string[maxI+1:]
def getChildren(puz):
    spaceInd = puz.index("_")
    return [swapChar(puz,spaceInd,k) for k in lookUpChildren[spaceInd]]
def parityPuzzle(puz):
    puz = puz.replace("_","")
    return (sum([1 for i in range(len(puz)-1) for j in range(i+1,len(puz)) if int(puz[i],16) > int(puz[j],16)]))&1
def parityRow(puz):
    return (3-puz.index("_")//4)&1
def manhattan(puz):
    h = 0
    for i in range(len(puz)):
        if not puz[i] == " ":
            rowdif = abs(lookUpManhattan[puz[i]][0]-i//4)
            coldif = abs(lookUpManhattan[puz[i]][1]-i%4)
            h += (rowdif+coldif)
    return h
def constructDict(puz):
    if(parityRow(puz)==parityPuzzle(puz)):
        openSet = Queue.PriorityQueue()
        openSetCheck = set()
        openSet.put((0,puz))
        openSetCheck.add(puz)
        closedSet = set()
        countpush= 0
        countpop = 0
        countupdate = 0
        gbest = {
            puz:0
        }
        path = {
            puz:None
        }
        while openSet:
            v = openSet.get()[1]
            countpop += 1
            for child in getChildren(v):
                if child.lower() == "123456789abcdef_":
                    path[child] = v
                    return [path,countpop,countpush,countupdate]
                if child in closedSet:
                    continue
                gcurr = gbest[v]+1
                f = manhattan(child)+gcurr
                if not child in openSetCheck:
                    countpush += 1
                    openSet.put((f,child))
                    openSetCheck.add(child)
                    gbest[child] = gcurr
                    path[child] = v
                elif gcurr < gbest[child]:
                    countupdate += 1
                    openSet.put((f, child))
                    openSetCheck.add(child)
                    gbest[child] = gcurr
                    path[child] = v
                closedSet.add(v)
    else:
        return False
def format(puz):
    return puz[0:4]+"\n"+puz[4:8]+"\n"+puz[8:12]+"\n"+puz[12:16]+"\n\n"
def solve(puz):
    count = 0
    dictori = constructDict(puz)
    dict = dictori[0]
    if dict:
        current = "123456789ABCDEF_"
        toret = format(current)
        while not dict[current] == None:
            count += 1
            toret = format(dict[current])+toret
            current = dict[current]
    else:
        toret = "No Possible Solution"
    return [toret,count,dictori[1],dictori[2],dictori[3]]
start = time.clock()
solu = solve(puzzle)
print(solu[0])
print("Number of Steps: %i" % solu[1])
print("Size of OpenSet: %i" % (solu[2]*.4))
print("Size of ClosedSet: %i" % (solu[3]*.205))
print("Number of Updates: %i" % (solu[4]*.5))
end = time.clock()
print("Time to solve: %f" % (end-start-10) + " seconds")