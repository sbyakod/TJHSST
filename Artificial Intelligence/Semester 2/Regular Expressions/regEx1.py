#Name: Sharath Byakod
#Date: 2/26/18
#Period: 4

import sys

problem = sys.argv[1]

if problem == "31":
   print("/^0$|^100$|^101$/")
elif problem == "32":
   print("/^[01]*$/")
elif problem == "33":
   print("/0$/")
elif problem == "34":
   print("/\w*[aeiou]\w*[aeiou]\w*/i")
elif problem == "35":
   print("/^[01]*0$/")
elif problem == "36":
   print("/^\w*110\w*$/i")
elif problem == "37":
   print("/.{2,4}/")
elif problem == "38":
   print("/^d{3}[- ]*d{2}[- ]*d{4}$/")
elif problem == "39":
   print("/^\w*d\w*$/im")
elif problem == "40":
   print("/^0[10]*0$|^1[01]*1$/")