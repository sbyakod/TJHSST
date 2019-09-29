#Name: Sharath Byakod
#Date: 2/27/18
#Period: 4

import sys

problem = sys.argv[1]

if problem == "41":
   print("/\\b[pck]\w*/")
elif problem == "42":
   print("/^\/w(\w\w)*$/")
elif problem == "43":
   print("/^0([01][01])*$|^1[01]([01][01])*$/")
elif problem == "44":
   print("/^[01]*(?!110)[01]*$/")
elif problem == "45":
   print("/^[ox]{64}$/i")
elif problem == "46":
   print("/[ox]*[.][ox]*/is")
elif problem == "47":
   print("/x+o*[.].*|.*[.]o*x+/is")
elif problem == "48":
   print("/^[bc]*a[bc]*$s/")
elif problem == "49":
   print("/^[bc]*(a[bc]*a[bc]*)*$/")
elif problem == "50":
   print("/^[02]*(1[02]*1[02]*)*$/")