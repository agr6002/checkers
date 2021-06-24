class Model:
    def __init__(self, board, space):
        print("  Constructing model.")
        self.board = board
        self.space = space
    def finalize(self):
        print("  Finalizing model.")
        
    def initialize(self):
        print("  Initializing model.")
        self.setBoard()
        #self.setCheckers()
        #self.setSpace()
    def run(self):
        print("  Running model.")
        #self.setSpace()
    def setBoard(self):
            color = "black"
            for row in range(8):
                color = "black" if (color == "white") else "white"
                for col in range(8):
                    color = "black" if (color == "white") else "white"
                    if(color == "white"):
                        self.space[row][col] = "white"
                    elif(color == "black"):
                        self.space[row][col] = "black"
                        continue
                    else:
                        print("color wrong")
    def setCheckers(self):
        for row in [0, 2, 6]:
            for col in [0, 2, 4, 6]:
                if row < 3:
                    self.space[row][col] = "red"
                else:
                    self.space[row][col] = "blue"
        for row in [1,5,7]:
            for col in [1,3,5,7]:
                if row < 3: 
                    self.space[row][col] = "red"
                else:
                    self.space[row][col] = "blue"
    def setSpace(self):
        row = -1
        #col = 0
        for rows in self.space:
            col = -1
            row += 1
            for cols in rows:
                col += 1
                if(self.board[row][col] == None and self.space[row][col] != "white"):
                    self.space[row][col] = "black"
                elif(self.board[row][col] == None and self.space[row][col] == "white"):
                    self.space[row][col] = "white"
                else:
                    self.space[row][col] = self.board[row][col].color
        print(self.space)


