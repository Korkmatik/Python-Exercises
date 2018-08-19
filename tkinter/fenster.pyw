def gruessen():
    fenster.label.config(text='Hallo!')


from tkinter import *

fenster =Tk()
fenster.label = Label(master=fenster, text='Begrüßung')
fenster.label.pack()
fenster.button = Button(master=fenster, text='Sage Hallo', command=gruessen)
fenster.button.pack()

fenster.mainloop()