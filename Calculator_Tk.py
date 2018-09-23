from Tkinter import *


class Window(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.initWindow()

    def replaceNumber(self, text):
        self.displayLabel.delete(0, END)
        self.displayLabel.insert(0, text)

    def calcExpr(self):
        self.expression = self.displayLabel.get()

        try:
            self.result = eval(self.expression)
            self.replaceNumber(self.result)

        except:
            pass

        print(self.result)

    def displayNumber(self, text):
        self.entryText = self.displayLabel.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceNumber(text)
        else:
            self.displayLabel.insert(self.textLength, text)

    def clearText(self):
        self.replaceNumber("0")

    def initWindow(self):

        self.master.title("CALCULATOR")
        self.pack(fill=BOTH, expand=1)


        self.displayLabel = Entry(self, relief=RAISED, justify=RIGHT)
        self.displayLabel.grid(row=0, column=0, columnspan=5)
        self.displayLabel.insert(0, "0")

        oneButton = Button(self, text="1", bg="wheat2", command=lambda: self.displayNumber("1"))
        oneButton.grid(row=1, column=0)

        twoButton = Button(self, text="2", bg="wheat2", command=lambda: self.displayNumber("2"))
        twoButton.grid(row=1, column=1)

        threeButton = Button(self, text="3", bg="wheat2", command=lambda: self.displayNumber("3"))
        threeButton.grid(row=1, column=2)

        fourButton = Button(self, text="4", bg="wheat2", command=lambda: self.displayNumber("4"))
        fourButton.grid(row=2, column=0)

        fiveButton = Button(self, text="5", bg="wheat2", command=lambda: self.displayNumber("5"))
        fiveButton.grid(row=2, column=1)

        sixButton = Button(self, text="6", bg="wheat2",command=lambda: self.displayNumber("6"))
        sixButton.grid(row=2, column=2)

        sevenButton = Button(self, text="7", bg="wheat2", command=lambda: self.displayNumber("7"))
        sevenButton.grid(row=3, column=0)

        eightButton = Button(self, text="8", bg="wheat2", command=lambda: self.displayNumber("8"))
        eightButton.grid(row=3, column=1)

        nineButton = Button(self, text="9", bg="wheat2", command=lambda: self.displayNumber("9"))
        nineButton.grid(row=3, column=2)

        zeroButton = Button(self, text="0", bg="burlywood4", command=lambda: self.displayNumber("0"))
        zeroButton.grid(row=4, column=0)

        # Mathematical operates buttons:

        addButton = Button(self, text="+", bg="burlywood4", command=lambda: self.displayNumber(" + "))
        addButton.grid(row=1, column=3)

        subButton = Button(self, text=" -", bg="burlywood4", command=lambda: self.displayNumber(" - "))
        subButton.grid(row=2, column=3)

        exprButton = Button(self, text="=", bg="burlywood4", command=lambda: self.calcExpr())
        exprButton.grid(row=3, column=3)

        divButton = Button(self, text="/", bg="burlywood4", command=lambda: self.displayNumber("/"))
        divButton.grid(row=4, column=1)

        multButton = Button(self, text="*", bg="burlywood4", command=lambda: self.displayNumber("*"))
        multButton.grid(row=4, column=2)

        clearButton = Button(self, text="C",bg ="brown3", command=lambda: self.clearText())
        clearButton.grid(row=4, column=3)

        # quitButton = Button(self, text = "EXIT", command = self.userExit)
        # quitButton.place(x=290, y =450)


    def userExit(self):
        exit()


root = Tk()
root.grid()
app = Window(root)
root.mainloop()
