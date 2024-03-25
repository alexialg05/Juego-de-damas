ef printBoard(board):
    x = len(board)
    y = len(board[0])
    print(" "*6, end = "")
    for i in range(0, x):
        print(i+1, end = "    ")
    print()
    print("   "+"-"*26)
    for i in range(0, x):
        print(" "+str(i+1)+" |", end = "")
        for j in range(0, y):
            if board[i][j] == "R":
                print(" \U0001F534 ", end = "")
            elif board[i][j] == "RD":
                print(" \U0001F536 ", end = "")
            elif board[i][j] == "B":
                print(" \U0001F535 ", end = "")
            elif board[i][j] == "BD":
                print(" \U0001F537 ", end = "")
            else:
                print("    ", end="")
            print("|", end="")
        print()
        print("   " + "-" * 26)

def canEatAgainBlue(row, column, board):
    itCan = False
    # Check if is possible give 2 steps forward
    if row > 2:
        # Check left
        if column > 2:
            if (board[row - 2][column - 2] == "R" or board[row - 2][column - 2] == "RD") and (
                    board[row - 3][column - 3] == ""):
                itCan = True
        # Check right
        if column < 4:
            if (board[row - 2][column] == "R" or board[row - 2][column] == "RD") and (
                    board[row - 3][column + 1] == ""):
                itCan = True
    return itCan

def canEatAgainBlueD(row, column, board):
    itCan = False
    # Check if is possible give 2 steps forward
    if row > 2:
        # Check left
        if column > 2:
            if (board[row - 2][column - 2] == "R" or board[row - 2][column - 2] == "RD") and (
                    board[row - 3][column - 3] == ""):
                itCan = True
        # Check right
        if column < 4:
            if (board[row - 2][column] == "R" or board[row - 2][column] == "RD") and (
                    board[row - 3][column + 1] == ""):
                itCan = True
    if row < 4:
        # Check left
        if column > 2:
            if (board[row][column - 2] == "R" or board[row][column - 2] == "RD") and (
                    board[row + 1][column - 3] == ""):
                itCan = True
        # Check right
        if column < 4:
            if (board[row][column] == "R" or board[row][column] == "RD") and (
                    board[row + 1][column + 1] == ""):
                itCan = True
    return itCan
def canEatAgainRed(row, column, board):
    itCan = False
    # Check if is possible give 2 steps forward
    if row < 4:
        # Check left
        if column > 2:
            if (board[row][column - 2] == "B" or board[row][column - 2] == "BD") and (
                    board[row +1][column - 3] == ""):
                itCan = True
        # Check right
        if column < 4:
            if (board[row][column] == "B" or board[row][column] == "BD") and (
                    board[row + 1][column + 1] == ""):
                itCan = True
    return itCan

def canEatAgainRedD(row, column, board):
    itCan = False
    # Check if is possible give 2 steps forward
    if row < 4:
        # Check left
        if column > 2:
            if (board[row][column - 2] == "B" or board[row][column - 2] == "BD") and (
                    board[row +1][column - 3] == ""):
                itCan = True
        # Check right
        if column < 4:
            if (board[row][column] == "B" or board[row][column] == "BD") and (
                    board[row + 1][column + 1] == ""):
                itCan = True
    if row > 2:
        # Check left
        if column > 2:
            if (board[row - 2][column - 2] == "B" or board[row - 2][column - 2] == "BD") and (
                    board[row - 3][column - 3] == ""):
                itCan = True
        # Check right
        if column < 4:
            if (board[row - 2][column] == "B" or board[row - 2][column] == "BD") and (
                    board[row - 3][column + 1] == ""):
                itCan = True
    return itCan


def redMove(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, redRowLocked, redColLocked):
    # Normal move case
    turn = "Red"
    if redRowLocked == -1 and redColLocked == -1 or redRowLocked == rowOrigin and redColLocked == columnOrigin:
        if rowDestiny == rowOrigin + 1 and ((columnDestiny >= 0 and columnDestiny == columnOrigin - 1) or (
                columnDestiny <= len(board) and columnDestiny == columnOrigin + 1)) and board[rowDestiny - 1][
            columnDestiny - 1] == "":
            board[rowOrigin - 1][columnOrigin - 1] = ""
            board[rowDestiny - 1][columnDestiny - 1] = "RD" if rowDestiny == len(board) else "R"
            turn = "Blue"
            print("Valid movement")

        # Eat move case
        elif rowDestiny == rowOrigin + 2 and ((columnDestiny >= 0 and columnDestiny == columnOrigin - 2) or (
                columnDestiny <= len(board) and columnDestiny == columnOrigin + 2)) and board[rowDestiny - 1][
            columnDestiny - 1] == "" and (
                board[rowOrigin][columnOrigin - 1 + (-1 if columnDestiny < columnOrigin else 1)] == "B" or
                board[rowOrigin][columnOrigin - 1 + (-1 if columnDestiny < columnOrigin else 1)] == "BD"):
            board[rowOrigin - 1][columnOrigin - 1] = ""
            board[rowOrigin][columnOrigin - 1 + (-1 if columnDestiny < columnOrigin else 1)] = ""
            board[rowDestiny - 1][columnDestiny - 1] = "RD" if rowDestiny == len(board) else "R"
            print("Valid movement")
            turn = "Red" if canEatAgainRed(rowDestiny, columnDestiny, board) else "Blue"

        else:
            print("Invalid movement")
        if turn == "Red":
            return turn, rowDestiny, columnDestiny
        else:
            return turn, -1, -1
    else:
        print("Invalid movement, move the one that ate")
        return turn, redRowLocked, redColLocked
