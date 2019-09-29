
import time

template={0:[1,3],1:[0,4,2],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[6,4,8],8:[7,5]}
daInp="12345678_"
target="12345678_"
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
def add(tree,k,v):
	if k in tree.keys():
		temp=tree[k]
		temp.append(v)
		tree[k]=temp
	else:
		temp=[]
		temp.append(v)
		tree[k]=temp	
			
def getPath(inp):
	parseMe=[inp]
	dic={0:[inp]}
	alreadySeen={inp:0}
	curDis=0
	count=0
	lowerBound=0
	while len(parseMe)>lowerBound:
		ver=parseMe[lowerBound]
		lowerBound+=1
		temp=findDec(ver)
		curDis=alreadySeen[ver]+1
		for dec in temp:
			if dec not in alreadySeen.keys():
				add(dic,curDis,dec)
				parseMe.append(dec)
				alreadySeen[dec]=curDis
	return dic;


def getPathO(inp):
	parseMe=[inp]
	alreadySeen={inp:"end"}
	lowerBound=0
	while len(parseMe)>lowerBound:
		ver=parseMe[lowerBound]
		lowerBound+=1
		temp=findDec(ver);
		for dec in temp:
			if dec not in alreadySeen.keys():
				alreadySeen[dec]=ver
				parseMe.append(dec)
		if ver==target:
			return alreadySeen
	return {}


pathDic=getPath(daInp)
maxi=0
for x in pathDic.keys():
	if x>maxi:
		maxi=x
print("\n"+ "maxSteps: " + str(maxi))
print("\n")
for x in range (1,maxi+1):
	print(str(x) + ": "+str(len(pathDic[x])))


print("\n")
pathDicO=getPathO(pathDic[31][0])
pathArr=[target]
cur=target
while cur!=pathDic[31][0]:
	pathArr.append(pathDicO[cur])
	cur=pathDicO[cur]

path=pathArr[::-1]
numSteps=len(path)-1
display(path)
print("steps: " + str(numSteps))