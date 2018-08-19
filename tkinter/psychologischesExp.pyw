from tkinter import *

class Psychology:
    def __init__(self):
        self.window = Tk()
        
        # Erstellen der gui elemente
        self.lblOrg = Label(self.window, bg='grey', width=5)
        self.lblScale = Label(self.window, text='Helligkeit', font=('Arial', 12))
        self.scale = Scale(self.window, orient=HORIZONTAL, resolution=0.5, to=100)
        self.lblUsr = Label(self.window, bg='grey', width=5)
        self.button = Button(self.window, text='check', command=self.check)
        self.lblWR = Label(self.window, width=20)

        self.layout()

        self.window.mainloop()

    def layout(self):
        """Diese Funkton bestimmt das Layout der GUI Elemente"""
        self.lblOrg.pack(side=LEFT, fill=Y)
        self.lblUsr.pack(side=RIGHT, fill=Y)
        self.lblScale.pack(pady=5)
        self.scale.pack(pady=5)        
        self.button.pack(pady=5)
        self.lblWR.pack(pady=5)

    def check(self):
        """Diese Funktion checkt ob beide Graustufen der Labels gleich sind"""
        pass

p = Psychology()