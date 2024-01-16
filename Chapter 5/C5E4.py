import tkinter as tk
from tkinter import ttk
import math

class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass  # To be implemented in subclasses

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = tk.DoubleVar()

    def inputSides(self):
        self.radius.set(float(entry_radius.get()))

    def area(self):
        return math.pi * self.radius.get() * self.radius.get()

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.length = tk.DoubleVar()
        self.width = tk.DoubleVar()

    def inputSides(self):
        self.length.set(float(entry_length.get()))
        self.width.set(float(entry_width.get()))

    def area(self):
        return self.length.get() * self.width.get()

class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.side1 = tk.DoubleVar()
        self.side2 = tk.DoubleVar()
        self.side3 = tk.DoubleVar()

    def inputSides(self):
        self.side1.set(float(entry_side1.get()))
        self.side2.set(float(entry_side2.get()))
        self.side3.set(float(entry_side3.get()))

    def area(self):
        s = (self.side1.get() + self.side2.get() + self.side3.get()) / 2
        return math.sqrt(s * (s - self.side1.get()) * (s - self.side2.get()) * (s - self.side3.get()))

def calculate_area(shape):
    shape.inputSides()
    area_value = shape.area()
    result_label.config(text=f"Area: {area_value}")

root = tk.Tk()
root.geometry("300x230")
root.title("Shape Area Calculator")

frame = tk.Frame(root, width="300", height="230")
frame.pack(side="top")

shape_label = tk.Label(frame, text="Shape Area Calculator", font=('Arial', 17), fg="black")
shape_label.grid(row=0, column=0, columnspan=5)

shape_var = tk.StringVar()
shape_var.set([])

shape_var_label = tk.Label(frame, text="Select shape", fg="black")
shape_var_label.grid(row=1, column=0)

shape_dropdown = ttk.Combobox(frame, textvariable=shape_var, values=["Circle", "Rectangle", "Triangle"])
shape_dropdown.grid(row=1, column=1, columnspan=4, pady=5)

entry_radius_label= tk.Label(frame, text="For Circle:", fg="black")
entry_radius_label.grid(row=2, column=0, sticky="e")
entry_radius = tk.Entry(frame, width=10)
entry_radius.grid(row=2, column=1, pady=5)

entry_rectangle_label= tk.Label(frame, text="For Rectangle:", fg="black")
entry_rectangle_label.grid(row=3, column=0, sticky="e")
entry_length = tk.Entry(frame, width=10)
entry_width = tk.Entry(frame, width=10)
entry_length.grid(row=3, column=1, pady=5)
entry_width.grid(row=3, column=2, pady=5)

entry_triangle_label= tk.Label(frame, text="For Triangle:", fg="black")
entry_triangle_label.grid(row=4, column=0, sticky="e")
entry_side1 = tk.Entry(frame, width=10)
entry_side2 = tk.Entry(frame, width=10)
entry_side3 = tk.Entry(frame, width=10)
entry_side1.grid(row=4, column=1, pady=5)
entry_side2.grid(row=4, column=2, pady=5)
entry_side3.grid(row=4, column=3, pady=5)

result_label = tk.Label(frame, text="Area: ", font=('Arial', 17), fg="black")
result_label.grid(row=5, column=0, columnspan=5, pady=5)

calculate_button = tk.Button(frame, text="Calculate Area", command=lambda: calculate_area(get_selected_shape()))
calculate_button.grid(row=6, column=0, columnspan=5, pady=10)

def get_selected_shape():
    selected_shape = shape_var.get()
    if selected_shape == "Circle":
        return Circle()
    elif selected_shape == "Rectangle":
        return Rectangle()
    elif selected_shape == "Triangle":
        return Triangle()

root.mainloop()
