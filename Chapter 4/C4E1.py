import tkinter as tk

root = tk.Tk()
root.title("Tkinter Text File Example")


with open("bio.txt", "r") as file:
    data = file.read()

label = tk.Label(root, text=data)
label.pack()

root.mainloop()
