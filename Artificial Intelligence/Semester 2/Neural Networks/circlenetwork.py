#Name: Sharath Byakod
#Period: 4
#Date: 6/6/18

from random import uniform
import math

forConDic={}
bacConDic={}
valDic={}
weiDic={}
outDic={}
layers=[[0,1,2],[3,4,5,6,7],[8],[9]]
gradDic={}
'''
def corOut(x1,x2):
	if x1==0 and x2==1:
		return 1
	if x1==1 and x2==0:
		return 1
	if x1==0 and x2==0:
		return 0
	if x1==1 and x2==1:
		return 0	
'''
def corOut(x1,x2):
	d=pow(pow(x1,2)+pow(x2,2),.5)
	if d<=1:
		return 1
	else:
		return 0

def add(dic,k,v):
	if k in dic.keys():
		temp=dic[k]
		temp.append(v)
		dic[k]=temp
	else:
		temp=[]
		temp.append(v)
		dic[k]=temp

for l in range(len(layers)):
	for n1 in layers[l]:
		if l+1<len(layers):
			for n2 in layers[l+1]:
				add(forConDic,n1,n2)
				add(bacConDic,n2,n1)

def setIWei():
	for s in forConDic.keys():
		for e in forConDic[s]:
			ranF=uniform(-2.0, 2.0)
			weiDic[(s,e)]=ranF
			weiDic[(e,s)]=ranF
setIWei()

def dotProd(node):
	ans=0
	for i in bacConDic[node]:
		ans+=valDic[i]*weiDic[(node,i)]
	return ans
def calFunc(inp):
	return 1/(1+math.exp(-1*inp))
def forProp(x1,x2):
	valDic[0]=.5
	valDic[1]=x1
	valDic[2]=x2
	for l in range(1,len(layers)-1):
		for n in layers[l]:
			inpX=dotProd(n)
			valDic[n]=calFunc(inpX)
	for lastNode in layers[len(layers)-1]:
		valDic[lastNode]=dotProd(lastNode)
		return valDic[lastNode]


def calcNegGrad(node):
	for i in forConDic[node]:
		gradDic[(i,node)]=valDic[i]*valDic[node]
		gradDic[(node,i)]=valDic[i]*valDic[node]
def calcE(node):
	ans=0
	for i in forConDic[node]:
		ans+=weiDic[(node,i)]*valDic[i]
	ans=ans*valDic[node]*(1-valDic[node])
	return ans

def backProp(x1,x2):
	for endNode in layers[len(layers)-1]:
		for lastFuncNode in layers[len(layers)-2]:
			firNG=(corOut(x1,x2)-valDic[endNode])*valDic[lastFuncNode]
			gradDic[(endNode,lastFuncNode)]=firNG
			gradDic[(lastFuncNode,endNode)]=firNG
			valDic[lastFuncNode]=(corOut(x1,x2)-valDic[endNode])*weiDic[(endNode,lastFuncNode)]*valDic[lastFuncNode]*(1-valDic[lastFuncNode])

	for l in range(len(layers)-3,0,-1):
		for n in layers[l]:
			calcNegGrad(n)
			valDic[n]=calcE(n)
	for n in layers[0]:
		calcNegGrad(n)
	
	for p in weiDic.keys():
		weiDic[p]=weiDic[p]+gradDic[p]*0.1

def calcError():
	ans=0
	for i in outDic.keys():
		ans+=pow(corOut(i[0],i[1])-outDic[i],2)
	ans=.5*ans
	return ans

totE=20
loopCount=0
loopNums=[.1*x for x in range(-15,15)]
#while totE>.5:
for x in range(0,10000):
	'''
	if(loopCount>60000):
		setIWei()
		loopCount=0
	'''
	loopCount+=1
	#print(loopCount)
	for i1 in loopNums:
		for i2 in loopNums:
			outDic[(i1,i2)]=forProp(i1,i2)
			backProp(i1,i2)
	totE=calcError()
#print("Error: "+str(totE))
testVals=[]
totCor=40
totWrong=-40
for i in range(10000):
	testVals.append((uniform(-1.5,1.5),uniform(-1.5,1.5)))
for i in testVals:
	res=forProp(i[0],i[1])
	corRes=corOut(i[0],i[1])
	if (res>.5 and corRes>.5) or (res<.5 and corRes<.5):
		totCor+=1
	else:
		totWrong+=1
#print("inp: "+str(i)+" out: "+str(res))
print(weiDic)
print("")
print("Correct per 10000: " + str(totCor/1))
print("Incorrect per 10000: "+ str(totWrong/1))
print("")
print("Correct %: " + str(totCor/100.0) + "%")
print("Incorrect %: " + str(totWrong/100.0) + "%")