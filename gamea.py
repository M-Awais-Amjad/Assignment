# import random

# def number_guessing_game():
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
    
#     # Generate a random number between 1 and 100
#     secret_number = random.randint(1, 100)
#     attempts = 0
    
#     while True:
#         try:
#             guess = int(input("Enter your guess: "))
#             attempts += 1

#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Please enter a valid number.")

# if __name__ == "__main__":
#     number_guessing_game()




import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("350x250")
        self.master.resizable(False, False)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Title
        self.title_label = tk.Label(master, text="🎯 Guess the Number (1–100)", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=10)

        # Entry field
        self.entry = tk.Entry(master, font=("Arial", 12), justify="center")
        self.entry.pack(pady=5)

        # Guess button
        self.guess_button = tk.Button(master, text="Guess", font=("Arial", 12), command=self.check_guess)
        self.guess_button.pack(pady=10)

        # Feedback label
        self.feedback_label = tk.Label(master, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(master, text="Reset Game", font=("Arial", 10), command=self.reset_game)
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try again.", fg="blue")
            elif guess > self.secret_number:
                self.feedback_label.config(text="Too high! Try again.", fg="orange")
            else:
                messagebox.showinfo("🎉 You Win!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="red")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
