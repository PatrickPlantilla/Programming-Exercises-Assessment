import tkinter as tk
from tkinter import ttk

class Employee:
    def __init__(self, name, age, emp_id, salary):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.salary = salary

    def setData(self, name, age, emp_id, salary):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.salary = salary

    def getData(self):
        return f"{self.name}\t\t{self.age}\t\t{self.salary}\t{self.emp_id}"

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x600")
        self.root.title("Employee Information")

        self.frame = tk.Frame(root)
        self.frame.pack(side="top", pady=10)

        self.employee_list = []

        self.employee_info_label = tk.Label(self.frame, text="Employee Information", font=('Arial', 17), fg="black")
        self.employee_info_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Name:").grid(row=1, column=0, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.frame, text="Age:").grid(row=2, column=0, pady=5)
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.grid(row=2, column=1, pady=5)

        tk.Label(self.frame, text="Employee ID:").grid(row=3, column=0, pady=5)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=3, column=1, pady=5)

        tk.Label(self.frame, text="Salary:").grid(row=4, column=0, pady=5)
        self.salary_entry = tk.Entry(self.frame)
        self.salary_entry.grid(row=4, column=1, pady=5)

        tk.Button(self.frame, text="Add Employee", command=self.add_employee).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.frame, text="Display Employees", command=self.display_employees).grid(row=6, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.frame, text="", fg="black")
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        emp_id = int(self.id_entry.get())
        salary = float(self.salary_entry.get())

        employee = Employee(name, age, emp_id, salary)
        self.employee_list.append(employee)
        self.clear_entries()
        self.result_label.config(text="Employee added successfully!")

    def display_employees(self):
        if not self.employee_list:
            self.result_label.config(text="No employees to display.")
        else:
            header = "{:<15}{:<10}{:<15}{:<5}\n".format("Name", "Age", "Salary", "ID")
            data = "\n".join(["{:<15}{:<10}{:<15}{:<5}".format(employee.name, employee.age, employee.salary, employee.emp_id) for employee in self.employee_list])
            self.result_label.config(text=header + data)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()
