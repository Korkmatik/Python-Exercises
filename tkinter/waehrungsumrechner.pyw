from tkinter import *

class Waehrungsumrechner:

    def __init__(self):
        self.window = Tk()
        self.window.title('Währungen')

        self.label = Label(self.window, text="Geben Sie einen Betrag in Euro ein\nund wählen Sie eine Währung", font=('Arial', 16))
        self.label.pack(padx=10, pady=5)

        self.entry = Entry(self.window)
        self.entry.pack()

        self.currency = StringVar()
        self.radioButUSD = Radiobutton(self.window, text='US-Dollar', variable=self.currency, value='USD')
        self.radioButUSD.select()
        self.radioButUSD.pack()
        self.radioButGBP = Radiobutton(self.window, text='Britische Pfund', variable=self.currency, value='GBP')
        self.radioButGBP.pack()

        self.button = Button(self.window, text='Rechnung', command=self.convert)
        self.button.pack(pady=10)

        self.result = Label(self.window, font=('Arial', 16))
        self.result.pack(pady=5)

        self.window.mainloop()

    def convert(self):
        result = 0.0

        if self.currency.get() == 'USD':
            result = float(self.entry.get()) * 1.14
            text = str(result) + ' USD'
            self.result.config(text=text)
        elif self.currency.get() == 'GBP':
            result = float(self.entry.get()) * 0.897
            text = str(result) + ' GBP'
            self.result.config(text=text)            

wu = Waehrungsumrechner()