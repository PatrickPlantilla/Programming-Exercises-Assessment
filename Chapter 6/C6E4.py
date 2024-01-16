import tkinter as tk

root = tk.Tk()
root.title('Draw Lines')
root.geometry("300x100")

canvas = tk.Canvas(root, width=100, height=120, bg='white')
canvas.pack()

canvas.create_line(10, 20, 60, 80, fill='blue', width=2, tags='solid_line')
canvas.create_line(10, 30, 20, 80, fill='red', dash=(2, 2), width=2, tags='dotted_line')
canvas.create_line(20, 80, 60, 10, fill='red', dash=(2, 2), width=2, tags='dotted_line')
canvas.create_line(60, 10, 80, 100, fill='red', dash=(2, 2), width=2, tags='dotted_line')


root.mainloop()
