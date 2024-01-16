import tkinter as tk
from tkinter import ttk

#I do not have access to the top image so i cannot fully replicate the GUI
root = tk.Tk()
root.geometry("400x800")
root.title("Student Management System")
root.configure(pady=10, padx=40)

root = tk.Root(root, bg="#dddddd", height="350", width="750", highlightbackground="white", highlightthickness=1)
root.pack(side="top")

student_name_var = tk.StringVar()
mobile_number_var = tk.StringVar()
email_id_var = tk.StringVar()
home_address_var = tk.StringVar()



SMS_label = tk.Label(root, text="Student Management System", font=('Arial', 17), fg="black", bg="#dddddd")
SMS_label.grid(row=0, column=0, columnspan=2)

NSR_label = tk.Label(root, text="New Student Registration", font=('Arial', 14), fg="black", bg="#dddddd")
NSR_label.grid(row=1, column=0, columnspan=2)



student_name_label = tk.Label(root, text="Student Name", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
student_name_label.grid(row=2, column=0, padx=5, sticky="e")

student_name_entry = tk.Entry(root, textvariable=student_name_var, font=("calibre", 10, "bold"), fg="black", bg="grey", width=21)
student_name_entry.grid(row=2, column=1, padx=5, sticky="w")



mobile_number_label = tk.Label(root, text="Mobile Number", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
mobile_number_label.grid(row=3, column=0, padx=5, sticky="e")

mobile_number_entry = tk.Entry(root, textvariable=mobile_number_var, font=("calibre", 10, "bold"), fg="black", bg="grey", width=21)
mobile_number_entry.grid(row=3, column=1, padx=5, sticky="w")



email_id_label = tk.Label(root, text="Email Id", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
email_id_label.grid(row=4, column=0, padx=5, sticky="e")

email_id_entry = tk.Entry(root, textvariable=email_id_var, font=("calibre", 10, "bold"), fg="black", bg="grey", width=21)
email_id_entry.grid(row=4, column=1, padx=5, sticky="w")



home_address_label = tk.Label(root, text="Home Address", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
home_address_label.grid(row=5, column=0, padx=5, sticky="e")

home_address_entry = tk.Entry(root, textvariable=home_address_var, font=("calibre", 10, "bold"), fg="black", bg="grey", width=21)
home_address_entry.grid(row=5, column=1, padx=5, sticky="w")



gender_label = tk.Label(root, text="Gender", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
gender_label.grid(row=6, column=0, padx=5, sticky="e")

gender_options = ["Male", "Female"]
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=gender_options, font=("calibre", 10, "bold"), width=18)
gender_combobox.grid(row=6, column=1, padx=5, sticky="w")



v = tk.StringVar(value="")

gender_label = tk.Label(root, text="Course Enrolled", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
gender_label.grid(row=7, column=0, padx=5, sticky="e")

Cc = tk.Radiobutton(root, text="BSc CC", variable=v, value="BSc CC", bg="#dddddd")
Cc.grid(row=7, column=1, padx=5, sticky="w")

Cy = tk.Radiobutton(root, text="BSc CY", variable=v, value="BSc CY", bg="#dddddd")
Cy.grid(row=8, column=1, padx=5, sticky="w")

Psy = tk.Radiobutton(root, text="BSc PSY", variable=v, value="BSc PSY", bg="#dddddd")
Psy.grid(row=9, column=1, padx=5, sticky="w")

Bm = tk.Radiobutton(root, text="BSc BM", variable=v, value="BSc BM", bg="#dddddd")
Bm.grid(row=10, column=1, padx=5, sticky="w")



Languages_label = tk.Label(root, text="Course", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
Languages_label.grid(row=11, column=0, padx=5, sticky="e")

English= tk.Checkbutton(root, text="Engish", bg="#dddddd")
English.grid(row=11, column=1, padx=5, sticky="w")

Tagalog= tk.Checkbutton(root, text="Tagalog", bg="#dddddd")
Tagalog.grid(row=11, column=1, padx=5, sticky="e")

HindiUrdu= tk.Checkbutton(root, text="Hindi/Urdu", bg="#dddddd")
HindiUrdu.grid(row=12, column=1, padx=5, sticky="w")



Rate_Skills= tk.Label(root, text="Rate your English communication skills", font=("calibre", 10, "bold"), fg="black", bg="#dddddd")
Rate_Skills.grid(row=13, column=0, columnspan=2)

s = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, length=200, resolution=0.01, fg="black", bg="#dddddd")
s.grid(row=14, column=0, columnspan=2)



def print():
    print("Ok")
button1 = tk.Button(root, text="Submit", font=("Arial", 12), command=print, bg="#000465", fg="white")
button1.grid(row=15, column=0, padx=5, sticky="w")

def clear():
    student_name_var.set("")
    mobile_number_var.set("")
    email_id_var.set("")
    home_address_var.set("")
    v.set("")
    English.deselect()
    Tagalog.deselect()
    HindiUrdu.deselect()
    s.set(0)
button2 = tk.Button(root, text="Clear", font=("Arial", 12), command=clear, bg="#000465", fg="white")
button2.grid(row=15, column=1, padx=5, sticky="e")
root.mainloop()
