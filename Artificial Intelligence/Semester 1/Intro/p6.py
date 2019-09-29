#Name: Sharath Byakod
#Period: 4
#Date: 8/31/17

import sys
import math

list = sys.argv

p = int(list[1]) + int(list[2]) + int(list[3])
p = p / 2

a = p * (p - int(list[1])) * (p - int(list[2])) * (p - int(list[3]))
a = math.sqrt(a)
a = int(a)

print(a)