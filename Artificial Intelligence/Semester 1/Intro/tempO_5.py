import sys
## 27, 28, 35, 36  O, X, X, O
## Option input of gameboard/who's move

# game = "...........................OX......XO..........................."
#
# whoT = "X"

##This is the option sys.argv stuff
def showBoard(game): #Prints the board
    print("\n".join([game[i:i+8] for i in range(0,64,8)]))

def whoTurn(game): #Figures out who's turn it is
    #A faster way would be to count the number of periods. (Do that in a speed up)
    count = 0
    for each in game:
        if each == ".":
            count += 1
    if count%2 == 0:
        if "x" in game:
            return "x"
        else:
            return "X"
    else:
        if "x" in game:
            return "o"
        else:
            return "O"

def whoOpp(whoT):
    if "x" not in game:
        if whoT == "X":
            return "O"
        else:
            return "X"
    else:
        if whoT == "x":
            return "o"
        else:
            return "x"

if len(sys.argv) > 1:
    game = sys.argv[1]
    if len(sys.argv) == 3:
        if "x" in game:
            whoT = sys.argv[2].lower()
        else:
            whoT = sys.argv[2].upper()
    else:
        whoT = whoTurn(game)
else:
    whoT = "X"
    game = "...........................OX......XO..........................."


def possibleMoves(game, whoT):
    checkUp, checkDown, poss, oppo = {0,6,7,8}, {(54,9),(55,8),(56,7),(63,1)}, set(), whoOpp(whoT) ##
    for each in range(len(game)):
        if game[each] == whoT:
            for check in checkUp:
                if each > check:
                    if ((not(check == 0 or check == 8 or check == 6)) or (((check == 0 or check == 8) and each%8 != 0) or (not(check == 6 and each%8 ==7)))):
                        if game[each-(check+1)] == oppo:
                            temp = each-(check+1)
                            while temp >= check+1:
                                if(not(((check == 0 or check == 8) and temp%8 == 0) or ((check == 6 and temp%8 ==7)))):
                                    if game[temp] == whoT:
                                        break
                                    if game[temp] == ".":
                                        poss.add(temp)
                                        break
                                    temp = temp - (check+1)
                                    if game[temp] == ".":
                                        poss.add(temp)
                                        break
                                else:
                                    break
            for check in checkDown:
                if each < check[0]:
                    if ((not(check[0] == 63 or check[0] == 54 or check[0] == 56)) or (((check[0] == 63 or check[0] == 54) and each%8 != 7) or (not(check[0] == 56 and each%8 == 0)))):
                        if game[each+check[1]] == oppo:
                            temp = each+check[1]
                            while temp <= check[0]:
                                if(not( ((check[0] == 63 or check[0] == 54) and temp%8 == 7) or ((check[0] == 56 and temp%8 == 0)))):
                                    if game[temp] == whoT:
                                        break
                                    if game[temp] == ".":
                                        poss.add(temp)
                                        break
                                    temp = temp + check[1]
                                    if game[temp] == ".":
                                        poss.add(temp)
                                        break
                                else:
                                    break
    return poss


# print("State of game: ")
print(game)
print("")
showBoard(game)
print("")
# if len(sys.argv) == 1:
game = list(game)
print("Possible Moves: ", end = "")
moves = possibleMoves(game, whoT)
if len(moves) == 0:
    print("No Moves")
else:
    print(moves)
print("")
for each in moves:
    game[each] = "*"
print("")
showBoard("".join(game))
print("Move: ", end="")
print(moves.pop())