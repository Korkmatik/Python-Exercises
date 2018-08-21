import tkinter

class Gui():
    """The Graphical User Interface of this program"""
    
    def __init__(self):
        self.window = tkinter.Tk()
        self.image = Image()

        self.__initUserinterface()
        self.__initLayout()
        
        self.button = BtnContinue(self.window, self.cImg, self.image, self.lblDescription)

        self.window.mainloop()

    def __initUserinterface(self):        
        self.img = self.image.getImage()
        self.pic = tkinter.PhotoImage(file=self.img[0])
        self.cImg = tkinter.Canvas(self.window, width=self.pic.width(), height=self.pic.height())
        self.cImg.create_image(0, 0, image=self.pic, anchor=tkinter.NW)
        self.lblDescription = tkinter.Label(self.window, font=('Arial', 14), text=self.img[1])

    def __initLayout(self):
        self.cImg.pack(padx=2)
        self.lblDescription.pack(anchor=tkinter.CENTER, pady=3)

class BtnContinue:
    """A button to Display the next Image"""
    def __init__(self, window, canvas, image, description):
        self.window = window
        self.canvas = canvas
        self.image = image
        self.description = description

        self.__initButton()

    def __initButton(self):
        self.icon = tkinter.PhotoImage(file="Bilder\\weiter.gif")

        self.btn = tkinter.Button(self.window, image=self.icon, command=self.__next)
        self.btn.pack(pady=3, anchor=tkinter.CENTER)

    def __next(self):
        self.img, self.txt = self.image.getImage()
        self.lastimg = tkinter.PhotoImage(file=self.img)

        self.description.config(text=self.txt)
        self.canvas.itemconfigure(1, image=self.lastimg)

class Image:
    """Contains Images which should be shown and a Method to get the next Image from the list"""
    directory = 'Bilder\\'
    images = [('dalton.gif', 'Ein Dalton'), ('museum.gif', 'Ein Museum'), ('tuer.gif', 'Eine Tür')]
    currentImage = 0

    def getImage(self):
        if self.currentImage < len(self.images):
            img = (self.directory + self.images[self.currentImage][0], self.images[self.currentImage][1])
            self.currentImage += 1
            return img
        else:
            self.currentImage = 0
            img = (self.directory + self.images[self.currentImage][0], self.images[self.currentImage][1])
            self.currentImage += 1
            return img

Gui()