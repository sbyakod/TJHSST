'''import sys
import time
import math
from math import *
import tkinter
from tkinter import *

def distance(begin, end):
   #
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees

   # if (and only if) the input is strings
   # use the following conversions

   y1  = begin.latitude
   x1  = begin.longitude
   y2  = end.latitude
   x2  = end.longitude
   #
   R   = 6371 #km
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
   #

class Node:
    def __init__(self, label, longitude, latitude):
        self.label = label
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.neighbors = {}

    def __str__(self):
        return str(self.label) + ': ' + str(self.latitude) + ',' + str(self.longitude)

    def add_neighbor(self, node, distance):
        self.neighbors[node.name] = distance

class Edge:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.distance = distance(self.begin, self.end)

    def __str__(self):
        return str(self.begin.label) + ' - ' + str(self.end.label) + ' : ' + '%.1f'%self.distance

class Graph:
    def __init__(self,cycle):
        self.nodes = {}
        self.edges = set()
        self.cycle = cycle

    def read_data(self, node_file):
        words = []
        with open(node_file,'r') as f:
            lines = f.read().splitlines()
        f.close()
        number_of_nodes = int(lines[0])
        counter = 0
        for line in lines[1:]:
            x, y = line.split()
            self.nodes[counter] = Node(counter,float(x)/1000, float(y)/1000)
            counter+=1
        for i in range(len(self.cycle)):
            begin = self.nodes[self.cycle[i]]
            if i+1 != len(self.cycle): end = self.nodes[self.cycle[i+1]]
            else: end = self.nodes[self.cycle[0]]
            edge = Edge(begin, end)
            self.edges.add(edge)
    def print_nodes(self):
        for key, node in self.nodes.items():
            print(node)

    def print_edges(self):
        distance = 0
        for edge in self.edges:
            print(edge, "km")
            distance += edge.distance
        print('Total distance of all edges:', '%.1f'%distance," km")

    def give_dist(self):
        distance = 0
        for edge in self.edges:
            distance += edge.distance
        print('Total distance of all edges:', '%f'%distance," km")

    def show_map(self):
        start = next(iter(self.nodes))
        max_latitude = self.nodes[start].latitude
        min_latitude = self.nodes[start].latitude
        max_longitude = self.nodes[start].longitude
        min_longitude = self.nodes[start].longitude
        for key, node in self.nodes.items():
            if node.latitude > max_latitude:
                max_latitude = node.latitude
            if node.latitude < min_latitude:
                min_latitude = node.latitude
            if node.longitude > max_longitude:
                max_longitude = node.longitude
            if node.longitude < min_longitude:
                min_longitude = node.longitude
        offset = 20
        label_size = 2.5
        dx = (size_x - 2*offset)/(max_longitude-min_longitude)
        dy = (size_y - 2*offset)/(max_latitude-min_latitude)
        enlarge = 60
        for key, node in self.nodes.items():
            node.x = offset + (node.longitude - min_longitude) * dx
            node.y = size_y - (offset + (node.latitude - min_latitude) * dy)
            coord = node.x-label_size, node.y-label_size, node.x+label_size, node.y+label_size
            node.oval = canvas.create_oval(coord)
            widget = Label(canvas, text=node.label)
            widget.pack()
            canvas.create_window(node.x, node.y, window=widget)



        for i in range(0,len(self.cycle)-1):
            beginNode = self.nodes[self.cycle[i]]
            endNode = self.nodes[self.cycle[i+1]]
            canvas.create_line(beginNode.x, beginNode.y, endNode.x, endNode.y)
            print(beginNode.label,endNode.label,'%.1f'%distance(beginNode,endNode))
        print('Hamiltonian Cycle')
        for i in range(len(self.cycle)-1):
            print(self.cycle[i],' ',end='')
        self.give_dist()
        canvas.pack()

if __name__ == '__main__':
    size_x = 1200
    size_y = 600
    top = tkinter.Tk()

    canvas = Canvas(top, height=size_y, width=size_x)
    circle = [0,1,3,2,5,4,6,7,8,15,16,17,18,11,10,26,30,35,33,32,27,37,36,23,12,14,21,34,25,24,19,22,29,31,28,20,9,13,0]
    g = Graph(circle)
    g.read_data('kad.txt')
    g.show_map()
    top.bind_all('<Key>', lambda e: top.destroy())
    top.mainloop()'''

import doctest
from itertools import permutations


def distance(point1, point2):
    """
    Returns the Euclidean distance of two points in the Cartesian Plane.

    >>> distance([3,4],[0,0])
    5.0
    >>> distance([3,6],[10,6])
    7.0
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5


def total_distance(points):
    """
    Returns the length of the path passing throught
    all the points in the given order.

    >>> total_distance([[1,2],[4,6]])
    5.0
    >>> total_distance([[3,6],[7,6],[12,6]])
    9.0
    """
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])


def travelling_salesman(points, start=None):
    """
    Finds the shortest route to visit all the cities by bruteforce.
    Time complexity is O(N!), so never use on long lists.

    >>> travelling_salesman([[0,0],[10,0],[6,0]])
    ([0, 0], [6, 0], [10, 0])
    >>> travelling_salesman([[0,0],[6,0],[2,3],[3,7],[0.5,9],[3,5],[9,1]])
    ([0, 0], [6, 0], [9, 1], [2, 3], [3, 5], [3, 7], [0.5, 9])
    """
    if start is None:
        start = points[0]
    return min([perm for perm in permutations(points) if perm[0] == start], key=total_distance)


def optimized_travelling_salesman(points, start=None):
    """
    As solving the problem in the brute force way is too slow,
    this function implements a simple heuristic: always
    go to the nearest city.

    Even if this algoritmh is extremely simple, it works pretty well
    giving a solution only about 25% longer than the optimal one (cit. Wikipedia),
    and runs very fast in O(N^2) time complexity.

    >>> optimized_travelling_salesman([[i,j] for i in range(5) for j in range(5)])
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [1, 3], [1, 2], [1, 1], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 4], [3, 3], [3, 2], [3, 1], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
    >>> optimized_travelling_salesman([[0,0],[10,0],[6,0]])
    [[0, 0], [6, 0], [10, 0]]
    """
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path


def main():
    doctest.testmod()
    points = [[0, 0], [1, 5.7], [2, 3], [3, 7],
              [0.5, 9], [3, 5], [9, 1], [10, 5]]
    print("""The minimum distance to visit all the following points: {}
starting at {} is {}.

The optimized algoritmh yields a path long {}.""".format(
        tuple(points),
        points[0],
        total_distance(travelling_salesman(points)),
        total_distance(optimized_travelling_salesman(points))))


if __name__ == "__main__":
    main()
    
    0 1 3 2 4 6 5 14 12 7 8 10 11 15 16 17 18 27 26 30 35 33 32 37 36 34 31 29 23 21 19 22 24 25 20 13 9 
    
    28!!!!!
    
    797.619071998 km