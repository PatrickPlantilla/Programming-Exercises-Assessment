from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("String Counter")
root.geometry("200x200")

file_label = Label(root, text="No file selected")
file_label.pack()

letter_label = Label(root, text="Enter the letter to search:")
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
    search_term = string_entry.get()

    if search_term.isalpha() and len(search_term) == 1:
        count = 0
        try:
            with open(file, "r") as f:
                for line in f:
                    count += line.count(search_term)
            result_label.config(text=f"The letter '{search_term}' appears {count} times in the file.")
        except Exception as e:
            result_label.config(text=f"An error occurred: {e}")
    else:
        result_label.config(text="Please enter a single letter.")

open_button = Button(root, text="Open file", command=open_file)
open_button.pack()

count_button = Button(root, text="Times appeared", command=count_string)
count_button.pack()

root.mainloop()
