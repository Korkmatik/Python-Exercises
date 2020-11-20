from tkinter import *
from random import choice

class Memory:
    
    def __init__(self):

        self.window = Tk()

        self.__initGUI()

        self.window.mainloop()

    def __initGUI(self):

        self.__initCards()

        self.btnNew = Button(self.window, text='Neu', command=self.__new)
        self.btnNew.pack(side=RIGHT, padx=2, pady=2)

    def __new(self):
        pass

    def __initCards(self):
        pathBackCard = 'Bilder\\rueck.gif'
        pathNoCard = 'Bilder\\hell.gif'        
        pathCards = [['Bilder\\dreieck.gif', 2], ['Bilder\\kreis.gif', 2], ['Bilder\\krone.gif', 2], ['Bilder\\mond.gif', 2], \
                    ['Bilder\\pfeil.gif', 2], ['Bilder\\pilz.gif', 2], ['Bilder\\quadrat.gif', 2], ['Bilder\\raute.gif', 2]]

        self.__cards = [] # will conatain the sequence of the memory cards

        # filling self.__cards randomly 
        for i in range(len(pathCards)*2):
            randNumbers = [0,1,2,3,4,5,6,7]
            while True:
                rand = choice(randNumbers)
                if pathCards[rand][1] != 0: # checks if the card is already twice in self.__cards
                    self.__cards = pathCards[rand][0]
                    pathCards[rand][1] -= 1
                    continue
                else:
                    if len(randNumbers) < 1:
                        randNumbers.remove(rand)
                    else:
                        continue

        # filling the playground with the cards, back is up
        self.picBackCard = PhotoImage(file=pathBackCard)

        self.card0 = Label(self.window, image=self.picBackCard)
        self.card1 = Label(self.window, image=self.picBackCard)
        self.card2 = Label(self.window, image=self.picBackCard)
        self.card3 = Label(self.window, image=self.picBackCard)
        self.card4 = Label(self.window, image=self.picBackCard)
        self.card5 = Label(self.window, image=self.picBackCard)
        self.card6 = Label(self.window, image=self.picBackCard)
        self.card7 = Label(self.window, image=self.picBackCard)
        self.card8 = Label(self.window, image=self.picBackCard)
        self.card9 = Label(self.window, image=self.picBackCard)
        self.card10 = Label(self.window, image=self.picBackCard)
        self.card11 = Label(self.window, image=self.picBackCard)
        self.card12 = Label(self.window, image=self.picBackCard)
        self.card13 = Label(self.window, image=self.picBackCard)
        self.card14 = Label(self.window, image=self.picBackCard)
        self.card15 = Label(self.window, image=self.picBackCard)

        self.card0.grid(x=0, y=0)
        self.card1.grid(x=1, y=0)
        self.card2.grid(x=2, y=0)
        self.card3.grid(x=3, y=0)
        self.card4.grid(x=0, y=1)
        self.card5.grid(x=1, y=1)
        self.card6.grid(x=2, y=1)
        self.card7.grid(x=3, y=1)
        self.card8.grid(x=0, y=2)
        self.card9.grid(x=1, y=2)
        self.card10.grid(x=2, y=2)
        self.card11.grid(x=3, y=2)
        self.card12.grid(x=0, y=3)
        self.card13.grid(x=1, y=3)
        self.card14.grid(x=2, y=3)
        self.card15.grid(x=3, y=3)


Memory()