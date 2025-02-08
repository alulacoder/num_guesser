import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a new random number
def generate_new_number():
    return random.randint(0, 30)

# Initial random number
number_to_guess = generate_new_number()

# Function to check the user's guess
def check_guess():
    try:
        user_guess = int(entry_guess.get())
        
        if user_guess < 0 or user_guess > 30:
            messagebox.showwarning("Out of Range", "Please guess a number between 0 and 30.")
        elif user_guess < number_to_guess:
            feedback_label.config(text="Too low! Try again.", fg="blue")
        elif user_guess > number_to_guess:
            feedback_label.config(text="Too high! Try again.", fg="red")
        else:
            feedback_label.config(text="🎯 You guessed the correct number!", fg="green")
            messagebox.showinfo("Congratulations!", "🎉 You guessed the number correctly!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Function to provide a hint
def give_hint():
    if number_to_guess % 2 == 0:
        hint = "Hint: The number is EVEN."
    else:
        hint = "Hint: The number is ODD."
    hint_label.config(text=hint, fg="green")

# Function to reset the game
def reset_game():
    global number_to_guess
    number_to_guess = generate_new_number()  # Generate new number
    entry_guess.delete(0, tk.END)            # Clear the guess entry
    feedback_label.config(text="")           # Clear feedback
    hint_label.config(text="")               # Clear hint
    messagebox.showinfo("Game Reset", "🔄 The game has been reset!\nTry to guess the new number.")
    # To save an image
    

# Setting up the window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x300")

# Adding widgets
instructions = tk.Label(root, text="Guess the number (0 to 30):", font=("Arial", 12))
instructions.pack(pady=10)

entry_guess = tk.Entry(root, font=("Arial", 12), justify="center")
entry_guess.pack(pady=5)

# Buttons frame to organize "Check Guess," "Hint," and "Reset" buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

check_button = tk.Button(button_frame, text="Check Guess", command=check_guess, font=("Arial", 12))
check_button.pack(side="left", padx=5)

hint_button = tk.Button(button_frame, text="ℹ️ Hint", command=give_hint, font=("Arial", 12), bg="lightblue")
hint_button.pack(side="left", padx=5)


reset_button = tk.Button(button_frame, text="🔄 Reset", command=reset_game, font=("Arial", 12), bg="orange")
reset_button.pack(side="left", padx=5)

feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

hint_label = tk.Label(root, text="", font=("Arial", 11, "italic"))
hint_label.pack()

# Run the app
root.mainloop()
