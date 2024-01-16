import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import the Image and ImageTk modules

class CoffeeVendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x500")
        self.root.title("Coffee Vending Machine")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Coffee Vending Machine", font=('Arial', 16))
        title_label.pack(pady=10)

        coffee_label = tk.Label(self.root, text="Select Coffee Type:")
        coffee_label.pack()

        coffees = ["Espresso", "Latte", "Cappuccino", "Cat Poop Coffee"]
        self.coffee_var = tk.StringVar()
        coffee_combobox = tk.OptionMenu(self.root, self.coffee_var, *coffees)
        coffee_combobox.pack()

        options_label = tk.Label(self.root, text="Select Options:")
        options_label.pack()

        self.sugar_var = tk.IntVar()
        sugar_checkbox = tk.Checkbutton(self.root, text="Sugar", variable=self.sugar_var)
        sugar_checkbox.pack()

        self.milk_var = tk.IntVar()
        milk_checkbox = tk.Checkbutton(self.root, text="Milk", variable=self.milk_var)
        milk_checkbox.pack()

        self.stevia_var = tk.IntVar()
        stevia_checkbox = tk.Checkbutton(self.root, text="Stevia", variable=self.stevia_var)
        stevia_checkbox.pack()

        # Create Label for displaying coffee images
        self.coffee_image_label = tk.Label(self.root)
        self.coffee_image_label.pack()

        submit_button = tk.Button(self.root, text="Submit", command=self.display_message)
        submit_button.pack(pady=20)

    def display_message(self):
        coffee_type = self.coffee_var.get()
        options = []

        if self.sugar_var.get():
            options.append("Sugar")

        if self.milk_var.get():
            options.append("Milk")

        if self.stevia_var.get():
            options.append("Stevia")

        message = f"Selected Coffee: {coffee_type}\nOptions: {', '.join(options)}"

        messagebox.showinfo("Order Confirmation", message)

        
        if coffee_type == "Espresso":
            img = ImageTk.PhotoImage(Image.open("espresso_image.jpg"))
            self.coffee_image_label.configure(image=img)
            self.coffee_image_label.image = img
        elif coffee_type == "Latte":
            img = ImageTk.PhotoImage(Image.open("latte_image.jpg"))
            self.coffee_image_label.configure(image=img)
            self.coffee_image_label.image = img
        elif coffee_type == "Cappuccino":
            img = ImageTk.PhotoImage(Image.open("cappuccino_image.jpg"))
            self.coffee_image_label.configure(image=img)
            self.coffee_image_label.image = img
        elif coffee_type == "Cat Poop Coffee":
            img = ImageTk.PhotoImage(Image.open("poop_image.jpg"))
            self.coffee_image_label.configure(image=img)
            self.coffee_image_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    vm = CoffeeVendingMachine(root)
    root.mainloop()
