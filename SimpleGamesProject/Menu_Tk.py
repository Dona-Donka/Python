from Tkinter import *
from Tk_RockPaperScissors import RockPaperWindow


class Menu(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.initWindow()

    def userExit(self):
        exit()

    def rockPaperScissorsRun(self):
       #self.objcRock = RockPaperWindow(self)
        #self.objcRock.initWindow()
        # self.initWindow().run()
        root = Tk()
        root.title("ROCK-PAPER-SCISSORS")
        # root.configure(background="red")
        app = RockPaperWindow(root)
        root.mainloop()

    def initWindow(self):
        self.master.title("GAMES BOARD")
        self.pack(fill=BOTH, expand=1)
        self.configure(background="sea green", relief="ridge")

        self.helloLabel = Label(self, text='Hello in Games Board!', bg="sea green", font=("Comic Sans MS", 18, "bold"),
                                fg="floral white")
        self.helloLabel.grid(row=3, column=5)

        self.button1 = Button(self, text="Rock, Paper, Sissors", bg="sea green", font=("Comic Sans MS", 10),
                              fg="floral white")
        self.button1.configure(command=self.rockPaperScissorsRun)
        self.button1.grid(row=10, column=0)

        self.button2 = Button(self, text="Guess the number", bg="sea green", font=("Comic Sans MS", 10),
                              fg="floral white")
        self.button2.grid(row=10, column=12)


if __name__ == "__main__":
    root = Tk()
    root.title("GAMES BOARD")
    app = Menu(root)
    root.mainloop()

