from model import Model
from view import View
from controller import Controller
from graphics import GraphWin

TITLE = "Checkers"
win = False
turn = "red"

class App:
    def __init__(self, screenWidth, screenHeight, board, space):
        print("Constructing app.")
        global turn
        self.board = board
        self.space = space
        self.win = GraphWin(TITLE, screenWidth, screenHeight)
        self.model = Model(self.board, self.space)
        self.view = View(self.win, self.board)
        self.controller = Controller(self.win, self.board, self.space, turn)
    def launch(self):
        print("Launching app.")
        self.initialize()
        self.run()
        self.finalize()
    def finalize(self):
        print("Finalizing app.")
        self.model.finalize()
        self.view.finalize()
        self.controller.finalize()
    def initialize(self):
        print("Initializing app.")
        print(self.space)
        self.model.initialize()
        print(self.space)
        self.view.initialize()
        self.controller.initialize()
    def run(self):
        print("Running app.")
        while(win == False):
            global turn
            self.controller = Controller(self.win, self.board, self.space, turn )
            print(turn)
            self.model.run()
            self.view.run()
            self.controller.run()
            turn = "blue" if(turn == "red") else "red"
            #print("change" + turn)
        input("Press <ENTER> to continue.")  