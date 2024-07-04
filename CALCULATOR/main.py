import tkinter as tk
from tkinter.font import Font

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("")

# Function to calculate the result
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to handle button click
def on_button_click(value):
    if value == "=":
        calculate()
    elif value == "C":
        clear_display()
    else:
        update_display(value)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

# Custom fonts
display_font = Font(family="Helvetica", size=24)
button_font = Font(family="Helvetica", size=18, weight="bold")

# Display variable
display_var = tk.StringVar()

# Create display
display = tk.Entry(root, textvariable=display_var, font=display_font, bd=10, relief=tk.FLAT, bg="#333", fg="#fff", justify="right")
display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(fill="both", expand=True)

# Button configuration
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons
for i, button in enumerate(buttons):
    action = lambda x=button: on_button_click(x)
    b = tk.Button(button_frame, text=button, font=button_font, command=action, bg="#eee", fg="#333", bd=2, relief=tk.RAISED)
    b.grid(row=i//4, column=i%4, sticky="nsew", padx=5, pady=5)
    b.bind("<Enter>", lambda e, btn=b: btn.configure(bg="#ddd"))
    b.bind("<Leave>", lambda e, btn=b: btn.configure(bg="#eee"))

# Configure grid layout
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

# Run the Tkinter event loop
root.mainloop()
