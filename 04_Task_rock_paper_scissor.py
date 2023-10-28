from tkinter import *
import random
from tkinter import messagebox


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.comp_score = 0
        self.player_score = 0
        self.user_choice = ""
        self.computer_choice = ""
        self.result = ""
        self.label_comp_choice = None
        self.label_comp_score = None
        self.label_player_choice = None
        self.label_player_score = None
        self.result_label = None
        self.create_GUI()

    def check_win(self, c, u):
        if c == u:
            return "Tie!"
        elif c == "rock":
            if u == "scissor":
                return "You lost!"
            else:
                return "Congratulations, you won!"
        elif c == "paper":
            if u == "rock":
                return "You lost!"
            else:
                return "Congratulations, you won!"
        elif c == "scissor":
            if u == "paper":
                return "You lost!"
            else:
                return "Congratulations, you won!"

    def user_choice_handler(self, choice):
        self.user_choice = choice
        self.comp()

    def comp(self):
        num = random.randint(1, 3)

        if num == 1:
            self.computer_choice = "rock"
        elif num == 2:
            self.computer_choice = "paper"
        else:
            self.computer_choice = "scissor"

        self.result = self.check_win(self.computer_choice, self.user_choice)

        if self.result == "Congratulations, you won!":
            self.player_score += 1
        elif self.result == "You lost!":
            self.comp_score += 1

        self.result_label.configure(text=self.result)
        self.label_comp_choice.configure(text=self.computer_choice)
        self.label_comp_score.configure(text=self.comp_score)
        self.label_player_choice.configure(text=self.user_choice)
        self.label_player_score.configure(text=self.player_score)
        self.ask()

    def rock(self):
        self.user_choice = "rock"
        self.comp()

    def paper(self):
        self.user_choice = "paper"
        self.comp()

    def scissor(self):
        self.user_choice = "scissor"
        self.comp()

    def create_GUI(self):
        label1 = Label(
            self.root,
            text="Rock Paper Scissor Game",
            font=("Comic Sans MS", 20, "bold italic"),
            width=20,
            bd=5,
            bg="purple",
            fg="white",
        )
        label1.pack(side="top", fill=BOTH)

        Label(
            self.root,
            text="Choose Option: ",
            font="sarif 14 bold",
            width=12,
            bd=5,
            bg="grey",
            fg="beige",
        ).place(x=193, y=80)

        Label(
            self.root, text="Computer:", bg="grey", font="arial 18 bold", fg="yellow"
        ).place(x=30, y=100)
        Label(
            self.root,
            text="Choses:",
            font="calibri 16 bold italic",
            bg="grey",
            fg="blue",
        ).place(x=40, y=150)
        self.label_comp_choice = Label(
            self.root, font="calibri 14 bold", bg="grey", fg="white", width=8
        )
        self.label_comp_choice.place(x=30, y=200)

        Label(
            self.root,
            text="Score:",
            font="calibri 16 bold italic",
            bg="grey",
            fg="blue",
        ).place(x=40, y=250)
        self.label_comp_score = Label(
            self.root, font="calibri 14 bold", bg="grey", fg="white", width=8
        )
        self.label_comp_score.place(x=30, y=300)

        # /////////////////////////////////////////////////////////////////////////////////////////

        Label(
            self.root, text="Player:", bg="grey", font="arial 18 bold", fg="yellow"
        ).place(x=400, y=100)
        Label(
            self.root,
            text="Choses:",
            font="calibri 16 bold italic",
            bg="grey",
            fg="blue",
        ).place(x=410, y=150)
        self.label_player_choice = Label(
            self.root, font="calibri 14 bold", bg="grey", fg="white", width=8
        )
        self.label_player_choice.place(x=400, y=200)

        Label(
            self.root,
            text="Score:",
            font="calibri 16 bold italic",
            bg="grey",
            fg="blue",
        ).place(x=410, y=250)
        self.label_player_score = Label(
            self.root, font="calibri 14 bold", bg="grey", fg="white", width=8
        )
        self.label_player_score.place(x=400, y=300)

        Button(
            self.root,
            text="Rock",
            font="Helvetica 12 bold",
            width=12,
            bd=5,
            bg="beige",
            fg="black",
            command=self.rock,
        ).place(x=200, y=120)

        Button(
            self.root,
            text="Paper",
            font="Helvetica 12 bold",
            width=12,
            bd=5,
            bg="beige",
            fg="black",
            command=self.paper,
        ).place(x=200, y=170)

        Button(
            self.root,
            text="Scissor",
            font="Helvetica 12 bold",
            width=12,
            bd=5,
            bg="beige",
            fg="black",
            command=self.scissor,
        ).place(x=200, y=220)

        Button(
            self.root,
            text="Exit",
            font="Helvetica 12 bold",
            width=12,
            bd=5,
            bg="red",
            fg="black",
            command=self.root.destroy,
        ).place(x=200, y=270)

        self.result_label = Label(
            self.root,
            font="calibri 20 bold italic",
            width=20,
            bd=5,
            bg="white",
            fg="brown",
        )
        self.result_label.pack(side="bottom", fill=BOTH)
        self.result_label.config(text="Result")

    def ask(self):
        new_window = Toplevel()
        new_window.geometry("250x200+500+270")
        new_window.title("Another round")
        new_window.configure(bg="#17161b")
        new_window.resizable(False, False)

        new_window.grab_set()  # prevent interaction with main window

        def closingMessage():
            messagebox.showinfo(
                "Message",
                "Please select from the provided options.",
            )

        new_window.protocol("WM_DELETE_WINDOW", closingMessage)

        label_play = Label(
            new_window,
            text="Do you want to play \nanother round?",
            font=("calibri", 16, "bold italic"),
            width=1,
            bd=5,
            height=2,
            bg="#17161b",
            fg="white",
        )
        label_play.pack(side="top", fill=BOTH)

        Button(
            new_window,
            text="Yes",
            font="sarif 12 bold",
            width=5,
            bd=5,
            height=1,
            bg="#2a2d36",
            fg="white",
            command=new_window.destroy,
        ).place(x=100, y=80)
        Button(
            new_window,
            text="No",
            width=5,
            font="sarif 12 bold",
            bd=5,
            height=1,
            bg="#2a2d36",
            fg="white",
            command=exit,
        ).place(x=100, y=130)


def main():
    root = Tk()
    root.title("Rock Paper Scissor Game")
    root.geometry("540x450+350+150")
    root.configure(bg="gray")
    root.resizable(False, False)

    game = RockPaperScissorsGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
