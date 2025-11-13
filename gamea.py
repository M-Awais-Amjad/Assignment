import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Number Guessing Game")
        self.master.geometry("400x350")
        self.master.resizable(False, False)
        self.master.configure(bg="#F0F4FF")  # soft blue background

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        # Title
        self.title_label = tk.Label(
            master,
            text="🎯 Guess the Number (1–100)",
            font=("Helvetica", 16, "bold"),
            bg="#F0F4FF",
            fg="#2B2D42"
        )
        self.title_label.pack(pady=15)

        # Entry field
        self.entry = tk.Entry(
            master,
            font=("Helvetica", 14),
            justify="center",
            bg="#FFFFFF",
            fg="#1C1C1C",
            bd=2,
            relief="solid",
            width=10
        )
        self.entry.pack(pady=10)

        # Guess button
        self.guess_button = tk.Button(
            master,
            text="Guess",
            font=("Helvetica", 12, "bold"),
            bg="#6A5ACD",  # slate blue
            fg="white",
            activebackground="#483D8B",
            activeforeground="white",
            width=12,
            command=self.check_guess
        )
        self.guess_button.pack(pady=8)

        # Feedback label
        self.feedback_label = tk.Label(
            master,
            text="",
            font=("Helvetica", 13),
            bg="#F0F4FF"
        )
        self.feedback_label.pack(pady=15)

        # Button frame (for reset + exit)
        button_frame = tk.Frame(master, bg="#F0F4FF")
        button_frame.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(
            button_frame,
            text="🔄 Reset Game",
            font=("Helvetica", 11, "bold"),
            bg="#00BFA6",   # teal green
            fg="white",
            activebackground="#009E89",
            activeforeground="white",
            width=12,
            command=self.reset_game
        )
        self.reset_button.grid(row=0, column=0, padx=10)

        # Exit button
        self.exit_button = tk.Button(
            button_frame,
            text="❌ Exit Game",
            font=("Helvetica", 11, "bold"),
            bg="#FF4B5C",   # soft red
            fg="white",
            activebackground="#E63946",
            activeforeground="white",
            width=12,
            command=self.exit_game
        )
        self.exit_button.grid(row=0, column=1, padx=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.feedback_label.config(text="📉 Too low! Try again.", fg="#0077B6")
            elif guess > self.secret_number:
                self.feedback_label.config(text="📈 Too high! Try again.", fg="#F3722C")
            else:
                messagebox.showinfo("🎉 You Win!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="⚠️ Please enter a valid number!", fg="#D62828")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.entry.focus()

    def exit_game(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
