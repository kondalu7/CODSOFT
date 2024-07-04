import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def toggle_task():
    try:
        index = listbox.curselection()
        task_text = listbox.get(index)
        if task_text.startswith("✓ "):
            task_text = task_text[2:]
        else:
            task_text = "✓ " + task_text
        listbox.delete(index)
        listbox.insert(index, task_text)
    except:
        messagebox.showwarning("Warning", "Please select the task you've done.")


window = tk.Tk()
window.title("To-Do List")
window.configure(bg="light gray")

# Custom fonts
title_font = Font(family="Helvetica", size=18, weight="bold")
button_font = Font(family="Helvetica", size=12, weight="bold")
entry_font = Font(family="Helvetica", size=12)
listbox_font = Font(family="Helvetica", size=12)

# Create title label
title_label = tk.Label(window, text="My To-Do List", font=title_font, bg="light gray", fg="black")
title_label.pack(pady=10)

# Create an entry widget to add tasks
entry = tk.Entry(window, width=50, font=entry_font, bd=2, relief=tk.SOLID)
entry.pack(padx=20, pady=10, ipady=5)

# Create a frame to hold the buttons
button_frame = tk.Frame(window, bg="light gray")
button_frame.pack(pady=10)

# Create buttons
add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=button_font, bg="white", fg="green", relief=tk.FLAT)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=button_font, bg="white", fg="red", relief=tk.FLAT)
delete_button.pack(side=tk.LEFT, padx=5)

toggle_button = tk.Button(button_frame, text="Done Task", command=toggle_task, font=button_font, bg="white", fg="blue", relief=tk.FLAT)
toggle_button.pack(side=tk.LEFT, padx=5)

# Create a listbox to display tasks
listbox = tk.Listbox(window, width=50, height=15, font=listbox_font, bd=2, relief=tk.SOLID, selectbackground="white", selectforeground="black")
listbox.pack(padx=20, pady=10)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Start the Tkinter event loop
window.mainloop()
