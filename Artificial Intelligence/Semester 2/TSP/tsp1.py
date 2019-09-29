#Name: Sharath Byakod
#Date: 4/30/18
#Period: 4

import sys
import time
import math
from math import *
import tkinter
from tkinter import *

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
      
top.bind_all('<Key>', lambda e: top.destroy())
top.mainloop()