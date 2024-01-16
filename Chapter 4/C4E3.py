import tkinter as tk

root = tk.Tk()
root.title("Tkinter Text File Example")

with open("numbers.txt", "r") as file:
    data = file.read().splitlines()

numbers = [int(number) for number in data]

label_text = ", ".join(map(str, numbers))
label = tk.Label(root, text=label_text)
label.pack()

root.mainloop()