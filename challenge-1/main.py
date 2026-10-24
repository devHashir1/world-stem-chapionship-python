import random
import tkinter as tk 
from tkinter import messagebox

class Main:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Number Guessing")
        self.root.geometry("400x400")

        self.title = tk.Label(self.root, text="Number Guessing Game", font=("Arial", 18))
        self.title.pack(padx=10,pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Enter", command=self.play)
        self.button.pack(padx=10, pady=10)

        self.number = random.randint(1, 100)
        self.info = tk.Label(self.root, font=('Arial', 18))
        self.info.pack(padx=10,pady=10)

        self.guesses = 0

        

        self.root.mainloop()
    def play(self):
        try:
            self.guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning(message="Invalid input. Enter a whole no. in range of 1-100")

        if self.guess > self.number:
            messagebox.showinfo(message="Too High. Try entering a lower number")
            self.guesses += 1
        elif self.guess < self.number:
            messagebox.showinfo(message="Too Low. Try entering a Higher number")
            
            self.guesses += 1
        else:
            self.info.config(text=f'You Won. You took {self.guesses} attempts')
            



Main()