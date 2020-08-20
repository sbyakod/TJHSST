#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:16:54 2017

@author: Sharath Byakod
"""

def swap(string, a, b):
    a, b = int(a), int(b)
    return string[:a] + string[b] + string[a+1:b] + string[a] + string[b+1:]

def getParent(vertex):
    return dctAlreadySeen.get(vertex)
def printThis():
    vertex = getParent("end")
    vertexList = [] 
    while vertex != "":
        vertexList.insert(0, vertex)
        vertex = getParent(vertex)
    for item in vertexList[:]:
        print(item[0] + item[1] + item[2] + "\n" + item[3] + item[4] + item[5] + "\n" +item[6] + item[7] + item[8])
        print()
    print("Steps: " + str(len(vertexList) - 1))
def printThis2():
    for i in range(1, 32):
        print(str(i) + ": " + str(len(dctAlreadySeen[i])))

goalState = "12345678_"
dctAlreadySeen = {0: [goalState]}
setCheck = {goalState}
for i in range(1, 32):
    dctAlreadySeen.setdefault(i,[])
    for j in dctAlreadySeen[i-1]:
        vertex = str(j)
        a = vertex.index("_")
        if a > 2:
            child = swap(vertex, a-3, a)
            if child not in setCheck:
                dctAlreadySeen[i].append(child)
                setCheck.add(child)
        if a < 6:
            child = swap(vertex, a, a+3)
            if child not in setCheck:
                dctAlreadySeen[i].append(child)
                setCheck.add(child)
        if a % 3 < 2:
            child = swap(vertex, a, a+1)
            if child not in setCheck:
                dctAlreadySeen[i].append(child)
                setCheck.add(child)
        if a % 3 > 0:
            child = swap(vertex, a-1, a)
            if child not in setCheck:        
                dctAlreadySeen[i].append(child)
                setCheck.add(child)
printThis2()
print()

maxStep = 31
for i in range(31, 0, -1):
    if len(dctAlreadySeen[i]) != 0:
        maxStep = i
        break
        
print("Max steps puzzle: " + dctAlreadySeen[maxStep][0])

 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:33:35 2017
Compeletly working
@author: dannykim


inputStr = dctAlreadySeen[maxStep][0]
parseMe = [inputStr]
dctAlreadySeen = {inputStr: ""}

while len(parseMe) != 0:
    vertex = str(parseMe.pop(0))
    if vertex == goalState:
        print()
        print("Solution")
        dctAlreadySeen["end"] = goalState
        printThis()
        exit()
    a = vertex.index("_")
    if a > 2:
        child = swap(vertex, a-3, a)
        if child not in dctAlreadySeen:
            parseMe.append(child)
            dctAlreadySeen[child] = vertex
    if a < 6:
        child = swap(vertex, a, a+3)
        if child not in dctAlreadySeen:
            parseMe.append(child)
            dctAlreadySeen[child] = vertex
    if a % 3 < 2:
        child = swap(vertex, a, a+1)
        if child not in dctAlreadySeen:
            parseMe.append(child)
            dctAlreadySeen[child] = vertex
    if a % 3 > 0:
        child = swap(vertex, a-1, a)
        if child not in dctAlreadySeen:        
            parseMe.append(child)   
            dctAlreadySeen[child] = vertex

print("No Solution")
"""
"""
