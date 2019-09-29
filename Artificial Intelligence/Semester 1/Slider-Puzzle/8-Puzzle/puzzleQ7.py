import sys
import time
inp = sys.argv[1]
template={0:[1,3],1:[0,4,2],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[6,4,8],8:[7,5]}
target="12345678_"
numSteps=0;
start=time.time();
def swap(s, i, j):
   lst = list(s);
   lst[i], lst[j] = lst[j], lst[i]
   return ''.join(lst)
def display(arr):
   for i in arr:
      for x in range(0,9):
         if x%3==2:
            print(i[x]+"\n")
         else:
            print (i[x]+" ")
      print("\n")
def findDec(str):
   ans=[]
   ind=str.find('_')
   for x in template[ind]:
      temp=swap(str,ind,x)
      ans.append(temp)
   return ans	
			
def getPath():
   parseMe=[inp]
   alreadySeen={inp:"end"}
   lowerBound=0
   while len(parseMe)>lowerBound:
      ver=parseMe[lowerBound]
      lowerBound+=1
      temp=findDec(ver)
      for dec in temp:
         if dec not in alreadySeen.keys():
            alreadySeen[dec]=ver
            parseMe.append(dec)
      if ver==target:
         return alreadySeen
   return {}

pathDic=getPath()
if not pathDic:
   print ("no solution")
   print(time.time()-start)
else:
   pathArr=[target]
   cur=target
   while cur!=inp:
      pathArr.append(pathDic[cur])
      cur=pathDic[cur]

   path=pathArr[::-1]
   numSteps=len(path)-1
   display(path)
   print(numSteps)
   print(time.time()-start)