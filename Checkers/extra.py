

from math import floor

turn = "red"
isPlaying = True
click1 = None
col1 = 0
row1 = 0
piece1 = None
click2 = None
col2 = 0
row2 = 0
piece2 = None
Key = None
midRow = -1
midCol = -1


    






def drawAll():
    clear(win)
    drawBoard()

def getCol(pointx):
    return floor(pointx / (SCREEN_WIDTH / 8))

def getRow(pointy):
    return floor(pointy / (SCREEN_HEIGHT / 8))


def getPieces():
    print(turn)
    getPiece1()
    getPiece2()

def getPiece1():
    global click1
    global col1
    global row1
    global piece1
    click1 = win.getMouse()
    col1 = getCol(click1.x)
    row1 = getRow(click1.y)
    piece1 = board[row1][col1]
    while (piece1 is None or piece1.color is not turn):
        click1 = win.getMouse()
        col1 = getCol(click1.x)
        row1 = getRow(click1.y)
        piece1 = board[row1][col1]
    print("FINALLY, YOU CLICKED THE RIGHT PIECE")

def getMidRow():
    global midRow
    if (row1 == row2 - 2):
        midRow= row2 - 1 
    elif (row1 == row2 + 2):
        midRow = row2 + 1 
    else:
        midRow = -1

def getMidCol():
    global midCol
    if (col1 == col2 - 2):
        midCol = col2 - 1
    elif (col1 == col2 + 2):
        midCol = col2 + 1
    else:
        midCol = -1   

def getIsPosCor():
    global col1
    global row1
    global col2
    global row2
    global turn
    global midRow
    global midCol
    getMidRow()
    getMidCol()
    print(midRow)
    print(midCol)
    print(board[midRow][midCol])
    notTurn = "red" if(turn == "blue") else "blue"
    if (
        (
                row1 == (row2 - 1)
            or
                row1 == (row2 + 1)
        )
        and 
        (
                col1 == (col2 - 1)
            or
                col1 == (col2 + 1)
        )
    ):
        return True
    elif (
                board[midRow][midCol] == Checker(midRow, midCol, notTurn, 1)
            and
                midRow != -1 
            and
                midCol != -1
    ):
        return True
    else:
        return False

def getPiece2():
    global click1
    global col1
    global row1
    global piece1
    global click2
    global col2
    global row2
    global piece2
    global Key
    global turn
    click2 = win.getMouse()
    col2 = getCol(click2.x)
    row2 = getRow(click2.y)
    piece2 = board[row2][col2]
    while (
            piece2 is not None
        or
            space[row2][col2] is "white"
        or
            (turn == "red" and row2 < row1)
        or
            (turn == "blue" and row2 > row1)
        or
            getIsPosCor() == False
    ):
        click2 = win.getMouse()
        col2 = getCol(click2.x)
        row2 = getRow(click2.y)
        piece2 = board[row2][col2]
        print("Click Again")
        Key = win.checkKey()
        print(Key)
        if(Key == "a"):
            getPieces()

def start():
    global turn
    global col1
    global row1
    global col2
    global row2
    while (isPlaying):
        drawAll()
        getPieces()
        if(Key == "a"):
            continue
        board[row1][col1] = None
        board[row2][col2] = Checker(row2, col2, turn, 1)
        #print("Done")
        turn = "red" if (turn == "blue") else "blue"


start()
