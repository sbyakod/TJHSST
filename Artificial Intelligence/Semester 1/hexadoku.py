import time

thePuz = [".",".",".",".",".",".",".","3","4",".",".",".",".",".","2",".",".",".",".",".",".",".",".","."]
#                                                                  2   1   6
dictionary = {
1 : [0,1,2,6,7,8],
2 : [2,3,4,8,9,10],
3 : [5,6,7,12,13,14],
4 : [7,8,9,14,15,16],
5 : [9,10,11,16,17,18],
6 : [13,14,15,19,20,21],
7 : [15,16,17,21,22,23]
}
dictionary2 = {
1 : [0,1,2,3,4],
2 : [5,6,7,8,9,10,11],
3 : [12,13,14,15,16,17,18],
4 : [19,20,21,22,23],
5 : [12,5,6,0,1],
6 : [19,13,14,7,8,2,3],
7 : [20,21,15,16,9,10,4],
8 : [22,23,17,18,11],
9 : [5,12,13,19,20],
10 : [0,6,7,14,15,21,22],
11 : [1,2,8,9,16,17,23],
12 : [3,4,10,11,18],
}

def pzlInvalidpt1(pzl):
    for each in dictionary:
        theSet = set()
        l = []
        for index in dictionary.get(each):
            x = pzl[index]
            #print(str(index) + "::"+ str(x))
            if(x != "."):
                theSet.add(x)
                l.append(x)
        if(len(theSet) != len(l)):
            return True
    return False

def pzlInvalidpt2(pzl):
    for each in dictionary:
        theSet = set()
        l = []
        for index in dictionary.get(each):
            x = pzl[index]
            if(x != "."):
                theSet.add(x)
                l.append(x)
        if(len(theSet) != len(l)):
            return True
    for each in dictionary2:
        theSet = set()
        l = []
        for index in dictionary2.get(each):
            x = pzl[index]
            if(x != "."):
                theSet.add(x)
                l.append(x)
        if(len(theSet) != len(l)):
            return True


    return False

def pzlSolved(pzl):
    for each in dictionary:
        aSet = set()
        for index in dictionary.get(each):
            x = pzl[index]
            if(x != "."):
                aSet.add(x)
        if(len(aSet) != 6):
            return False
    return True

def bruteForce(pzl):
    if pzlInvalidpt1(pzl):
        return ""
    if pzlSolved(pzl):
        return pzl
    position = 0
    for x in range(0,len(pzl)):
        if pzl[x] == ".":
            position = x
            break
    for y in range(1,10):
        subbf = []
        for each in pzl:
            subbf.append(each)
        subbf[x] = str(y)
        bf = bruteForce(subbf)
        if(bf != ""):
            return bf
    return ""
print(bruteForce(thePuz))
