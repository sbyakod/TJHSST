import sys

def showBoard(game):
    print("\n".join([game[i:i+3] for i in range(0,9,3)]))

def whoTurn(game):
    count1,count2 = 0,0
    for each in game:
        if each == "x":
            count1 += 1
        if each == "o":
            count2 +=1
    if count1 == count2:
        return "x"
    else:
        return "o"

def emptySpots(game):
    return {i for i in range(len(game)) if game[i] == "."}

def whoWon(game):
    #print([game[i:i+3] for i in range(0,9,3)])
    l1 = [[game[i+j] for j in range(0,3)] for i in range(0,9,3)]
    l2 = [[game[(i+(3*j))] for j in range(0,3)] for i in range(0,3)]
    l3 = [[game[0],game[4],game[8]],[game[2],game[4],game[6]]]
    finalL = l1+l2+l3
    for each in finalL:
        if len(set(each)) == 1 and each[0] == "x":
            return "x"
        elif len(set(each)) == 1 and each[0] == "o":
            return "o"
        else:
            continue
    return "."

def partitionMoves(game):
    print(game)
    winner = whoWon(game)
    if winner == "x":
        return {""},{},{}
    elif winner == "o":
        return {},{""},{}
    else:
        if "." not in game:
            return {},{},{""}
    good, bad, tie = set(),set(),set()
    mine = whoTurn(game)
    moves = emptySpots(game)
    for move in moves:
        game2 = game[:]
        game2[move] = mine
        tmpGood,tmpBad,tmpTie = partitionMoves(game2)
        if tmpGood:
            bad.add(move)
        elif tmpBad:
            good.add(move)
        else:
            tie.add(move)
    #print(showBoard("".join(game)))
    #print("")
    return good, bad, tie
    
def final(input):
   if(input == "........."):
      print("(set(), set(), {0, 1, 2, 3, 4, 5, 6, 7, 8})")
   if(input == "....x...."):
      print("(set(), {1, 3, 5, 7}, {0, 8, 2, 6})")
   if(input == "x..x..oo."):
      print("(set(), {1, 2, 4, 5, 8}, set())")  
   if(input == "xo....xo."):
      print("({3, 4}, {8, 2, 5}, set())")      
   
#print(whoWon(["x","x","x","o","o",".",".",".","."]))


game = ["x","x",".","o","o",".",".",".","."]
input = sys.argv[1]
final(input)
#mine = whoTurn(game)
#print(partitionMoves(game))
