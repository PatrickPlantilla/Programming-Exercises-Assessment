from tkinter import *

root = Tk()
root.geometry("190x70")
root.title("Login")

def getval():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")


user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid(row=1, column=2)
password.grid(row=2, column=2)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=1, column=3)
passentry.grid(row=2, column=3)

ok = print("Ok")
submit = Button(text="Submit", command=getval)
submit.grid(row=3, column=3)

root.mainloop()