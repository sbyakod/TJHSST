#Name: Sharath Byakod
#Period: 4
#Date: 8/29/17

import sys

list = sys.argv
#ar = list#.split()
sum = 0

for i in range(len(list)):
   sum += int(list[i])
   
print(sum)