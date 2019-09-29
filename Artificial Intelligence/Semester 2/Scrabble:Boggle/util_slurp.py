#Name: Sharath Byakod
#Date: 4/10/18
#Period: 4

import sys
import urllib.request

input = sys.argv[1]

try:
   url = urllib.request.urlopen(input).read()
   print(url)
except:
   file = open(input, 'r')
   text = file.read().strip()
   file.close()