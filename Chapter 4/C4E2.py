from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("String Counter")
root.geometry("400x200")

file_label = Label(root, text="No file selected")
file_label.pack()

letter_label = Label(root, text="Enter the string to search:")
letter_label.pack()

string_entry = Entry(root)
string_entry.pack()

result_label = Label(root, text="")
result_label.pack()

def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_label.config(text=file)

def count_string():
    file = file_label.cget("text")
    string = string_entry.get()
    count = 0
    try:
        with open(file, "r") as f:
            for line in f:
                count += line.count(string)
        result_label.config(text=f"The string '{string}' appears {count} times in the file.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

open_button = Button(root, text="Open file", command=open_file)
open_button.pack()

count_button = Button(root, text="Count string", command=count_string)
count_button.pack()

root.mainloop()
