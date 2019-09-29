import time
import Queue

# string = "2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3"
sTime = time.time()

dictionary3 = {
0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 45, 72, 18, 19, 20, 54, 36, 27, 63],
1: [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 64, 18, 19, 20, 46, 73, 55, 28, 37],
2: [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 29, 47, 18, 19, 20, 56, 38, 74, 65],
3: [0, 1, 2, 4, 5, 6, 7, 8, 66, 39, 12, 13, 14, 48, 75, 21, 22, 23, 57, 30],
4: [0, 1, 2, 3, 5, 6, 7, 8, 76, 12, 13, 14, 40, 67, 21, 22, 23, 49, 58, 31],
5: [0, 1, 2, 3, 4, 6, 7, 8, 41, 32, 12, 13, 14, 77, 50, 21, 22, 23, 68, 59],
6: [0, 1, 2, 3, 4, 5, 7, 8, 42, 78, 15, 16, 17, 51, 33, 24, 25, 26, 60, 69],
7: [0, 1, 2, 3, 4, 5, 6, 8, 43, 34, 15, 16, 17, 52, 24, 25, 26, 79, 70, 61],
8: [0, 1, 2, 3, 4, 5, 6, 7, 80, 71, 44, 15, 16, 17, 35, 53, 24, 25, 26, 62],
9: [0, 1, 2, 36, 72, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 54, 45, 27, 63],
10: [0, 1, 2, 37, 64, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 46, 73, 55, 28],
11: [0, 1, 2, 38, 65, 29, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 56, 47, 74],
12: [48, 66, 3, 4, 5, 39, 9, 10, 11, 13, 14, 15, 16, 17, 75, 21, 22, 23, 57, 30],
13: [3, 4, 5, 49, 40, 9, 10, 11, 12, 14, 15, 16, 17, 67, 21, 22, 23, 58, 76, 31],
14: [32, 3, 4, 5, 77, 9, 10, 11, 12, 13, 15, 16, 17, 50, 41, 21, 22, 23, 68, 59],
15: [33, 69, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 51, 78, 24, 25, 26, 60, 42],
16: [34, 43, 70, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 52, 24, 25, 26, 79, 61],
17: [80, 35, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 53, 71, 24, 25, 26, 44, 62],
18: [0, 1, 2, 36, 54, 72, 9, 10, 11, 45, 19, 20, 21, 22, 23, 24, 25, 26, 27, 63],
19: [0, 1, 2, 37, 64, 9, 10, 11, 46, 73, 18, 20, 21, 22, 23, 24, 25, 26, 28, 55],
20: [0, 1, 2, 38, 65, 9, 10, 11, 29, 47, 56, 18, 19, 21, 22, 23, 24, 25, 26, 74],
21: [66, 3, 4, 5, 39, 57, 75, 12, 13, 14, 48, 18, 19, 20, 22, 23, 24, 25, 26, 30],
22: [67, 3, 4, 5, 40, 76, 12, 13, 14, 49, 18, 19, 20, 21, 23, 24, 25, 26, 58, 31],
23: [32, 68, 3, 4, 5, 41, 12, 13, 14, 77, 50, 18, 19, 20, 21, 22, 24, 25, 26, 59],
24: [33, 69, 6, 7, 8, 42, 78, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 60, 51],
25: [34, 70, 6, 7, 8, 43, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 79, 61, 52],
26: [80, 35, 6, 7, 8, 71, 44, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 62, 53],
27: [32, 33, 34, 35, 36, 37, 38, 63, 72, 9, 0, 45, 46, 47, 18, 54, 28, 29, 30, 31],
28: [32, 33, 34, 35, 36, 37, 38, 1, 64, 73, 10, 45, 46, 47, 19, 55, 27, 29, 30, 31],
29: [32, 33, 34, 35, 36, 37, 38, 65, 74, 2, 45, 46, 47, 11, 20, 56, 27, 28, 30, 31],
30: [32, 33, 34, 35, 39, 40, 41, 75, 12, 66, 48, 49, 50, 3, 21, 57, 27, 28, 29, 31],
31: [32, 33, 34, 35, 4, 39, 40, 41, 76, 13, 48, 49, 50, 67, 22, 58, 27, 28, 29, 30],
32: [33, 34, 35, 68, 5, 39, 40, 41, 77, 14, 48, 49, 50, 59, 23, 27, 28, 29, 30, 31],
33: [32, 34, 35, 69, 6, 60, 42, 43, 44, 78, 15, 51, 52, 53, 24, 27, 28, 29, 30, 31],
34: [32, 33, 35, 70, 7, 42, 43, 44, 61, 79, 16, 51, 52, 53, 25, 27, 28, 29, 30, 31],
35: [32, 33, 34, 71, 8, 42, 43, 44, 80, 17, 51, 52, 53, 62, 26, 27, 28, 29, 30, 31],
36: [0, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 72, 18, 54, 9, 27, 28, 29, 63],
37: [64, 1, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 10, 19, 73, 55, 27, 28, 29],
38: [65, 2, 11, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 74, 56, 20, 27, 28, 29],
39: [32, 66, 3, 36, 37, 38, 40, 41, 42, 43, 44, 12, 48, 49, 50, 21, 57, 75, 30, 31],
40: [32, 67, 36, 37, 38, 39, 41, 42, 43, 44, 13, 48, 49, 50, 76, 4, 22, 58, 30, 31],
41: [32, 36, 37, 38, 39, 40, 42, 43, 44, 77, 14, 48, 49, 50, 23, 68, 59, 5, 30, 31],
42: [33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 78, 15, 51, 52, 53, 24, 6, 60, 69],
43: [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 79, 16, 51, 52, 53, 7, 25, 70, 61],
44: [17, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 80, 8, 51, 52, 53, 71, 26, 62],
45: [0, 18, 36, 37, 38, 72, 9, 46, 47, 48, 49, 50, 51, 52, 53, 54, 27, 28, 29, 63],
46: [64, 1, 36, 37, 38, 73, 10, 45, 47, 48, 49, 50, 51, 52, 53, 55, 27, 28, 29, 19],
47: [65, 2, 36, 37, 38, 74, 11, 45, 46, 48, 49, 50, 51, 52, 53, 56, 20, 27, 28, 29],
48: [32, 66, 3, 39, 40, 41, 75, 12, 45, 46, 47, 49, 50, 51, 52, 53, 57, 21, 30, 31],
49: [32, 67, 4, 39, 40, 41, 76, 45, 46, 47, 48, 50, 51, 52, 53, 22, 58, 13, 30, 31],
50: [32, 14, 68, 5, 39, 40, 41, 77, 45, 46, 47, 48, 49, 51, 52, 53, 23, 59, 30, 31],
51: [33, 34, 35, 69, 6, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 24, 15, 60, 78],
52: [33, 34, 35, 70, 7, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 25, 79, 61, 16],
53: [33, 34, 35, 17, 71, 8, 80, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 26, 62],
54: [64, 65, 27, 36, 0, 72, 73, 74, 45, 18, 9, 55, 56, 57, 58, 59, 60, 61, 62, 63],
55: [64, 65, 28, 37, 1, 72, 73, 74, 46, 10, 19, 54, 56, 57, 58, 59, 60, 61, 62, 63],
56: [64, 65, 2, 38, 72, 73, 74, 11, 29, 47, 20, 54, 55, 57, 58, 59, 60, 61, 62, 63],
57: [66, 67, 68, 39, 12, 30, 75, 76, 77, 48, 3, 21, 54, 55, 56, 58, 59, 60, 61, 62],
58: [66, 67, 68, 22, 40, 75, 76, 77, 13, 49, 4, 54, 55, 56, 57, 59, 60, 61, 62, 31],
59: [32, 66, 67, 68, 5, 41, 75, 76, 77, 14, 50, 23, 54, 55, 56, 57, 58, 60, 61, 62],
60: [33, 6, 69, 70, 71, 15, 42, 78, 79, 80, 24, 51, 54, 55, 56, 57, 58, 59, 61, 62],
61: [16, 34, 43, 69, 70, 71, 7, 78, 79, 80, 25, 52, 54, 55, 56, 57, 58, 59, 60, 62],
62: [35, 69, 70, 71, 8, 44, 78, 79, 80, 17, 26, 53, 54, 55, 56, 57, 58, 59, 60, 61],
63: [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 45, 18, 9, 54, 55, 56, 36, 27, 0],
64: [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 46, 10, 19, 1, 54, 55, 56, 28, 37, 63],
65: [64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 11, 2, 47, 20, 54, 55, 56, 38, 29, 63],
66: [64, 65, 67, 68, 69, 70, 71, 12, 30, 75, 76, 77, 48, 3, 21, 57, 58, 59, 39, 63],
67: [64, 65, 66, 68, 69, 70, 71, 40, 31, 75, 76, 77, 13, 49, 22, 57, 58, 59, 4, 63],
68: [64, 65, 66, 67, 69, 70, 71, 41, 75, 76, 77, 14, 50, 32, 23, 57, 58, 59, 5, 63],
69: [64, 65, 66, 67, 68, 70, 71, 42, 78, 79, 80, 6, 51, 24, 33, 15, 60, 61, 62, 63],
70: [64, 65, 66, 67, 68, 69, 71, 7, 34, 78, 79, 80, 43, 52, 16, 25, 60, 61, 62, 63],
71: [64, 65, 66, 67, 68, 69, 70, 8, 44, 78, 79, 80, 17, 35, 53, 26, 60, 61, 62, 63],
72: [64, 65, 45, 36, 0, 73, 74, 75, 76, 77, 78, 79, 80, 18, 9, 54, 55, 56, 27, 63],
73: [64, 65, 37, 1, 72, 74, 75, 76, 77, 78, 79, 80, 19, 46, 54, 55, 56, 28, 10, 63],
74: [64, 65, 2, 11, 38, 72, 73, 75, 76, 77, 78, 79, 80, 20, 54, 55, 56, 47, 29, 63],
75: [48, 66, 67, 68, 39, 72, 73, 74, 76, 77, 78, 79, 80, 3, 12, 57, 58, 59, 30, 21],
76: [66, 67, 68, 49, 72, 73, 74, 75, 77, 78, 79, 80, 40, 22, 57, 58, 59, 13, 4, 31],
77: [32, 66, 67, 68, 5, 72, 73, 74, 75, 76, 78, 79, 80, 50, 14, 41, 23, 57, 58, 59],
78: [33, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 80, 42, 24, 6, 15, 60, 61, 62, 51],
79: [16, 34, 43, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 52, 7, 25, 60, 61, 62],
80: [35, 17, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 8, 44, 53, 26, 60, 61, 62]}

