#Name: Sharath Byakod
#Date: 3/1/18
#Period: 4

#31, 32, 33, 34, 41, 42, 55

import sys

problem = sys.argv[1]

if problem == '31':
   print(r'/^0$|^100$|^101$/')
elif problem == '32':
   print(r'/^[01]*$/')
elif problem == '33':
   print(r'/0$/')
elif problem == '34':
   print(r'/\w*[aeiou]\w*[aeiou]\w*/i')
elif problem == '35':
   print(r'/^[01]*0$/')
elif problem == '36':
   print(r'/^\w*110\w*$/i')
elif problem == '37':
   print(r'/.{2,4}/')
elif problem == '38':
   print(r'/^d{3}[- ]*d{2}[- ]*d{4}$/')
elif problem == '39':
   print(r'/^\w*d\w*$/im')
elif problem == '40':
   print(r'/^0[10]*0$|^1[01]*1$/')
elif problem == '41':
   print(r'/\b[pck]\w*/i')
elif problem == '42':
   print(r'/^\w(\w\w)*$/')
elif problem == '43':
   print(r'/^0([01][01])*$|^1[01]([01][01])*$/')
elif problem == '44':
   print(r'/^[01]*(?!110)[01]*$/')
elif problem == '45':
   print(r'/^[ox]{64}$/i')
elif problem == '46':
   print(r'/[ox]*[.][ox]*/is')
elif problem == '47':
   print(r'/x+o*[.].*|.*[.]o*x+/is')
elif problem == '48':
   print(r'/^[bc]*a[bc]*$s/')
elif problem == '49':
   print(r'/^[bc]*(a[bc]*a[bc]*)*$/')
elif problem == '50':
   print(r'/^[02]*(1[02]*1[02]*)*$/')
elif problem == '51':
   print(r'/^(.)\1{10,}$/')
elif problem == '52':
   print(r'/(\w)\w*\1/i')
elif problem == '53':
   print(r'/(\w)+\1\w*/i')
elif problem == '54':
   print(r'/(\w)+\w*\1\w*/i')
elif problem == '55':
   print(r'/^(0|1)[10]*\1$|^0$|^1$/')      