def redDMove(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, redRowLocked, redColLocked):
    turn = "Red"
    if redRowLocked == -1 and redColLocked == -1 or redRowLocked == rowOrigin and redColLocked == columnOrigin:
        if (1 <= rowDestiny <= len(board) and rowDestiny != rowOrigin and 1 <= columnDestiny <= len(
                board) and columnDestiny != columnOrigin
                and abs(rowDestiny - rowOrigin) == 1 and abs(columnDestiny - columnOrigin) == 1 and
                board[rowDestiny - 1][columnDestiny - 1] == ""):
            board[rowOrigin - 1][columnOrigin - 1] = ""
            board[rowDestiny - 1][columnDestiny - 1] = "RD"
            print("Valid movement")
            turn = "Blue"
        elif (1 <= rowDestiny <= len(board) and rowDestiny != rowOrigin and 1 <= columnDestiny <= len(board) and columnDestiny != columnOrigin
                    and abs(rowDestiny-rowOrigin) == 2 and abs(columnDestiny-columnOrigin) == 2 and board[rowDestiny-1][columnDestiny-1] == ""
                    and (board[rowOrigin if rowDestiny > rowOrigin else rowOrigin-2][columnOrigin if columnDestiny > columnOrigin else columnOrigin-2] == "B"
                    or board[rowOrigin if rowDestiny > rowOrigin else rowOrigin-2][columnOrigin if columnDestiny > columnOrigin else columnOrigin-2] == "BD")):
            board[rowOrigin-1][columnOrigin-1] = ""
            board[rowOrigin if rowDestiny > rowOrigin else rowOrigin - 2][
                columnOrigin if columnDestiny > columnOrigin else columnOrigin - 2] = ""
            board[rowDestiny-1][columnDestiny-1] = "RD"
            print("Valid movement")
            turn = "Red" if canEatAgainRedD(rowDestiny, columnDestiny, board) else "Blue"
        if turn == "Red":
            return turn, rowDestiny, columnDestiny
        else:
            return turn, -1, -1
    else:
        print("Invalid movement, move the one that ate")
        return turn, redRowLocked, redColLocked

def blueMove(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, blueRowLocked, blueColLocked):
    # Normal move case
    turn = "Blue"
    if blueRowLocked == -1 and blueColLocked == -1 or blueRowLocked == rowOrigin and blueColLocked == columnOrigin:
        if rowDestiny == rowOrigin -1 and ((columnDestiny >= 0 and columnDestiny == columnOrigin - 1) or (
                columnDestiny <= len(board) and columnDestiny == columnOrigin + 1)) and board[rowDestiny - 1][
            columnDestiny - 1] == "":
            board[rowOrigin - 1][columnOrigin - 1] = ""
            board[rowDestiny - 1][columnDestiny - 1] = "BD" if rowDestiny == 1 else "B"
            print("Valid movement")
            turn = "Red"
        # Eat move case
        elif rowDestiny == rowOrigin - 2 and ((columnDestiny >= 0 and columnDestiny == columnOrigin - 2) or (
                columnDestiny <= len(board) and columnDestiny == columnOrigin + 2)) and board[rowDestiny - 1][
            columnDestiny - 1] == "" and (
                board[rowDestiny][columnOrigin - 1 + (-1 if columnDestiny < columnOrigin else 1)] == "R" or
                board[rowDestiny][columnOrigin - 1 + (-1 if columnDestiny < columnOrigin else 1)] == "RD"):
            board[rowOrigin - 1][columnOrigin - 1] = ""
            board[rowDestiny][columnOrigin - 1 + (-1 if columnDestiny < columnOrigin else 1)] = ""
            board[rowDestiny - 1][columnDestiny - 1] = "BD" if rowDestiny == 1 else "B"
            print("Valid movement")
            turn = "Blue" if canEatAgainBlue(rowDestiny, columnDestiny, board) else "Red"
        else:
            print("Invalid movement")
        if turn == "Blue":
            return turn, rowDestiny, columnDestiny
        else:
            return turn, -1, -1
    else:
        print("Invalid movement, move the one that ate")
        return turn, blueRowLocked, blueColLocked
