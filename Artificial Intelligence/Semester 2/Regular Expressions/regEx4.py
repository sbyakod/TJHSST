#Name: Sharath Byakod
#Date: 3/5/18
#Period: 4

#42, 44-51, 56, 57, 58, 59

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
   print(r'/^1[01]*0$|^0$/')
elif problem == '36':
   print(r'/^[01]*110[01]*$/')
elif problem == '37':
   print(r'/^.{2,4}$/is')
elif problem == '38':
   print(r'/^\d{3}[ ]*-?[ ]*\d{2}[ ]*-?[ ]*\d{4}$/')
elif problem == '39':
   print(r'/^.*?d\w*/im')
elif problem == '40':
   print(r'/^0[10]*0$|^1[01]*1$|^1$|^0$/')
elif problem == '41':
   print(r'/\b[cpk]\w*\b/i')
elif problem == '42':
   print(r'/^.(.{2})*$/s')
elif problem == '43':
   print(r'/^(0([10][10])*|1([10][10])*[01])$/')
elif problem == '44':
   print(r'/^((1((1)*$|0))|0)*$/')
elif problem == '45':
   print(r'/^[xo.]{64}$/i')
elif problem == '46':
   print(r'/^[xo]*[.][xo]*$/i')
elif problem == '47':
   print(r'/^((x+o*\.|\.)[xo.]*|[xo.]*(\.o*x+|\.))$/i')
elif problem == '48':
   print(r'/^[cb]*a[cb]*$|^[cba]$/')
elif problem == '49':
   print(r'/^(a[cb]*a|[cb]+)+$/')
elif problem == '50':
   print(r'/^(2[20]*|)(1[20]*1[20]*)+$|^2[20]+$/')
elif problem == '51':
   print(r'/(.)\1\1\1\1\1\1\1\1\1/s')
elif problem == '52':
   print(r'/(\w)\w*\1/i')
elif problem == '53':
   print(r'/(\w)+\1\w*/i')
elif problem == '54':
   print(r'/(\w)+\w*\1\w*/i')
elif problem == '55':
   print(r'/^(0|1)[10]*\1$|^0$|^1$/')
elif problem == '56':
   print(r'/(?=\w*cat)\b\w\w\w\w{3}\b/i')
elif problem == '57':
   print(r'/^[10][10]*(?<=\1)$/')
elif problem == '58':
   print(r'/^([10])(?=[10]*\1$)|^0$|^1$/')
elif problem == '59':
   print(r'/\b(a|e|i|o|u)\w*?(?!\1)(a|e|i|o|u)\b/i')
elif problem == '60':
   print(r'/^(?!.*011)[01]*$/')