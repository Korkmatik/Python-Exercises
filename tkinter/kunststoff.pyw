from tkinter import *

TEXTE = "Es ist {}"

class Kunststoff:

    def __init__(self):

        self.window = Tk()
        self.window.title('Kunststoff')

        # density
        Label(self.window, text="Dichte", font=('Arial', 16)).pack(pady=5)
        self.doesSwim= IntVar()
        self.rbSwim = Radiobutton(self.window, text='schwimmt', value=1, variable=self.doesSwim)
        self.rbNoSwim = Radiobutton(self.window, text='schwimmt nicht', value=0, variable=self.doesSwim)
        self.rbSwim.pack()
        self.rbNoSwim.pack()

        # flammability
        Label(self.window, text='Brennbarkeit', font=('Arial', 16)).pack(pady=5)
        self.doesBurn = IntVar()
        self.rbBurn = Radiobutton(self.window, text='brennt', value=1, variable=self.doesBurn)
        self.rbNoBurn = Radiobutton(self.window, text='brennt nicht', value=0, variable=self.doesBurn)
        self.rbBurn.pack()
        self.rbNoBurn.pack()

        # habits while burning
        Label(self.window, text='Verhalten beim Verbrennen', font=('Arial', 16)).pack(pady=5, padx= 10)
        self.habits = StringVar()
        self.flame, self.drips, self.smell = IntVar(), IntVar(), IntVar()
        self.check = []

        for text, habit in [('rußende Flamme', self.flame), ('tropft', self.drips), ('duftet nach Wachs', self.smell)]:
            self.check.append(Checkbutton(self.window, text=text, offvalue=0, onvalue=1, variable=habit))

        for checkbox in self.check:
            checkbox.pack()

        # button for submit
        Button(self.window, text='Auswertung', command=self.evaluation).pack(pady=10)

        # label for result
        self.result = Label(self.window, font=('Arial', 16))
        self.result.pack(pady=5)
        
        self.window.mainloop()

       
    def evaluation(self):
        burn, swim, smell, drips, flame = self.doesBurn.get(), self.doesSwim.get(), self.smell.get(), self.drips.get(), self.flame.get()
        if burn and swim and smell and drips:
            self.result.config(text=TEXTE.format('Polyehtylen (PE)'))
        elif burn and flame:
            self.result.config(text=TEXTE.format('Polystyrol (PS)'))
        elif not (burn or swim or flame or drips or smell):
            self.result.config(text=TEXTE.format('Polyvinylchlorid (PVC)'))
        else:
            self.result.config(text='Kunststoff unbekannt')

if __name__ == '__main__':
    k = Kunststoff()