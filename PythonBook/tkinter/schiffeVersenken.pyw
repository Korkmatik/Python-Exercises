from tkinter import *
from random import *

class Feld:
    def __init__(self, spiel, x, y):
        self.x = x
        self.y = y
        self.spiel = spiel
        self.button = Button(self.spiel.fenster, height=1, width=2, command=self.press)
        self.button.grid(column=x, row=y)

    def press(self):
        check = self.spiel.spielfeld.checkTreffer
        if check(self.x, self.y):
            self.button.config(bg='blue')
        else:
            self.button.config(bg='white')

class Spielfeld:
    def __init__(self):
        self.d = {}
        for i in range(12):
            for j in range(12):
                self.d[(i, j)] = 0
        for i in range(4): self.setzeBoot(1)
        for i in range(3): self.setzeBoot(2)
        for i in range(2): self.setzeBoot(3)
        self.setzeBoot(4)

    def setzeBoot(self, laenge):
        max = 11 - laenge
        ok = 0
        if choice([0, 1]):
            # Schiff ist waagrecht
            y = randint(1, 10)
            x = randint(1, max)

            if self.check(x, y, x+laenge-1, y):
                for x in range(x, x+laenge):
                    self.d[(x, y)] = 1
        else:
            x = randint(1, 10)
            y = randint(1, max)
            if self.check(x, y, x, y+laenge-1):
                for y in range(y, y+laenge):
                    self.d[(x, y)] = 1
                ok = 1

    def check(self, x1, y1, x2, y2):
        ok = 1
        for x in range(x1-1, x2+2):
            for y in range(y1-1, y2+2):
                if self.d[x,y]: ok=0
        return 0

    def checkTreffer(self, x, y):
        return self.d[x, y]

class Schiffeversenken:
    def __init__(self):
        self.fenster = Tk()
        self.spielfeld = Spielfeld()
        for x in range(12):
            for y in range(12):
                button= Feld(self, x, y)
        self.fenster.mainloop()

spiel = Schiffeversenken()