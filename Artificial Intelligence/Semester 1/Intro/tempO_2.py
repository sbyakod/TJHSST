import sys
## 27, 28, 35, 36  O, X, X, O
## Option input of gameboard/who's move

# game = "...........................OX......XO..........................."
#
# whoT = "X"

whoT = None
game = None
theMove = None

def showBoard(game): #Prints the board
    print("\n".join([game[i:i+8] for i in range(0,64,8)]))

def whoTurn(game): #Figures out who's turn it is
    count = 0
    for each in game:
        if each == ".":
            count += 1
    if count%2 == 0:
        return "X"
    else:
        return "O"

def whoOpp(whoT): #Figures out who's the opponent
    if whoT == "X":
        return "O"
    else:
        return "X"

def getArgs(whoT, game, theMove): #Gets the base arguments
    if len(sys.argv) > 1:
        if len(sys.argv) == 4:
            game = sys.argv[1].upper()
            whoT = sys.argv[2].upper()
            theMove = int(sys.argv[3])
        elif len(sys.argv) == 2:
            if len(sys.argv[1]) > 3:
                game = sys.argv[1].upper()
                whoT = "X"
                theMove = -1
            elif len(sys.argv[1]) == 1 and (sys.argv[1] == "X" or "O"):
                whoT = sys.argv[1].upper()
                game = "...........................OX......XO..........................."
                theMove = -1
            else:
                theMove = int(sys.argv[1])
                whoT = "X"
                game = "...........................OX......XO..........................."
        elif len(sys.argv) == 3:
            if len(sys.argv[1]) > 3:
                game = sys.argv[1].upper()
                if len(sys.argv[2]) == 1 and (sys.argv[2] == "X" or "O"):
                    whoT = sys.argv[2].upper()
                    theMove = -1
                else:
                    theMove = int(sys.argv[2])
                    whoT = "X"
            elif len(sys.argv[1]) == 1 and (sys.argv[1] == "X" or "O"):
                whoT = sys.argv[1].upper()
                if len(sys.argv[2]) > 3:
                    game = sys.argv[2].upper()
                    theMove = -1
                else:
                    theMove = int(sys.argv[2])
                    game = "...........................OX......XO..........................."
            else:
                theMove = int(sys.argv[1])
                if len(sys.argv[2]) > 3:
                    game = sys.argv[2].upper()
                    whoT = "X"
                else:
                    whoT = sys.argv[2].upper()
                    game = "...........................OX......XO..........................."
    else:
        whoT = "X"
        game = "...........................OX......XO..........................."
        theMove = -1

    return whoT, game, theMove


def possibleMoves(game, whoT):
    checkUp, checkDown, poss, oppo = {0,6,7,8}, {(54,9),(55,8),(56,7),(63,1)}, set(), whoOpp(whoT) ##
    for each in range(len(game)):
        if game[each] == whoT:
            for check in checkUp:
                if each > check:
                    if ((not(check == 0 or check == 8 or check == 6)) or (((check == 0 or check == 8) and each%8 != 0) or (not(check == 6 and each%8 ==7)))):
                        if game[each-(check+1)] == oppo:
                            temp = each-(check+1)
                            while temp > check+1:
                                if(not(((check == 0 or check == 8) and temp%8 == 0) or ((check == 6 and temp%8 ==7)))):
                                    if game[temp] == ".":
                                        poss.add(temp)
                                        break
                                    temp = temp - (check+1)
                                else:
                                    break
            for check in checkDown:
                if each < check[0]:
                    if ((not(check[0] == 63 or check[0] == 54 or check[0] == 56)) or (((check[0] == 63 or check[0] == 54) and each%8 != 7) or (not(check[0] == 56 and each%8 == 0)))):
                        if game[each+check[1]] == oppo:
                            temp = each+check[1]
                            while temp < check[0]:
                                if(not( ((check[0] == 63 or check[0] == 54) and temp%8 == 7) or ((check[0] == 56 and temp%8 == 0)))):
                                    if game[temp] == ".":
                                        poss.add(temp)
                                        break
                                    temp = temp + check[1]
                                else:
                                    break
    return poss

def move(game, player, position):
    if position == -1:
        print("No move given.")
    elif position not in possibleMoves(game,player):
        print("Move not possible.")
    else:
        game[position] = player
        checkUp, checkDown, oppo = {0,6,7,8}, {(54,9),(55,8),(56,7),(63,1)}, whoOpp(whoT)
        for check in checkUp:
            if position > check:
                if ((not(check == 0 or check == 8 or check == 6)) or (((check == 0 or check == 8) and position%8 != 0) or (not(check == 6 and position%8 ==7)))):
                    if game[position-(check+1)] == oppo:
                        temp = position-(check+1)
                        pos = 0
                        while temp > check+1:
                            if(not(((check == 0 or check == 8) and temp%8 == 0) or ((check == 6 and temp%8 ==7)))):
                                if game[temp] == ".":
                                    break
                                elif game[temp] == whoT:
                                    pos = temp
                                    break
                                temp = temp - (check+1)
                        while pos != position:
                            pos = pos + (check+1)
                            game[pos] = whoT

        for check in checkDown:
            if position < check[0]:
                if ((not(check[0] == 63 or check[0] == 54 or check[0] == 56)) or (((check[0] == 63 or check[0] == 54) and position%8 != 7) or (not(check[0] == 56 and position%8 == 0)))):
                    if game[position+check[1]] == oppo:
                        temp = position+check[1]
                        pos = 0
                        while temp < check[0]:
                            if(not( ((check[0] == 63 or check[0] == 54) and temp%8 == 7) or ((check[0] == 56 and temp%8 == 0)))):
                                if game[temp] == ".":
                                    break
                                elif game[temp] == whoT:
                                    pos = temp
                                    break
                                temp = temp + check[1]
                        while pos != position:
                            pos = pos - check[1]
                            game[pos] = whoT




whoT, game, theMove = getArgs(whoT, game, theMove)
# print("State of game: ")
# showBoard(game)
print("")
print(game)
print("")
game = list(game)
print("Possible Moves: ", end = "")
moves = possibleMoves(game,whoT)
print(moves)
temp = game[:]
for each in moves:
    temp[each] = "*"
print("")
print("")
showBoard("".join(temp))
move(game,whoT,theMove)
temp = game[:]
print("")
print(whoT, end="")
print(" => ", end="")
print(theMove)
print("")
print("".join(temp))
print("")

countX = 0
countO = 0
for each in temp:
    if each == "X":
        countX += 1
    elif each == "O":
        countO += 1
print("X: " , end="")
print(countX, end="")
print(" O: ", end="")
print(countO)

# for each in moves:
#     if each != 19:
#         temp[each] = "*"
# print("")
showBoard("".join(temp))