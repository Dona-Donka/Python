from Tkinter import *
from random import randrange


class RockPaperWindow(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.initWindow()

    def displayTypes(self, userType):
        foo = ['Rock', 'Paper', 'Scissors']

        self.randomIndex = randrange(len(foo))
        self.pcType = foo[self.randomIndex]

        self.pcDisplayLabel.delete(0, END)
        self.pcDisplayLabel.insert(0, self.pcType)

        self.userDisplayLabel.delete(0, END)
        self.userDisplayLabel.insert(0, userType)

        self.gamesEngine(userType, self.pcType)

    def gamesEngine(self, userType, pcType):
        self.winText = ''

        if userType == 'Rock' and pcType == 'Paper':
            self.winText = "You lose, papper beats rock"

        elif userType == 'Paper' and pcType == 'Rock':
            self.winText = "You win, paper beats rock"

        elif userType == 'Scissors' and pcType == 'Rock':
            self.winText = "You lose, rock beats scissors"

        elif userType == 'Rock' and pcType == 'Scissors':
            self.winText = "You win, rock beats scissors"


        else:
            self.winText = "You must chose Rock, Paper os Scissors!"
            # userMessageColor = "yellow"

        self.winDisplayLabel.delete(0, END)
        self.winDisplayLabel.insert(0, self.winText)

    def setRock(self):
        userType = 'Rock'
        self.displayTypes(userType)

    def setPaper(self):
        userType = 'Paper'
        self.displayTypes(userType)

    def setScissors(self):
        userType = 'Scissors'
        self.displayTypes(userType)

    def initWindow(self):
        self.master.title("ROCK-PAPER-SCISSORS")
        self.pack(fill=BOTH, expand=1)

        self.winDisplayLabel = Entry(self, relief=RAISED, justify=RIGHT)
        self.winDisplayLabel.grid(row=0, column=0, columnspan=15)
        self.winDisplayLabel.insert(0, "")

        self.userDisplayLabel = Entry(self, relief=RAISED, justify=RIGHT)
        self.userDisplayLabel.grid(row=1, column=0, columnspan=7)
        self.userDisplayLabel.insert(0, "YOUR TYPE")

        self.pcDisplayLabel = Entry(self, relief=RAISED, justify=RIGHT)
        self.pcDisplayLabel.grid(row=1, column=11, columnspan=7)
        self.pcDisplayLabel.insert(0, "COMPUTER TYPE")

        rockButton = Button(self, text="ROCK", command=lambda: self.setRock())
        rockButton.grid(row=2, column=2)

        paperButton = Button(self, text="PAPER", command=lambda: self.setPaper())
        paperButton.grid(row=2, column=8)

        scissorsButton = Button(self, text="SCISSORS", command=lambda: self.setScissors())
        scissorsButton.grid(row=2, column=16)


root = Tk()
root.title("ROCK-PAPER-SCISSORS")
app = RockPaperWindow(root)
root.mainloop()
