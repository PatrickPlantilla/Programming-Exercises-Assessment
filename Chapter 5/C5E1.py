import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("250x130")
root.title("Dog Information System")

frame = tk.Frame(root, width="250", height="130")
frame.pack(side="top")

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def woof(self):
        return f"{self.name} says Woof!"

Dog1 = Dog("Hachiko", 11, "Akita Inu")
Dog2 = Dog("Blondi", 4, "German Shepherd")

Dog_info_label = tk.Label(frame, text="Dog Information", font=('Arial', 17), fg="black")
Dog_info_label.grid(row=0, column=0, columnspan=2)

Dog1_info_label = tk.Label(frame, text=f"{Dog1.name} - Age: {Dog1.age}, Breed: {Dog1.breed}", fg="black")
Dog1_info_label.grid(row=1, column=0)

Dog2_info_label = tk.Label(frame, text=f"{Dog2.name} - Age: {Dog2.age}, Breed: {Dog2.breed}", fg="black")
Dog2_info_label.grid(row=2, column=0)

def make_Dog_woof():
    oldest_Dog = max([Dog1, Dog2], key=lambda x: x.age)
    woof_label = tk.Label(frame, text=oldest_Dog.woof())
    woof_label.grid(row=3, column=0, columnspan=2)

woof_button = tk.Button(frame, text="Make Oldest Dog Woof", command=make_Dog_woof)
woof_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
