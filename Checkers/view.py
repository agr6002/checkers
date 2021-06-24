from graphics import Point, Rectangle
from checker import Checker

class View:
    def __init__(self, win, board):
        print("  Constructing view.")
        self.win = win
        self.board = board
    def clear(self):
        for item in self.win.items[:]:
            item.undraw()
        self.win.update()
    def drawBoard(self):
        color = "black"
        for row in range(8):
            color = "black" if (color == "white") else "white"
            for col in range(8):
                color = "black" if (color == "white") else "white"
                rect = Rectangle(
                    Point(
                        col * self.win.width / 8,
                        row * self.win.height / 8
                    ),
                    Point(
                        (col + 1) * self.win.width / 8,
                        (row + 1) * self.win.height / 8
                    )
                )
                rect.setFill(color)
                rect.draw(self.win)
                #self.board[row][col] = color
    def drawCheckers(self):
        for row in self.board:
            for col in row:
                if col is not None:
                    col.draw()  
    def finalize(self):
        print("  Finalizing view.")
    def initialize(self):
        print("  Initializing view.")
        self.drawBoard()
        self.setCheckers()
        self.drawCheckers()
    def run(self):
        print("  Running view.")
        self.clear()
        self.drawBoard()
        self.drawCheckers()
    def setCheckers(self):
        for row in [0, 2, 6]:
            for col in [0, 2, 4, 6]:
                if row < 3:
                    self.board[row][col] = Checker(row, col, "red", 1, self.win)
                else:
                    self.board[row][col] = Checker(row, col, "blue", 1, self.win)
        for row in [1,5,7]:
            for col in [1,3,5,7]:
                if row < 3: 
                    self.board[row][col] = Checker(row, col, "red", 1, self.win)
                else:
                    self.board[row][col] = Checker(row, col, "blue", 1, self.win)