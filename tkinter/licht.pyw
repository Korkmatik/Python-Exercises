from tkinter import *

class Switch:
    def __init__(self):
        self.window = Tk()
        self.ein = 0
        self.label = Label(self.window, font=('Arial', 12), text='Licht aus', height=5, bg='black', fg='white', width=25)
        self.button = Button(self.window, text='O/I', command=self.switchLight)
        self.label.pack()
        self.button.pack(pady=10)

        self.window.mainloop()

    def switchLight(self):
        if self.ein:
            self.label.config(bg='white', fg='black', text='Licht ein')
            self.ein = 0
        else:
            self.label.config(bg='black', fg='white', text='Licht aus')
            self.ein = 1

switch = Switch()