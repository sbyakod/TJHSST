from tkinter import *
from math import pi , acos , sin , cos
import Queue
import sys
import time

class rrUtil:
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

   def graph_all_edges(self):
      self.w.delete("all")
      for coord in self.edges:
         for edge in self.edges[coord]:
            self.w.create_line((self.nodes[coord][0] - self.minx) * self.xscale + self.xroom // 2,
                         (self.maxy - self.nodes[coord][1]) * self.yscale + self.yroom // 2,
                         (self.nodes[edge][0] - self.minx) * self.xscale + self.xroom // 2,
                         (self.maxy - self.nodes[edge][1]) * self.yscale + self.yroom // 2)

   def graph_edge(self, citya, cityb, color="black", width = 1):
      self.w.create_line((self.nodes[citya][0] - self.minx) * self.xscale + self.xroom // 2,
                        (self.maxy - self.nodes[citya][1]) * self.yscale + self.yroom // 2,
                        (self.nodes[cityb][0] - self.minx) * self.xscale + self.xroom // 2,
                        (self.maxy - self.nodes[cityb][1]) * self.yscale + self.yroom // 2,
                        fill = color,
                        width = width)

   def graph_point(self,citya,color="black"):
      r=1
      self.w.create_oval((self.nodes[citya][0] - self.minx) * self.xscale + self.xroom // 2-r,(self.maxy - self.nodes[citya][1]) * self.yscale + self.yroom // 2+r,(self.nodes[citya][0] - self.minx) * self.xscale + self.xroom // 2+r,(self.maxy - self.nodes[citya][1]) * self.yscale + self.yroom // 2-r, fill = color)

   def mainloop(self):
      mainloop()

   def graph_text(self, citya, text):
      self.w.create_text((self.nodes[citya][0] - self.minx) * self.xscale + self.xroom // 2,
                        (self.maxy - self.nodes[citya][1]) * self.yscale + self.yroom // 2,
                        anchor = SE,
                        font = ("Purisa",20),
                        text = text,
                        fill = "purple")

   def graph_clear(self):
      self.w.delete("all")

   def calc(self,citya,cityb):
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

   def dist_all_edges(self):
      dist = 0
      closed = set()
      for node in self.nodes:
         for edge in self.edges[node]:
            if not edge in closed:
               dist += self.calc(node,edge)
         closed.add(node)
      return dist

   def path(self, citya, cityb, graph = False):
   
      oSet = Queue.PriorityQueue()
      cSet = set()
      seen = {}
      path = {citya:None}
      gbest = {citya:0}
   
      oSet.put((0,citya))
      io = 0
      while oSet:
         v = oSet.get()[1]
         for neighbor in self.edges[v]:
            if neighbor == cityb:
               path[neighbor] = v
               seen[neighbor] = v
               cSet.add(v)
            
               if graph:
                  return [path, seen, cSet]
            
               return [path]
            if neighbor in cSet:
               continue
            gcurr = gbest[v]+self.calc(v,neighbor)
            f = gcurr+self.calc(neighbor,cityb)
            if not neighbor in seen:
               oSet.put((f,neighbor))
               seen[neighbor] = v
               gbest[neighbor] = gcurr
               path[neighbor] = v
               self.graph_edge(neighbor, v, "green", 1)
               if io % 600 == 0:
                  self.w.update()
            elif gcurr < gbest[neighbor]:
               oSet.put((f,neighbor))
               seen[neighbor] = v
               gbest[neighbor] = gcurr
               path[neighbor] = v
               self.graph_edge(neighbor, v, "green", 1)
               if io % 600 == 0:
                  self.w.update()
            cSet.add(v)
            self.graph_point(v,"blue")
         io += 1

   def distance(self, citya, cityb, graph = False):
      self.graph_clear()
      if graph:
         self.graph_all_edges()
      dist = 0
      path = self.path(citya,cityb,graph)
      curr = cityb
      toret = ""
      while path[0][curr]:
         if graph:
            self.graph_edge(curr, path[0][curr], "red", 3)
            self.w.update()
         moved = self.calc(curr,path[0][curr])
         dist += moved
         curr = path[0][curr]
      toret = toret+"Total Distance: "+str(dist)+" mi"
      return toret

start = time.clock()
inputs = sys.argv[1:]
util = rrUtil("rrNodes.txt", "rrEdges.txt","rrNodeCity.txt",15,15,10)

if len(inputs) == 2:
   print(util.distance(util.names[inputs[0]], util.names[inputs[1]], True))
else:
   print("Invalid Inputs")

end = time.clock()
print("Time: "+str(end-start))

util.mainloop()