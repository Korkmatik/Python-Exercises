from tkinter import *
from tkinter import messagebox, filedialog

class Texteditor:
    def __init__(self):
        self.window = Tk()
        self.window.title('Texteditor')

        self.scrollbar = Scrollbar(self.window)
        self.text = Text(self.window, width=50, height=10, wrap=WORD, font=('Arial', 12), yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)


        self.text.pack(side=LEFT)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.__addMenu()

        self.window.mainloop()

    def __addMenu(self):
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        self.__addFileMenue()

    def __addFileMenue(self):
        self.filemenue = Menu(self.menu)
        self.filemenue.add_command(label='Laden', command=self.open)
        self.filemenue.add_command(label="Speichern unter..", command=self.save)
        self.filemenue.add_separator()
        self.filemenue.add_command(label="Ende", command=self.close)

        self.menu.add_cascade(label="Datei", menu=self.filemenue)

    def open(self):
        self.datei = filedialog.askopenfile()

        if self.datei:
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.datei.read())

        self.datei.close()
    
    def save(self):
        self.datei = filedialog.asksaveasfile()

        if self.datei:
            self.datei.write(self.text.get(1.0, END))

    def close(self):
        if messagebox.askyesno('Beenden', 
            'Möchten Sie wirklich das Programm beenden?'):
            self.window.destroy()

Texteditor()