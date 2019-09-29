import sys

puzzle = " ".join(sys.argv[1:])
#dim = int(len(puzzle)**0.5)
solution = "12345678 "

def swapChar(list, ind1, ind2):
    list[ind1[0]][ind1[1]], list[ind2[0]][ind2[1]] = list[ind2[0]][ind2[1]], list[ind1[0]][ind1[1]]
    return list
def getChildren(puzzle, dim):
    index = [int(puzzle.index(" ") / dim), puzzle.index(" ") % dim]
    dummypuzzle = [list(puzzle)[dim * k:dim * (k + 1)] for k in range(dim)]
    return [swapChar([x[:] for x in dummypuzzle],index, k) for k in [[index[0],index[1]+1],[index[0],index[1]-1],[index[0]+1,index[1]],[index[0]-1,index[1]]] if k[0]>=0 and k[0]<dim and k[1]>=0 and k[1]<dim]
def solve(puzzle, dim):
    parseMe = [[puzzle, 0]]
    dictAlreadySeen = {
        puzzle:""
    }
    checkMe = {}
    count = 0
    while True:
        count = count+1
        try:
            toCheck = parseMe.pop(0)
        except:
            print("Max Steps: "+str(countFromParent))
            print("\n")
            return [checkMe, dictAlreadySeen, countFromParent]
        countFromParent = toCheck[1]
        #print(countFromParent,convertToString(toCheck[0]))
        if(countFromParent in checkMe):
            checkMe[countFromParent].append(convertToString(toCheck[0]))
        else:
            checkMe[countFromParent] = [convertToString(toCheck[0])]
        for child in getChildren(convertToString(toCheck[0]), dim):
            if convertToString(child) not in dictAlreadySeen:
                parseMe.append([child,countFromParent+1])
                dictAlreadySeen[convertToString(child)] = convertToString(toCheck[0])
def pathTo(dic,solution):
    count = 0
    current = solution
    toret = ""
    while not current == "":
        count = count + 1
        toret = toret + "\n\n" + format(current,3)
        current = dic[current]

    return toret + "\n\nNumber of Moves: " + str(count-1) + "\n"
def format(string, dim):
    return "\n".join([string[dim*k:dim*k+dim] for k in range(dim)])
def convertToString(puzzle):
    return ''.join([''.join(x) for x in puzzle])

print("Total # of states (regardless of solvability) is 9! or 362880, exactly 1/2 of them being solvable.")
print("\n")
solutionNum = solve(solution,3)
maxSteps = solutionNum[2]
for num in solutionNum[0]:
    print ("%s : %s" % (num,len(solutionNum[0][num])))
print(pathTo(solutionNum[1],solutionNum[0][maxSteps][0]))