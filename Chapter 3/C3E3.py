import tkinter as tk
from tkinter import ttk

class AreaCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x200")
        self.master.title("Area Calculator")

        self.create_tabs()

    def create_tabs(self):
        tab_control = ttk.Notebook(self.master)

        circle_tab = ttk.Frame(tab_control)
        square_tab = ttk.Frame(tab_control)
        rectangle_tab = ttk.Frame(tab_control)

        self.create_circle_tab(circle_tab)
        self.create_square_tab(square_tab)
        self.create_rectangle_tab(rectangle_tab)

        tab_control.add(circle_tab, text='Circle')
        tab_control.add(square_tab, text='Square')
        tab_control.add(rectangle_tab, text='Rectangle')

        tab_control.pack(expand=1, fill='both')

    def create_circle_tab(self, circle_tab):
        radius_label = tk.Label(circle_tab, text="Enter Radius:")
        radius_label.grid(row=0, column=0, padx=10, pady=10)

        radius_entry = tk.Entry(circle_tab)
        radius_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(circle_tab, text="Calculate Area", command=lambda: self.calculate_circle_area(radius_entry, result_label))
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        result_label = tk.Label(circle_tab, text="")
        result_label.grid(row=2, column=0, columnspan=2)

    def calculate_circle_area(self, radius_entry, result_label):
        try:
            radius = float(radius_entry.get())
            area = 3.14 * radius * radius
            result_label.config(text=f"Area: {area}")
        except ValueError:
            result_label.config(text="Invalid Input")

    def create_square_tab(self, square_tab):
        side_label = tk.Label(square_tab, text="Enter Side Length:")
        side_label.grid(row=0, column=0, padx=10, pady=10)

        side_entry = tk.Entry(square_tab)
        side_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(square_tab, text="Calculate Area", command=lambda: self.calculate_square_area(side_entry, result_label))
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        result_label = tk.Label(square_tab, text="")
        result_label.grid(row=2, column=0, columnspan=2)

    def calculate_square_area(self, side_entry, result_label):
        try:
            side = float(side_entry.get())
            area = side * side
            result_label.config(text=f"Area: {area}")
        except ValueError:
            result_label.config(text="Invalid Input")

    def create_rectangle_tab(self, rectangle_tab):
        length_label = tk.Label(rectangle_tab, text="Enter Length:")
        length_label.grid(row=0, column=0, padx=10, pady=10)

        length_entry = tk.Entry(rectangle_tab)
        length_entry.grid(row=0, column=1, padx=10, pady=10)

        width_label = tk.Label(rectangle_tab, text="Enter Width:")
        width_label.grid(row=1, column=0, padx=10, pady=10)

        width_entry = tk.Entry(rectangle_tab)
        width_entry.grid(row=1, column=1, padx=10, pady=10)

        calculate_button = tk.Button(rectangle_tab, text="Calculate Area", command=lambda: self.calculate_rectangle_area(length_entry, width_entry, result_label))
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        result_label = tk.Label(rectangle_tab, text="")
        result_label.grid(row=3, column=0, columnspan=2)

    def calculate_rectangle_area(self, length_entry, width_entry, result_label):
        try:
            length = float(length_entry.get())
            width = float(width_entry.get())
            area = length * width
            result_label.config(text=f"Area: {area}")
        except ValueError:
            result_label.config(text="Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()
