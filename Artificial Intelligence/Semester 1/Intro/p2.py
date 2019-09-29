#Name: Sharath Byakod
#Period: 4
#Date: 8/29/17

import sys

arg = sys.argv[1]
temp = ""

for i in range(0, len(arg), 2):
   temp += arg[i]

print(temp)

#"abcdefg"[::2]