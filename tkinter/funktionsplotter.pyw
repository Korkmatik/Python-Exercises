from tkinter import Tk, Entry, Button, Label, Canvas, LEFT, LAST

class Funktionsplotter:
    def __init__(self):
        
        self.window = Tk()
        self.window.title('Funktionsplotter')

        self.initGui()

        self.window.mainloop()
        
    def initGui(self):
        """All widgets of the GUI"""
        self.lbl = Label(self.window, text='f(x)=', font=('Arial', 12))
        self.inFunction = Entry(self.window)
        self.btnPlot = Button(self.window, text='Plot', command=self.drawFunction)
        self.graphic = Canvas(self.window, width='6c', height='6c', bg='white')
        self.graphic.create_line(10,80,150,80, arrow=LAST)
        self.graphic.create_line(80,150,80,10, arrow=LAST)
        self.graphic.create_text(90,90, text='1')
        self.graph = self.graphic.create_line(30,80,130,80, width=2, fill='red')

        self.layout()

    def layout(self):
        """the Layout of the GUI"""
        self.lbl.pack(side=LEFT, padx=5)
        self.inFunction.pack(side=LEFT, padx=5)
        self.btnPlot.pack(side=LEFT, padx=5)
        self.graphic.pack(padx=10)

    def drawFunction(self):
        """Draws the function into the Canvas"""
        results = self.plot()

        if len(results):
            self.graphic.coords(self.graph, 30, results[-5], 40, results[-4], 50, results[-3], 
                60, results[-2], 70, results[-1], 80, results[0], 90, results[1], 100, results[2], 110, results[3], 120, results[4], 130, results[5])

    def plot(self):
        """Calculates all y-Values from x=-5 to x=5 and saves it into and list
            method returns a list with these results"""
        results = {}
        
        for x in range(-5, 6, 1):
            results[x] = 80 - 10 * eval(self.inFunction.get())

        return results        

Funktionsplotter()