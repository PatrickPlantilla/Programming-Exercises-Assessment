import tkinter as tk
from tkinter import ttk

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def display(self):
        average = self.calcGrade()
        return f"{self.name} - Average Grade: {average:.2f}"

root = tk.Tk()
root.geometry("250x165")
root.title("Student Grade Calculator")

frame = tk.Frame(root, width="250", height="165")
frame.pack(side="top")

student_info_label = tk.Label(frame, text="Student Information", font=('Arial', 17), fg="black")
student_info_label.grid(row=0, column=0, columnspan=2)



name_entry_label = tk.Label(frame, text="Name:")
name_entry_label.grid(row=1, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=1)

mark1_entry_label = tk.Label(frame, text="Mark 1:")
mark1_entry_label.grid(row=2, column=0)
mark1_entry = tk.Entry(frame)
mark1_entry.grid(row=2, column=1)

mark2_entry_label = tk.Label(frame, text="Mark 2:")
mark2_entry_label.grid(row=3, column=0)
mark2_entry = tk.Entry(frame)
mark2_entry.grid(row=3, column=1)

mark3_entry_label = tk.Label(frame, text="Mark 3:")
mark3_entry_label.grid(row=4, column=0)
mark3_entry = tk.Entry(frame)
mark3_entry.grid(row=4, column=1)



def create_student():
    student = Student(name_entry.get(), int(mark1_entry.get()), int(mark2_entry.get()), int(mark3_entry.get()))
    result_label.config(text=student.display())

create_button = tk.Button(frame, text="Create Student", command=create_student)
create_button.grid(row=5, column=0, columnspan=2)

result_label = tk.Label(frame, text="", fg="black")
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
