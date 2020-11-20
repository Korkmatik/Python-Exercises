from tkinter import *
import random

class GUI():
    """Gui layout for the game"""
    def __init__(self):
        self.game = Game()
        self.window = Tk()
        self.lbl = Label(self, text='Wörterraten', font=('Arial', 16))
        self.lblPoints = Label(self, text="0", font=('Arial', 16))
        self.lblWord = Label(self, font=('Arial', 16), bg='white')
        self.language = StringVar()
        self.rbEnglish = Radiobutton(self, text='Englisch', variable=self.language, value='engl')
        self.rbGerman = Radiobutton(self, text='Deutsch', variable=self.language, value='ger')
        self.btnNew = Button(self, text='Neu', command=self.game.newGame)
        self.inLetter = Entry(self, width=1)
        self.btnSubmit = Button(self, text='OK', command=self.game.check)
        self.rbGerman.select()

        self.layout()

        self.window.mainloop()

    def layout(self):
        self.lbl.grid(column=1, row=1)
        self.lblPoints.grid(column=4, row=1)
        self.lblWord.grid(column=2, row=2)
        self.rbEnglish.grid(column=1, row=3)
        self.rbGerman.grid(column=1, row=4)
        self.btnNew.grid(column=3, row=3)
        self.inLetter.grid(column=4, row=3)
        self.btnSubmit.grid(column=5, row=3)
        
class Game():
    """The main logic of the game"""
    def __init__(self):
        pass

    def check(self):
        """Checks if the word contains the Letter typed in the Entry: inLetter"""
        pass

    def newGame(self):
        """Starts a new Game with a new word"""
        pass

t = GUI()