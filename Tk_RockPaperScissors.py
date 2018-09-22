from Tkinter import *
from random import randrange


class RockPaperWindow(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.initWindow()

    def userExit(self):
        exit()

    def displayTypes(self, userType):
        foo = ['Rock', 'Paper', 'Scissors']

        self.randomIndex = randrange(len(foo))
        self.pcType = foo[self.randomIndex]

        self.pcDisplayLabel.delete(0, END)
        self.pcDisplayLabel.insert(0, self.pcType)

        self.userDisplayLabel.delete(0, END)
        self.userDisplayLabel.insert(0, userType)

        self.gamesEngine(userType, self.pcType)

    userPoints = 0
    pcPoints = 0
    def gamesEngine(self, userType, pcType):
        self.winText = ''


        if userType == 'Rock' and pcType == 'Paper':
            self.winText = "You lose, paper beats rock"
            self.pcPoints = self.pcPoints + 1

        elif userType == 'Rock' and pcType == 'Scissors':
            self.winText = "You win, rock beats scissors"
            self.userPoints = self.userPoints + 1

        elif userType == 'Paper' and pcType == 'Rock':
            self.winText = "You win, paper beats rock"
            self.userPoints = self.userPoints + 1

        elif userType == 'Paper' and pcType == 'Scissors':
            self.winText = "You lose, scissors beats paper"
            self.pcPoints = self.pcPoints + 1

        elif userType == 'Scissors' and pcType == 'Rock':
            self.winText = "You lose, rock beats scissors"
            self.pcPoints = self.pcPoints + 1

        elif userType == 'Scissors' and pcType == 'Paper':
            self.winText = "You win, scissors beats paper"
            self.userPoints = self.userPoints + 1

        else:
            self.winText = "You must chose Rock, Paper os Scissors!"
            # userMessageColor = "yellow"

        self.winDisplayLabel.delete(0, END)
        self.winDisplayLabel.insert(0, self.winText)

        self.userPointsDisplayLabel.delete(0, END)
        self.userPointsDisplayLabel.insert(0, self.userPoints)

        self.pcPointsDisplayLabel.delete(0, END)
        self.pcPointsDisplayLabel.insert(0, self.pcPoints)

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

        self.userPointsDisplayLabel = Entry(self, relief=RAISED, justify=RIGHT)
        self.userPointsDisplayLabel.grid(row=2, column=0, columnspan=7)
        self.userPointsDisplayLabel.insert(0, "0")

        self.pcPointsDisplayLabel = Entry(self, relief=RAISED, justify=RIGHT)
        self.pcPointsDisplayLabel.grid(row=2, column=11, columnspan=7)
        self.pcPointsDisplayLabel.insert(0, "0")

        rockButton = Button(self, text="ROCK", command=lambda: self.setRock())
        rockButton.grid(row=3, column=2)

        paperButton = Button(self, text="PAPER", command=lambda: self.setPaper())
        paperButton.grid(row=3, column=8)

        scissorsButton = Button(self, text="SCISSORS", command=lambda: self.setScissors())
        scissorsButton.grid(row=3, column=16)

        exitButton = Button(self, text="EXIT", command=lambda: self.userExit())
        exitButton.grid(row=5, column=4)



root = Tk()
root.title("ROCK-PAPER-SCISSORS")
app = RockPaperWindow(root)
root.mainloop()
