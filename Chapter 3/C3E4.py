import tkinter as tk
from tkinter import ttk

def draw_shape(shape, coordinates):
    if shape == "Oval":
        canvas.create_oval(coordinates, outline="black", width=2)
    elif shape == "Rectangle":
        canvas.create_rectangle(coordinates, outline="black", width=2)
    elif shape == "Square":
        canvas.create_rectangle(coordinates, outline="black", width=2)
    elif shape == "Triangle":
        canvas.create_polygon(coordinates, outline="black", width=2)

def submit():
    selected_shape = shape_var.get()
    coordinates_str = coordinates_entry.get()
    coordinates = tuple(map(int, coordinates_str.split(',')))
    draw_shape(selected_shape, coordinates)



root = tk.Tk()
root.geometry("800x800")
root.title("Draw Shapes")



frame = tk.Frame(root, bg="#dddddd", height="200", width="600", highlightbackground="white", highlightthickness=1)
frame.pack(side="top", pady=10)



title_label = tk.Label(frame, text="Shape Drawer", font=('Arial', 17), fg="black", bg="#dddddd")
title_label.grid(row=0, column=0, columnspan=2)



shape_label = tk.Label(frame, text="Select Shape", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
shape_label.grid(row=1, column=0, pady=5, padx=5, sticky="e")

shapes = ["Oval", "Rectangle", "Square", "Triangle"]
shape_var = tk.StringVar()
shape_combobox = ttk.Combobox(frame, textvariable=shape_var, values=shapes, font=("calibre", 10, "bold"), width=18)
shape_combobox.grid(row=1, column=1, pady=5, padx=5, sticky="w")



coordinates_label = tk.Label(frame, text="Coordinates", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
coordinates_label.grid(row=2, column=0, pady=5, padx=5, sticky="e")

coordinates_entry = tk.Entry(frame, font=("calibre", 10, "bold"), fg="black", width=21)
coordinates_entry.grid(row=2, column=1, pady=5, padx=5, sticky="w")



submit_button = tk.Button(frame, text="Draw Shape", font=("Arial", 12), command=submit, bg="#000465", fg="white")
submit_button.grid(row=3, column=0, columnspan=2, pady=10)



canvas = tk.Canvas(root, bg="white", height=800, width=700)
canvas.pack()

# Main loop
root.mainloop()
