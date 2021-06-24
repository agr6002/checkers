from graphics import Circle, Point

class Checker:
    def __init__(self, row, colum, color, status, win):
        self.row= row
        self.colum = colum
        self.color = color
        self.status = status
        self.win = win
    def draw(self):
        circ = Circle(
            Point(
                self.win.width / 16 + self.colum * self.win.width / 8, 
                self.win.height / 16 + self.row * self.win.height / 8
            ), 
            self.win.width / 16
        )
        circ.setFill(self.color)
        circ.draw(self.win)