def pzlInvalidpt1(pzl,index):
    return pzl[index] in (pzl[nbr] for nbr in dictionary3[index] if pzl[nbr] != ".")

string = "9........5..6...27.83..16.5..8.4..6...5.2.7...7..8.4..7.95..18.82...4..9........6"

def getLeastPos(pzl,pdList):
    least = 100
    smallInd = 0
    final = set()
    # for index in range(0,81):
    for index in pdList:
        if(pzl[index] == "."):
            # temp = pos[:]
            pos = {"1","2","3","4","5","6","7","8","9"}
            for nbr in dictionary3[index]:
                if pzl[nbr] in pos:
                    pos.remove(pzl[nbr])
            if len(pos) < least:
                least = len(pos)
                smallInd = index
                final = pos.copy()
    return smallInd, final

def bruteForce(pzl,index,pdList,count):
    # if count == 0:
        # if pzlInvalidpt1(pzl,index):
        #     return ""
    # count = 1
    #if pzlInvalidpt2(pzl,index):
    if "." not in pzl:
        return pzl
    # temp = pdList[:]i
    # position = temp.pop(0)
    position,poss = getLeastPos(pzl,pdList)
    index = position
    for y in poss:
        subbf = pzl[:]
        subbf[position] = str(y)
        bf = bruteForce(subbf,index,pdList,count)
        if(bf != ""):
            return bf
    return ""

theFile = open("puzzles.txt", "r")
lines = theFile.readlines()
for each in lines:
    candidates = {}
    each = each[:-1:]
    each = list(each)
    pdList = []
    for z in range(0,81):
        if(each[z] == "."):
            pdList.append(z)
    x = bruteForce(each,pdList[0],pdList,0)
    final = ""
    for each in x:
        final += str(each)
    print(final)
print(str(time.time()-sTime))

# 134587296278169354695234817359816472821473569746925183917348625462751938583692741

# pdList = []
# each = list(string)
# for z in range(0,81):
#     if(each[z] == "."):
#         pdList.append(z)
# x = bruteForce(each,pdList[0],pdList,0)
# final = ""
# for each in x:
#     final += str(each)
# print(final)
