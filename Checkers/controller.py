from math import floor
from checker import Checker

num = 0

class Controller:
    def __init__(self, win, board, space, turn):
        print("  Constructing controller.")
        self.board = board
        self.space = space
        self.win = win
        self.turn = turn
    def finalize(self):
        print("  Finalizing controller.")
    def getCol(self, pointx):
        return floor(pointx / (self.win.width / 8))
    def getIsPosCor(self):
        self.midRow = self.getMidRow()
        self.midCol = self.getMidCol()
        notTurn = "red" if(self.turn == "blue") else "blue"
        #print("    Not Turn " + notTurn)
        #print("    Mid Row " + str(self.midRow))
        #print("    Mid Col " + str(self.midCol))
        #print(self.space[self.midRow][self.midCol])
        #if(self.space[self.midRow][self.midCol] == notTurn):
        #    print("    fail")
        if (
            (
                    self.row1 == (self.row2 - 1)
                or
                    self.row1 == (self.row2 + 1)
            )
            and 
            (
                    self.col1 == (self.col2 - 1)
                or
                    self.col1 == (self.col2 + 1)
            )
        ):
            return True
        elif (
                    self.midRow != False
                and
                    self.midCol != False
                and
                    self.board[self.midRow][self.midCol].color == notTurn
                    #self.board[self.midRow][self.midCol] == Checker(self.midRow, self.midCol, notTurn, 1, self.win)
        ):
            return True
        else:
            return False
    def getMidCol(self):
        if (self.col1 == self.col2 - 2):
            return self.col1 + 1
        elif (self.col1 == self.col2 + 2):
            return self.col1 - 1
        else:
            return False
    def getMidRow(self):
        if (self.row1 == self.row2 - 2):
            return self.row1 + 1 
        elif (self.row1 == self.row2 + 2):
            return self.row1 - 1
        else:
            return False
    def getPiece1(self):
        click1 = self.win.getMouse()
        self.col1 = self.getCol(click1.x)
        self.row1 = self.getRow(click1.y)
        piece1 = self.board[self.row1][self.col1]
        while (piece1 is None or piece1.color is not self.turn):
            click1 = self.win.getMouse()
            self.col1 = self.getCol(click1.x)
            self.row1 = self.getRow(click1.y)
            piece1 = self.board[self.row1][self.col1]
            print("    wrong first click")
        print("    right first click")
    def getPiece2(self):
        click2 = self.win.getMouse()
        self.col2 = self.getCol(click2.x)
        self.row2 = self.getRow(click2.y)
        piece2 = self.board[self.row2][self.col2]
        #print(self.getIsPosCor())
        while (
                piece2 is not None
            or
                self.space[self.row2][self.col2] is "white"
            or
                (self.turn == "red" and self.row2 < self.row1)
            or
                (self.turn == "blue" and self.row2 > self.row1)
            or
                self.getIsPosCor()  == False
        ):
            print("    Click Again")
            click2 = self.win.getMouse()
            self.col2 = self.getCol(click2.x)
            self.row2 = self.getRow(click2.y)
            piece2 = self.board[self.row2][self.col2]
            print(self.getIsPosCor())
            # Key = self.win.checkKey()
            # print(Key)
            # if(Key == "a"):
            #     #self.getPieces()
            #     #continue
            #     return False
        print("    worked")
        return True
    def getPieces(self):
        global num
        num = num + 1
        self.getPiece1()
        while(self.getPiece2() == False):
            print("    wrong second click")
            self.getPieces()
        else:
            self.board[self.row1][self.col1] = None
            self.board[self.row2][self.col2] = Checker(self.row2, self.col2, self.turn, 1, self.win)
            print("    right second click")
        #print(num)
    def getRow(self, pointy):
        return floor(pointy / (self.win.height / 8))

    def initialize(self):
        print("  Initializing controller.")
        #print("    con I " + self.turn)
    def run(self):
        print("  Running controller.")
        #print("    con R " + self.turn)
        self.getPieces()
