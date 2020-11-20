from tkinter import *

fenster = Tk()
bild = PhotoImage(file='Bilder\\tuer.gif')
Label(fenster, image=bild).pack()
fenster.mainloop()