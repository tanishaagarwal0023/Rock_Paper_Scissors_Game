# import  Libraries

import tkinter as tk                # Used for creating GUIs
from tkinter import messagebox      # Used to show popup messages (like displaying results).
import random                       # Used to generate random values
from PIL import Image, ImageTk      # Used for handling background images

# Create a function to determine the winner

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You Win!"
    else:
        return "You Lose!"
    
# Function to get the computer's choice

def computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

# Function to handle the button click event
def play_game(user_choice):
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {comp_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("800x600")  # Set window size

# Open the background image

background_image = Image.open("background.jpg")  # Replace with the path to your background image
bg_photo = ImageTk.PhotoImage(background_image)

# Create a label widget to hold the background image

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Make the image cover the entire window

# Create frame to hold the buttons and center them

button_frame = tk.Frame(root, bg="#FFFFF0", width=400, height=300)
button_frame.pack_propagate(False)  # Prevent the frame from resizing based on its children
button_frame.pack(expand=True)


# Create buttons for user choice with specified colors

rock_button = tk.Button(button_frame, text="Rock", width=20, bg="sky blue", command=lambda: play_game('Rock'))
rock_button.grid(row=0, column=0, padx=50, pady=30)

paper_button = tk.Button(button_frame, text="Paper", width=20, bg="light yellow", command=lambda: play_game('Paper'))
paper_button.grid(row=1, column=0, padx=50, pady=30)

scissors_button = tk.Button(button_frame, text="Scissors", width=20, bg="light pink", command=lambda: play_game('Scissors'))
scissors_button.grid(row=2, column=0, padx=50, pady=30)

# Start the GUI loop or run the applications
root.mainloop()