def blueDMove(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, blueRowLocked, blueColLocked):
    turn = "Blue"
    if blueRowLocked == -1 and blueColLocked == -1 or blueRowLocked == rowOrigin and blueColLocked == columnOrigin:
        if(1 <= rowDestiny <= len(board) and rowDestiny != rowOrigin and 1 <= columnDestiny <= len(board) and columnDestiny != columnOrigin
                    and abs(rowDestiny-rowOrigin) == 1 and abs(columnDestiny-columnOrigin) == 1 and board[rowDestiny-1][columnDestiny-1] == ""):
            board[rowOrigin-1][columnOrigin-1] = ""
            board[rowDestiny-1][columnDestiny-1] = "BD"
            print("Valid movement")
            turn = "Red"
        elif (1 <= rowDestiny <= len(board) and rowDestiny != rowOrigin and 1 <= columnDestiny <= len(board) and columnDestiny != columnOrigin
                    and abs(rowDestiny-rowOrigin) == 2 and abs(columnDestiny-columnOrigin) == 2 and board[rowDestiny-1][columnDestiny-1] == ""
                    and (board[rowOrigin if rowDestiny > rowOrigin else rowOrigin-2][columnOrigin if columnDestiny > columnOrigin else columnOrigin-2] == "R"
                    or board[rowOrigin if rowDestiny > rowOrigin else rowOrigin-2][columnOrigin if columnDestiny > columnOrigin else columnOrigin-2] == "RD")):
            board[rowOrigin-1][columnOrigin-1] = ""
            board[rowOrigin if rowDestiny > rowOrigin else rowOrigin - 2][
                columnOrigin if columnDestiny > columnOrigin else columnOrigin - 2] = ""
            board[rowDestiny-1][columnDestiny-1] = "BD"
            print("Valid movement")
            turn = "Blue" if canEatAgainBlueD(rowDestiny, columnDestiny, board) else "Red"
        if turn == "Blue":
            return turn, rowDestiny, columnDestiny
        else:
            return turn, -1, -1
    else:
        print("Invalid movement, move the one that ate")
        return turn, blueRowLocked, blueColLocked

def move(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, turn, blueRowLocked, blueColLocked, redRowLocked, redColLocked):
    if board[rowOrigin-1][columnOrigin-1] == "R" and turn =="Red":
        #print("R")
        return redMove(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, redRowLocked, redColLocked)
    elif board[rowOrigin-1][columnOrigin-1] == "RD" and turn =="Red":
        #print("RD")
        return redDMove(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, redRowLocked, redColLocked)
    elif board[rowOrigin-1][columnOrigin-1] == "B" and turn =="Blue":
        #print("B")
        return blueMove(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, blueRowLocked, blueColLocked)
    elif board[rowOrigin-1][columnOrigin-1] == "BD" and turn =="Blue":
        #print("BD")
        return blueDMove(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, blueRowLocked, blueColLocked)
    else:
        print("Error: Invalid movement")
        print(turn)
        return turn, -1, -1

def winner(board):
    countBlue = 0
    countRed = 0
    for i in range(0, len(board[0])):
        for j in range(0, len(board[0])):
            if(board[i][j] == "B" or board[i][j] == "BD"):
                countBlue += 1
            if (board[i][j] == "R" or board[i][j] == "RD"):
                countRed += 1
    if countBlue == 0:
        printBoard(board)
        print("Red player wins")
        return True
    if countRed == 0:
        printBoard(board)
        print("Blue player wins")
        return True
    return False

def main(board, turn):
    currentTurn = turn
    blueRowLocked = -1
    blueColLocked = -1
    redRowLocked = -1
    redColLocked = -1
    while not winner(board):
        printBoard(board)
        if(currentTurn == "Red"):
            print("Red player turn")
            rowOrigin = int(input("Enter origin row: "))
            columnOrigin = int(input("Enter origin column: "))
            rowDestiny = int(input("Enter destiny row: "))
            columnDestiny = int(input("Enter destiny column: "))
            currentTurn, redRowLocked, redColLocked = move(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, "Red", blueRowLocked, blueColLocked, redRowLocked, redColLocked)
        else:
            print("Blue player turn")
            rowOrigin = int(input("Enter origin row: "))
            columnOrigin = int(input("Enter origin column: "))
            rowDestiny = int(input("Enter destiny row: "))
            columnDestiny = int(input("Enter destiny column: "))
            currentTurn, blueRowLocked,blueColLocked = move(rowOrigin, columnOrigin, rowDestiny, columnDestiny, board, "Blue", blueRowLocked, blueColLocked, redRowLocked, redColLocked)

board = [["R", "", "R", "","R"],
         ["", "R", "", "R",""],
         ["", "", "", "",""],
         ["", "B", "", "B",""],
         ["B", "", "B", "","B"]]
turn = "Red"
main(board, turn)
