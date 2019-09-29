from math import *
import sys, time
from tkinter import *
from itertools import permutations

def distance(x1,y1,x2,y2):
   R   = 6371 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

if len(sys.argv) == 1:
    file = 'KAD.txt'
else:
    file = sys.argv[1]
vertices = [line for line in open(file)]
numVertices = int(vertices.pop(0))
vertices = [(float(coor.split()[0])/1000.0, float(coor.split()[1])/1000.0) for coor in vertices]

permwidth = 8

distances = {}
for i in vertices:
    distances[i] = {}
    for j in vertices:
        if i == j: continue
        distances[i][j] = distance(i[0],i[1],j[0],j[1])

minx, miny, maxx, maxy = 99999999, 99999999, -99999999, -99999999
for i in vertices:
    if i[0] < minx: minx = i[0]
    if i[1] < miny: miny = i[1]
    if i[0] > maxx: maxx = i[0]
    if i[1] > maxy: maxy = i[1]
middle = (maxy+miny)/2.0
minx -= 0.05
miny -= 0.05
maxx += 0.05
maxy += 0.05

coordinates = {i:((600.0/(maxx-minx))*(i[0]-minx), 600.0-(600.0/(maxy-miny))*(i[1]-miny)) for i in vertices}

root1 = Tk()
root2 = None
root3 = None

def getDistance(path):
    if len(path) == numVertices:
        return sum([distances[vertices[path[i]]][vertices[path[(i+1)%len(path)]]] for i in range(len(path))])
    else:
        return sum([distances[vertices[path[i]]][vertices[path[i+1]]] for i in range(len(path)-1)])

def exit1(event):
    global root2
    root1.destroy()
    root2 = Tk()
    pt2()

def exit2(event):
    global root3
    root2.destroy()
    root3 = Tk()
    pt3()

def exit3(event):
    root3.destroy()

def uncross(path):
    updated = path[:]
    for i in range(len(path)):
        for j in range(i+1, len(path)):
            seg1, seg2 = (vertices[path[i]], vertices[path[(i+1)%len(path)]]), (vertices[path[j]], vertices[path[(j+1)%len(path)]])
            if distances[seg1[0]][seg1[1]] + distances[seg2[0]][seg2[1]] > distances[seg1[0]][seg2[0]] + distances[seg1[1]][seg2[1]]:
                updated = updated[:i+1] + updated[i+1:j+1][::-1] + updated[j+1:]
                return updated, False
    return updated, True

def permute(nodes):
    path = nodes[:]
    for i in range(len(path)-permwidth-1):
        og = path[i:i+permwidth+2]
        ogDist = getDistance(og)
        pathToDistance = {tuple(og):ogDist}
        perms = [list(j) for j in permutations(path[i+1:i+permwidth+1], permwidth)][1:]
        for k in perms: pathToDistance[tuple([og[0]] + k + [og[-1]])] = getDistance([og[0]] + k + [og[-1]])
        if perms:
            minperm = (list(min(pathToDistance, key=pathToDistance.get)))
            path = path[0:i] + minperm + path[i+permwidth+2:]
    return path

def pt1():
    distance = 0
    path = []
    canvas1 = Canvas(root1, width=600,height=600, background="white")
    canvas1.pack()
    #for vertex in vertices:
         #canvas1.create_oval(coordinates[vertex][0]-5, coordinates[vertex][1]+5,coordinates[vertex][0]+5, coordinates[vertex][1]-5, fill="black",width=1)
    for i in range(len(vertices)):
        path.append(str(i))
        distance += distances[vertices[i]][vertices[(i+1)%numVertices]]
        canvas1.create_line(coordinates[vertices[i]][0],coordinates[vertices[i]][1], coordinates[vertices[(i+1)%numVertices]][0], coordinates[vertices[(i+1)%numVertices]][1], fill="blue",width=1)
    print("Original path:", ' '.join(path))
    print("Distance:", distance, "km")
    root1.bind("<Key>", exit1)
    root1.mainloop()

def pt2():
    distance = 0
    path = [i for i in range(numVertices)]
    canvas2 = Canvas(root2, width=600,height=600, background="white")
    canvas2.pack()
    count = 0
    while(True):
        path, check = uncross(path)
        count += 1
        if check: break
    #for vertex in vertices:
         #canvas2.create_oval(coordinates[vertex][0]-5, coordinates[vertex][1]+5,coordinates[vertex][0]+5, coordinates[vertex][1]-5, fill="black",width=1)
    for i in range(len(path)):
        distance += distances[vertices[path[i]]][vertices[path[(i+1)%numVertices]]]
        canvas2.create_line(coordinates[vertices[path[i]]][0],coordinates[vertices[path[i]]][1], coordinates[vertices[path[(i+1)%numVertices]]][0], coordinates[vertices[path[(i+1)%numVertices]]][1], fill="blue",width=1)
    path = [str(i) for i in path]
    print("Unscrambled path:", ' '.join(path))
    print("Distance:", distance, "km")
    root2.bind("<Key>", exit2)
    root2.mainloop()

def pt3():
    global permwidth
    if file != 'KAD.txt': permwidth = 5
    distance, newDistance = 0, sys.maxsize
    path = [i for i in range(numVertices)]
    canvas3 = Canvas(root3, width=600,height=600, background="white")
    canvas3.pack()
    count = 0
    while(True):
        path, check = uncross(path)
        if check: break
    distance = getDistance(path)
    while(newDistance != distance):
        path = uncross(permute(path))[0]
        distance = newDistance
        newDistance = getDistance(path)
    #for vertex in vertices:
         #canvas3.create_oval(coordinates[vertex][0]-5, coordinates[vertex][1]+5,coordinates[vertex][0]+5, coordinates[vertex][1]-5, fill="black",width=1)
    for i in range(len(path)):
        canvas3.create_line(coordinates[vertices[path[i]]][0],coordinates[vertices[path[i]]][1], coordinates[vertices[path[(i+1)%numVertices]]][0], coordinates[vertices[path[(i+1)%numVertices]]][1], fill="blue",width=1)
    path = [str(i) for i in path]
    print("Permuted path:", ' '.join(path))
    print("Distance:", newDistance, "km")
    root3.bind("<Key>", exit3)
    root3.mainloop()

pt1()