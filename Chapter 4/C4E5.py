import tkinter as tk
from tkinter import messagebox

def validate_password():
    password = password_var.get()
    attempts_left = int(attempts_label.cget("text"))

    if (
        any(char.islower() for char in password)
        and any(char.isdigit() for char in password)
        and any(char.isupper() for char in password)
        and any(char in "$#@ " for char in password)
        and 6 <= len(password) <= 12
    ):
        messagebox.showinfo("Password Valid", "Password is valid!")
        root.destroy()
    else:
        if attempts_left == 1:
            messagebox.showerror("Alert", "Authorities have been alerted!")
            root.destroy()
        else:
            attempts_left -= 1
            attempts_label.config(text=str(attempts_left))
            messagebox.showwarning("Password Invalid", f"Invalid password. Attempts left: {attempts_left}")

root = tk.Tk()
root.geometry("200x200")
root.title("Student Management System")
root.configure()

password_var = tk.StringVar()
password_label = tk.Label(root, text="Password")
password_label.grid(row=16, column=0, pady=5, padx=5, sticky="e")

password_entry = tk.Entry(root, show="*", textvariable=password_var)
password_entry.grid(row=16, column=1, pady=5, padx=5, sticky="w")

attempts_label = tk.Label(root, text="5")
attempts_label.grid(row=17, column=0, pady=5, padx=5, sticky="e")

validate_button = tk.Button(root, text="Validate Password", command=validate_password)
validate_button.grid(row=17, column=1, pady=5, padx=5, sticky="w")

root.mainloop()
