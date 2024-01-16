import tkinter as tk
from tkinter import *
 
root = tk.Tk()

root.minsize(600, 400)
root.maxsize(600, 400)
root.resizable(width=False, height=False)
root.configure(background='grey')
hello = Label(root, text="hello", font="comicsans 13 bold")
hello.pack()
root.mainloop()