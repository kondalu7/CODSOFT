import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import string
import random

# Function to generate password
def generate_password():
    length = length_var.get()
    if not length.isdigit():
        messagebox.showwarning("Invalid input", "Please enter a valid number for the password length.")
        return

    length = int(length)
    if length <= 4:
        messagebox.showwarning("Invalid input", "Password length must be greater than 4.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Custom fonts
title_font = Font(family="Helvetica", size=24, weight="bold")
label_font = Font(family="Helvetica", size=14)
entry_font = Font(family="Helvetica", size=12)
button_font = Font(family="Helvetica", size=16, weight="bold")
password_font = Font(family="Helvetica", size=14)

# Title
title_label = tk.Label(root, text="Password Generator", font=title_font, bg="#f0f0f0")
title_label.pack(pady=20)

# Password length input
length_label = tk.Label(root, text="Enter password length:", font=label_font, bg="#f0f0f0")
length_label.pack(pady=5)

length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, font=entry_font, bd=5, relief=tk.FLAT, justify="center")
length_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate", command=generate_password, font=button_font, bg="#4CAF50", fg="white", bd=5, relief=tk.RAISED)
generate_button.pack(pady=20)

# Display generated password
password_label = tk.Label(root, text="Generated Password:", font=label_font, bg="#f0f0f0")
password_label.pack(pady=5)

password_var = tk.StringVar()
password_display = tk.Entry(root, textvariable=password_var, font=password_font, bd=5, relief=tk.FLAT, justify="center", state="readonly")
password_display.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
