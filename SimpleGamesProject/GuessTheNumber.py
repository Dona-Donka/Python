#!/usr/bin/env python
import random
from Tkinter import *


class GuessTheNumber(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.initWindow()

    def initWindow(self):
        self.master.title("GUESS THE NUMBER")
        self.pack(fill=BOTH, expand=1)

        self.winDisplayLabel = Entry(self, relief=RAISED, justify=RIGHT)
        self.winDisplayLabel.grid(row=0, column=0, columnspan=15)
        self.winDisplayLabel.insert(0, "")

        self.displayLabel = Entry(self, relief=RAISED, justify=RIGHT)
        self.displayLabel.grid(row=3, column=0, columnspan=15)
        self.displayLabel.insert(0, "Set the number")

        button = Button(self, text="CHECK", command=lambda: self.setNumber(text.get()))
        button.grid(row=3, column=20)

    def setNumber(self, text):
        print text

    def gameEngine(self, usersNumber):
        PCsNumber = random.randint(0, 100)
        #usersNumber = displayLabel.get(usersNumber)
        self.displayMessage = ""

        while usersNumber != PCsNumber:
            if (usersNumber > PCsNumber):
                self.displayMessage = "My number is smaller!"
            elif (usersNumber < PCsNumber):
                self.displayMessage = "My number is bigger!"

        self.displayMessage = "Congratulations! you guessed it!"

        self.winDisplayLabel.delete(0, END)
        self.winDisplayLabel.insert(0, self.displayMessage)


if __name__ == "__main__":
    root = Tk()
    root.title("GUESS THE NUMBER")
    # root.configure(background="red")
    app = GuessTheNumber(root)
    root.mainloop()
