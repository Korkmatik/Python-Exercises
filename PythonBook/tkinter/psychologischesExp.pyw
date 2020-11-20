from tkinter import *
from random import *

class Psychology:
    def __init__(self):
        self.window = Tk()
        
        # Erstellen der gui elemente
        self.lblOrg = Label(self.window, width=5)
        self.scale = Scale(self.window, orient=HORIZONTAL, to=255, length=200, label='Helligkeit', showvalue=0, command=self.changeColour)
        self.lblUsr = Label(self.window, width=5)
        self.button = Button(self.window, text='check', command=self.check)
        self.lblWR = Label(self.window, width=20)

        self.layout()
        self.neu()

        self.window.mainloop()

    def layout(self):
        """Diese Funkton bestimmt das Layout der GUI Elemente"""
        self.lblOrg.pack(side=LEFT, fill=Y)
        self.lblUsr.pack(side=RIGHT, fill=Y)
        self.scale.pack(pady=5)        
        self.button.pack(pady=5)
        self.lblWR.pack(pady=5)

    def neu(self):
        ziffern = '0123456789ABCDEF'
        farbwert = choice(ziffern) + choice(ziffern)
        grau = '#' + 3 *farbwert
        self.lblOrg.config(bg=grau)
 
    def loesche(self):
        self.lblWR.config(text='')


    def check(self):
        """Diese Funktion checkt ob beide Graustufen der Labels gleich sind""" 
        links = self.lblOrg.cget('bg')
        rechts = self.lblUsr.cget('bg')

        if links==rechts:
            self.lblWR.config(text='gleiche Helligkeit')
        elif links < rechts:
            self.lblWR.config(text='Zu hell')
        else:
            self.lblWR.config(text='Zu dunkel')
        
        self.lblWR.after(1000, self.loesche)
        self.lblOrg.after(1000, self.neu)

    def changeColour(self, event):
        nr = hex(self.scale.get())
        farbwert = str(nr).lstrip('0x').zfill(2)
        grauton = '#' + 3 * farbwert 
        self.lblUsr.config(bg=grauton)

p = Psychology()