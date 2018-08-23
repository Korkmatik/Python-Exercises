import tkinter
from threading import Thread
from time import localtime, sleep

class Digitaluhr:
    def __init__(self):
        self.window = tkinter.Tk()
        self.txtTime = tkinter.Label(self.window, text='Uhrzeit', font=('Arial', 14), height=1)
        self.txtTime.pack(padx=5, pady=5)
        Uhrzeit(self.txtTime)

        self.window.mainloop()

class Uhrzeit(Thread):
    def __init__(self, time):
        Thread.__init__(self)
        self.time = time

        self.start()

    def __getTime(self):
        """returns current time in a readable form"""
        hours = str(localtime()[3])
        minutes = str(localtime()[4])
        seconds = str(localtime()[5])

        return hours + ":" + minutes + ":" + seconds

    def run(self):
        while True:
            self.time.config(text=self.__getTime())
            sleep(1)

Digitaluhr()