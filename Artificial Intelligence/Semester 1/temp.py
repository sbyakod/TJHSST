import time
import sys

size = int(sys.argv[1])

dictionary = {
0 : [1,2,3,4,5],
1 : [0,2,5,6,10],
2 : [0,1,3,6,7],
3 : [0,2,4,7,8],
4 : [0,3,5,8,9],
5 : [0,4,1,9,10],
6 : [1,2,10,7,11],
7 : [2,3,6,8,11],
8 : [3,4,7,9,11],
9 : [4,5,8,10,11],
10 : [5,1,9,6,11],
11 : [6,7,8,9,10]
}

# if size > 4:
#     print("Input is not possible")
#     sys.exit()

def notworking(l):
    for x in range(0,len(l)):
        if(l[x] != 0):
            for this in dictionary.get(x):
                if l[this] == l[x]:
                    return True
    return False

def works(l):
    for each in l:
        if each == 0:
            return False
    return True

def bruteForce(l,index,options):
    if (not notworking(l)) and works(l):
        return l
    if notworking(l) or index >= 12:
        return False
    position = index
    for each in options:
        alist = l[:]
        alist[position] = each
        bf = bruteForce(alist,index+1,options)
        if(bf != False):
            return bf
    return False


l = [0,0,0,0,0,0,0,0,0,0,0,0]
options = []
for x in range(1,size+1):
    options.append(x)
print(bruteForce(l,0,options))