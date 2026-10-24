import tkinter as tk 
import random

class Main:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title("Rock Paper Scissor")

        self.title = tk.Label(self.root, text="Rock Paper Scissor", font=('Arial', 18))
        self.title.pack()

        self.button_rock = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"))
        self.button_rock.pack(padx=10,pady=10)

        self.button_paper = tk.Button(self.root, text="paper", command=lambda: self.play("paper"))
        self.button_paper.pack(padx=10,pady=10)

        self.button_rock = tk.Button(self.root, text="scissor", command=lambda: self.play("scissor"))
        self.button_rock.pack(padx=10,pady=10)

        self.result = tk.Label(self.root, font=('Arial', 18))
        self.result.pack(padx=10, pady=10)

        self.score = tk.Label(self.root, font=('Arial', 18))
        self.score.pack(padx=10, pady=10)

        self.computer_score = 0
        self.player_score = 0

        self.root.mainloop()
    def play(self, player: str):
        self.option = ("rock", "paper", "scissor")
        self.computer = random.choice(self.option)

        if (self.computer == "rock" and player == "paper") or \
           (self.computer == "paper" and player == "scissor") or \
           (self.computer == "scissor" and player == "rock"):
            self.result.config(text="You Win")
            self.player_score += 1
            self.score.config(text=f'Computer: {self.computer_score} \n Player: {self.player_score}')
        else:
            self.result.config(text="You lose")
            self.computer_score += 1
            self.score.config(text=f'Computer: {self.computer_score} \n Player: {self.player_score}')

Main()