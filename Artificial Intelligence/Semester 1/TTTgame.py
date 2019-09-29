import sys, tty, termios

class Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

if len(sys.argv) > 1:
    whoAI = sys.argv[1].upper()
    if len(sys.argv) == 3:
        boardState = list(sys.argv[2])
    else:
        boardState = [".",".",".",".",".",".",".",".","."]
else:
    whoAI = "X"
    boardState = [".",".",".",".",".",".",".",".","."]

def showBoard(game):
    print("\n".join([game[i:i+3] for i in range(0,9,3)]))

def whoTurn(game):
    count1,count2 = 0,0
    for each in game:
        if each == "X":
            count1 += 1
        if each == "O":
            count2 +=1
    if count1 == count2:
        return "X"
    else:
        return "O"

def emptySpots(game):
    return {i for i in range(len(game)) if game[i] == "."}

def whoWon(game):
    l1 = [[game[i+j] for j in range(0,3)] for i in range(0,9,3)]
    l2 = [[game[(i+(3*j))] for j in range(0,3)] for i in range(0,3)]
    l3 = [[game[0],game[4],game[8]],[game[2],game[4],game[6]]]
    finalL = l1+l2+l3
    for each in finalL:
        if len(set(each)) == 1 and each[0] == "X":
            return "X"
        elif len(set(each)) == 1 and each[0] == "O":
            return "O"
        else:
            continue
    return "."

def partitionMoves(game):
    winner = whoWon(game)
    mine = whoTurn(game)
    if winner == ".":
        if "." not in game:
            return {},{},{""}
    elif winner != mine and winner != ".":
        return {},{""},{}
    else:
        return {""},{},{}
    good, bad, tie = set(),set(),set()
    moves = emptySpots(game)
    for move in moves:
        game2 = game[:]
        game2[move] = mine
        tmpGood,tmpBad,tmpTie = partitionMoves(game2)
        if tmpGood:
            bad.add(move)
        elif tmpTie:
            tie.add(move)
        else:
            good.add(move)
    return good, bad, tie

game = boardState
showBoard("".join(game))
mine = whoAI
if mine == "X":
    notMine = "O"
else:
    notMine = "X"
check = 0
while("." in game):
    if(whoWon(game) == mine):
        print("You Won")
        check = 1
        break
    elif(whoWon(game) == notMine):
        print("Computer Won")
        check = 1
        break
    else:
        if whoTurn(game) == mine:
            spots = emptySpots(game)
            spots  = sorted([str(each) for each in spots])
            print("Possible moves are: ")
            end = ""
            print(spots)
            sys.stdout.write("What is your move? ")
            end = ""
            flush=True
            inkey = Getch()
            k=inkey()
            print(k)
            if k == "Q":
                "Goodbye!"
                exit()
            while k not in spots:
                print("")
                print("Please input a number between 0-8 and make sure it is a possible move.")
                print("Possible moves are: ")
                end = ""
                print(spots)
                print("What is your move? ")
                end = ""
                flush=True
                inkey = Getch()
                k=inkey()
                print(k)
            k = int(k)
            game[k] = mine
        else:
            print("")
            good, bad, tie = partitionMoves(game)
            if len(good) > 0:
                game[good.pop()] = notMine
            elif len(tie) > 0:
                game[tie.pop()] = notMine
            elif len(bad) > 0:
                game[bad.pop()] = notMine
    showBoard("".join(game))
if check == 0:
    print("It's a tie")