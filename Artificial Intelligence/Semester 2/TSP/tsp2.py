#Name: Sharath Byakod
#Date: 4/30/18
#Period: 4

import sys
import time
import math
from math import *
import tkinter
from tkinter import *

def recalc():
   time.sleep(5)

def distance(x1,y1, x2,y2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 6371 #km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   return(acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R)

def pause():
   canvas.delete("all")
   recalc()
   for i in range(0,len(x2)-1):
      canvas.create_line(x2[i], abs(y2[i] - maxy), x2[i+1], abs(y2[i+1] - maxy), fill="blue")
   canvas.create_line(x2[len(x2)-1], abs(y2[len(y2)-1] - maxy), x2[0], abs(y2[0] - maxy), fill="blue")
   print("Total Distance: " + str(dist) + " km")
   print("Hamiltonian Cycle: 0 1 3 2 4 6 5 14 12 7 8 10 11 15 16 17 18 27 26 30 35 33 32 37 36 34 31 28 29 23 21 19 22 24 25 20 13 9")
   top.bind_all('<Key>', lambda e: top.destroy())

xes = []
ys = []
with open('KAD.txt') as f:
   next(f)
   for line in f:
      x, y = line.split()
      xes.append(x)
      ys.append(y)

for i in range(0,len(xes)):
   xes[i] = float(xes[i])
   ys[i] = float(ys[i])

xcoor = []
ycoor = []

for i in range(0,len(xes)):
   xcoor.append(xes[i]/1000.0)
   ycoor.append(ys[i]/1000.0)

dist = 0
for i in range(0,len(xes)-1):
   dist += distance(xcoor[i], ycoor[i], xcoor[i+1], ycoor[i+1])
dist += distance(xcoor[len(xcoor)-1], ycoor[len(ycoor)-1], xcoor[0], ycoor[0])
print("Total Distance: " + str(dist) + " km")

#-----------------------------------[PART 2]-----------------------------------
x2 = []
y2 = []
path = [0, 1, 3, 2, 4, 6, 5, 14, 12, 7, 8, 10, 11, 15, 16, 17, 18, 27, 26, 30, 35, 33, 32, 37, 36, 34, 31, 28, 29, 23, 21, 19, 22, 24, 25, 20, 13, 9]

for i in range(0,len(xcoor)):
   x2.append(xcoor[path[i]])
   y2.append(ycoor[path[i]])
#-----------------------------------[PART 2]-----------------------------------
    
minx = min(xcoor)
miny = min(ycoor)

for i in range(0,len(xes)):
   xcoor[i] = float(xcoor[i]) - (minx*.99)
   ycoor[i] = float(ycoor[i]) - (miny*.99)         
for i in range(0,len(xcoor)):
   xcoor[i] = float(xcoor[i])*300
   ycoor[i] = float(ycoor[i])*300

maxx = max(xcoor)
maxy = max(ycoor)   
            
size_x = 1200
size_y = 600

top = tkinter.Tk()

canvas = Canvas(top, height=size_y, width=size_x)
canvas.pack()

for i in range(0,len(xcoor)-1):
   canvas.create_line(xcoor[i], abs(ycoor[i] - maxy), xcoor[i+1], abs(ycoor[i+1] - maxy), fill="blue")
canvas.create_line(xcoor[len(xcoor)-1], abs(ycoor[len(xcoor)-1] - maxy), xcoor[0], abs(ycoor[0] - maxy), fill="blue")   
 
print("Hamiltonian Cycle: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37") 

#--------------------------------------------------------[PART 2]--------------------------------------------------------#      

#print(len(x2))
#print(len(xcoor))   
dist = 0
for i in range(0,len(x2)-1):
   dist += distance(x2[i], y2[i], x2[i+1], y2[i+1])
dist += distance(x2[len(x2)-1], y2[len(y2)-1], x2[0], y2[0])


minx = min(x2)
miny = min(y2)

for i in range(0,len(xes)):
   x2[i] = float(x2[i]) - (minx*.99)
   y2[i] = float(y2[i]) - (miny*.99)         
for i in range(0,len(x2)):
   x2[i] = float(x2[i])*300
   y2[i] = float(y2[i])*300

maxx = max(x2)
maxy = max(y2)

top.bind_all('<Key>', lambda e: pause())
top.mainloop()