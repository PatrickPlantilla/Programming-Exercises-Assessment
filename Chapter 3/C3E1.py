import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")
root.title("Greeting App")
root.configure(pady=10, padx=40)

# InputFrame
input_frame = tk.Frame(root, bg="blue", height="200", width="300", highlightbackground="white", highlightthickness=1)
input_frame.pack(side="top")

title_label = tk.Label(input_frame, text="Greeting App", font=('Arial', 16, 'bold'), fg="black", bg="blue")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

name_var = tk.StringVar()
name_label = tk.Label(input_frame, text="Name:", font=("calibre", 10, "bold"), fg="black", bg="blue")
name_label.grid(row=1, column=0, pady=5, padx=5, sticky="e")
name_entry = tk.Entry(input_frame, textvariable=name_var, font=("calibre", 10, "bold"), fg="black", bg="grey", width=21)
name_entry.grid(row=1, column=1, pady=5, padx=5, sticky="w")

color_options = ["blue", "green", "red"]
color_var = tk.StringVar(value=color_options[0])
color_label = tk.Label(input_frame, text="Select Color:", font=("calibre", 10, "bold"), fg="black", bg="blue")
color_label.grid(row=2, column=0, pady=5, padx=5, sticky="e")
color_dropdown = ttk.Combobox(input_frame, textvariable=color_var, values=color_options, font=("calibre", 10, "bold"), width=18)
color_dropdown.grid(row=2, column=1, pady=5, padx=5, sticky="w")

def update_greeting():
    greeting = f"Hello, {name_var.get()}!"
    greeting_label.config(text=greeting, bg=color_var.get(), fg="orange")

update_button = tk.Button(input_frame, text="Update Greeting", command=update_greeting, font=("Arial", 12), bg="lightgreen")
update_button.grid(row=3, column=0, columnspan=2, pady=10)

# DisplayFrame
display_frame = tk.Frame(root, bg="blue", height="150", width="300", highlightbackground="white", highlightthickness=1)
display_frame.pack(side="top")

greeting_label = tk.Label(display_frame, text="", font=("calibre", 14))
greeting_label.pack()

root.mainloop()
