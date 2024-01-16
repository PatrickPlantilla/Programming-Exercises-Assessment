from tkinter import *
root = Tk()
root.configure(bg="LightGray")

root.minsize(150, 75)
root.maxsize(400, 200)

l=Label(root, bg="Red", padx=30, pady=2, relief=SUNKEN, text="A")
l.pack(side=TOP, fill=X, expand=TRUE)

l=Label(root, bg="Yellow", padx=30, pady=2, relief=SUNKEN, text="B")
l.pack(side=BOTTOM, fill=NONE)

l=Label(root, bg="Blue", padx=30, pady=2, text="C")
l.pack(side=LEFT, expand=TRUE)

l=Label(root, bg="White", padx=30, pady=2, text="D")
l.pack(fill=NONE)

root.mainloop()