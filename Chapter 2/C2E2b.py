import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.configure(background="white")

left_frame = tk.Frame(root, borderwidth=1, relief="solid", highlightbackground="white", highlightthickness=1)
left_frame.pack(side="left", expand=True, fill="both")

label_a = tk.Label(left_frame, text="A", bg="#22263d", fg="white")
label_a.pack(side="top", expand=True, fill="both")

label_b = tk.Label(left_frame, text="B", bg="white")
label_b.pack(side="bottom", expand=True, fill="both")



right_frame = tk.Frame(root, borderwidth=1, relief="solid", highlightbackground="white", highlightthickness=1)
right_frame.pack(side="right", expand=True, fill="both")

label_c = tk.Label(right_frame, text="C", bg="white")
label_c.pack(side="top", expand=True, fill="both")

label_d = tk.Label(right_frame, text="D", bg="#22263d", fg="white")
label_d.pack(side="bottom", expand=True, fill="both")

root.mainloop()
