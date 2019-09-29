import math
import time
from Tkinter import *

def calcd(y1,x1, y2,x2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 3958.76 # miles = 6371 km
   y1 *= math.pi/180.0
   x1 *= math.pi/180.0
   y2 *= math.pi/180.0
   x2 *= math.pi/180.0
   return math.acos( math.sin(y1)*math.sin(y2) + math.cos(y1)*math.cos(y2)*math.cos(x2-x1) ) * R

sTime = time.time()
dict = {}
thing = {}
array = []
file_object = open("romNodes.txt", "r")
graph = [0.0 for i in range(0, 20)]
cout = 0
lines = 0
for line in file_object:
	arr = line.split(" ")
	array.append(arr[0])
	dict[arr[0]] = [(float)(arr[1]), (float)(arr[2])]
	thing[arr[0]] = cout
	graph[cout] = [0.0 for i in range(0, 20)]
	cout = cout + 1
	lines = lines + 1
totaldistance = 0.0
file2 = open("romEdges.txt", "r")


for line in file2:
	arr = line.split(" ")
	y1 = dict[arr[0]][1]
	x1 = dict[arr[0]][0]
	y2 = dict[arr[1][0:1]][1]
	x2 = dict[arr[1][0:1]][0]
	distance = calcd(x1,y1,x2,y2)
	graph[thing[arr[0]]][thing[arr[1][0:1]]] = distance
	graph[thing[arr[1][0:1]]][thing[arr[0]]] = distance
	totaldistance += distance

top = Tk()
h = 800 
w = 800 
C = Canvas(top, bg = 'blue', height = h, width = w)
	
array2 = []
temp = lines-1
for i in range(0, lines):
	array2.append(array[temp])
	temp = temp-1

count1 = 0
for i in array:
	count2 = 19
	for j in array2:
		if(graph[count1][count2] != 0.0 and count2 >= 0):
			x1 = (dict[i][0])*80-1500-100-200-200-300-200-200-200
			y1 = (dict[i][1])*80-800-200-200-200-200
			x2 = (dict[j][0])*80-1500-100-200-200-300-200-200-200
			y2 = (dict[j][1])*80-800-200-200-200-200
			line = C.create_line(y1, 1000-x1, y2, 1000-x2,fill = 'white', width = 1)
		count2 = count2 - 1
	count1 = count1 + 1


print("Total Distance: " + str(totaldistance) + " miles")
constructTime = time.time() - sTime
print("Time to run: " + str(constructTime))
C.pack()
top.mainloop()

'''
from Tkinter import *
from math import pi , acos , sin , cos
import Queue

class rrUtil:
    #nodes contains city abbr. and its location [x,y]
    #edges contains city abbr. and a list of edges [a, b, c, ...]
    #names contains city abbr. and its full name

    #defines nodes, edges, names, minx, miny, maxx, maxy, xrange, and yrange
    def __init__(self, nodeFile, edgeFile, namesFile, xscale, yscale=0, xroom=0, yroom=0):
        self.nodes = {}
        self.edges = {}
        self.names = {}

        x = open(nodeFile, "r").read().split("\n")

        self.minx = float(x[0].split(" ")[2])
        self.maxx = float(x[0].split(" ")[2])
        self.miny = float(x[0].split(" ")[1])
        self.maxy = float(x[0].split(" ")[1])

        for i in range(len(x)):
            nodeInfo = x[i].split(" ")
            xc = float(nodeInfo[2])
            yc = float(nodeInfo[1])

            self.minx = min(self.minx, xc)
            self.maxx = max(self.maxx, xc)
            self.miny = min(self.miny, yc)
            self.maxy = max(self.maxy, yc)

            self.nodes[nodeInfo[0]] = [xc, yc]
            self.edges[nodeInfo[0]] = []

        x = open(namesFile, "r").read().split("\n")
        for line in x:
            keys = line.split(" ",1)
            self.names[keys[1]] = keys[0]

        x = open(edgeFile, "r").read().split("\n")
        for i in range(len(x)):
            nodeInfo = x[i].split(" ")
            if self.edges[nodeInfo[0]]:
                self.edges[nodeInfo[0]].append(nodeInfo[1])
            else:
                self.edges[nodeInfo[0]] = [nodeInfo[1]]
            if self.edges[nodeInfo[1]]:
                self.edges[nodeInfo[1]].append(nodeInfo[0])
            else:
                self.edges[nodeInfo[1]] = [nodeInfo[0]]

        self.xrange = self.maxx-self.minx
        self.yrange = self.maxy-self.miny

        if not yroom:
            self.yroom = xroom
        else:
            self.yroom = yroom
        if not yscale:
            self.yscale = xscale
        else:
            self.yscale = yscale

        self.xscale = xscale
        self.xroom = xroom

        self.master = Tk()
        self.w = Canvas(self.master, width=self.xscale * self.xrange + self.xroom, height=self.yscale * self.yrange + self.yroom)
        self.w.pack()

    #graphs edges given an xscale, yscale, xroom and yroom (space between edge and beginning of graph)
    def graph_all_edges(self):
        self.w.delete("all")
        for coord in self.edges:
            for edge in self.edges[coord]:
                self.w.create_line((self.nodes[coord][0] - self.minx) * self.xscale + self.xroom // 2,
                              (self.maxy - self.nodes[coord][1]) * self.yscale + self.yroom // 2,
                              (self.nodes[edge][0] - self.minx) * self.xscale + self.xroom // 2,
                              (self.maxy - self.nodes[edge][1]) * self.yscale + self.yroom // 2)

    #graphs a single edge
    def graph_edge(self, citya, cityb, color="black", width = 1):
        self.w.create_line((self.nodes[citya][0] - self.minx) * self.xscale + self.xroom // 2,
                           (self.maxy - self.nodes[citya][1]) * self.yscale + self.yroom // 2,
                           (self.nodes[cityb][0] - self.minx) * self.xscale + self.xroom // 2,
                           (self.maxy - self.nodes[cityb][1]) * self.yscale + self.yroom // 2,
                           fill = color,
                           width = width)

    #graphs a point
    def graph_point(self,citya,color="black"):
        r=1
        self.w.create_oval((self.nodes[citya][0] - self.minx) * self.xscale + self.xroom // 2-r,(self.maxy - self.nodes[citya][1]) * self.yscale + self.yroom // 2+r,(self.nodes[citya][0] - self.minx) * self.xscale + self.xroom // 2+r,(self.maxy - self.nodes[citya][1]) * self.yscale + self.yroom // 2-r, fill = color)

    #runs graphic
    def mainloop(self):
        mainloop()

    #graphs text on canvas at point
    def graph_text(self, citya, text):
        self.w.create_text((self.nodes[citya][0] - self.minx) * self.xscale + self.xroom // 2,
                           (self.maxy - self.nodes[citya][1]) * self.yscale + self.yroom // 2,
                           anchor = SE,
                           font = ("Purisa",20),
                           text = text,
                           fill = "purple")

    #clears canvas
    def graph_clear(self):
        self.w.delete("all")

    #returns the spherical distance between two nodes given ciy abbr.
    def calcd(self,citya,cityb):
        x1 = self.nodes[citya][0]
        y1 = self.nodes[citya][1]
        x2 = self.nodes[cityb][0]
        y2 = self.nodes[cityb][1]

        R = 3958.76

        y1 *= pi / 180.0
        x1 *= pi / 180.0
        y2 *= pi / 180.0
        x2 *= pi / 180.0

        return acos(sin(y1) * sin(y2) + cos(y1) * cos(y2) * cos(x2 - x1)) * R

    #returns the dist. of all edges within the graph
    def dist_all_edges(self):
        dist = 0
        closed = set()
        for node in self.nodes:
            for edge in self.edges[node]:
                if not edge in closed:
                    dist += self.calcd(node,edge)
            closed.add(node)
        return dist

    #returns a dict. in which the path from point b to point a is optimal
    def path_between_edges(self, citya, cityb, graph = False):

        openSet = Queue.PriorityQueue()
        closedSet = set()
        seen = {}
        path = {citya:None}
        gbest = {citya:0}

        openSet.put((0,citya))
        io = 0
        while openSet:
            v = openSet.get()[1]
            for neighbor in self.edges[v]:
                if neighbor == cityb:
                    path[neighbor] = v
                    seen[neighbor] = v
                    closedSet.add(v)

                    if graph:
                        return [path, seen, closedSet]

                    return [path]
                if neighbor in closedSet:
                    continue
                gcurr = gbest[v]+self.calcd(v,neighbor)
                f = gcurr+self.calcd(neighbor,cityb)
                if not neighbor in seen:
                    openSet.put((f,neighbor))
                    seen[neighbor] = v
                    gbest[neighbor] = gcurr
                    path[neighbor] = v
                    self.graph_edge(neighbor, v, "green", 1)
                    if io % 600 == 0:
                        self.w.update()
                elif gcurr < gbest[neighbor]:
                    openSet.put((f,neighbor))
                    seen[neighbor] = v
                    gbest[neighbor] = gcurr
                    path[neighbor] = v
                    self.graph_edge(neighbor, v, "green", 1)
                    if io % 600 == 0:
                        self.w.update()
                closedSet.add(v)
                self.graph_point(v,"yellow")
            io += 1

    #returns the optimal dist. between two nodes
    def distance_between_edges(self, citya, cityb, graph = False):
        self.graph_clear()
        if graph:
            self.graph_all_edges()
        dist = 0
        path = self.path_between_edges(citya,cityb,graph)
        curr = cityb
        toret = ""
        while path[0][curr]:
            if graph:
                self.graph_edge(curr, path[0][curr], "red", 3)
                self.w.update()
            moved = self.calcd(curr,path[0][curr])
            dist += moved
            toret = curr + " " + str(moved) + " mi\n" + toret
            curr = path[0][curr]
        toret = citya+"\n"+toret+"Total Distance: "+str(dist)+" mi"
        return toret
Samer Kadih
import Queue
import sys
import time
from Tkinter import *

from Finished.rrUtil import *

start = time.clock()

inputs = sys.argv[1:]

util = rrUtil("rrNodes.txt", "rrEdges.txt","rrNodeCity.txt",15,15,10)

if len(inputs) == 2:
    print(util.distance_between_edges(util.names[inputs[0]], util.names[inputs[1]], True))
elif len(inputs) == 3:
    if(inputs[0]+" "+inputs[1] in util.names):
        print(util.distance_between_edges(util.names[inputs[0] + " " + inputs[1]],util.names[inputs[2]], True))
    elif(inputs[1]+" "+inputs[2] in util.names):
        print(util.distance_between_edges(util.names[inputs[0]], util.names[inputs[1]+" "+ inputs[2]], True))
    else:
        print("Invalid Input")
elif len(inputs) == 4:
    print(util.distance_between_edges(util.names[inputs[0]+" "+inputs[1]], util.names[inputs[2]+" "+inputs[3]], True))
else:
    print("Invalid Inputs")

end = time.clock()
print("Time: "+str(end-start))

util.mainloop()
'''