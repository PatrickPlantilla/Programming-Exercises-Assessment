import tkinter as tk

class Animal:
    def __init__(self, animal_type, name, colour, age, weight, noise):
        self.animal_type = animal_type
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    def sayHello(self):
        return f"{self.name} says Hello!"

    def makeNoise(self):
        return f"{self.name} makes a {self.noise} noise!"

    def animalDetails(self):
        details = f"Type: {self.animal_type}, Name: {self.name}, Colour: {self.colour}, Age: {self.age}, Weight: {self.weight}, Noise: {self.noise}"
        return details

def display_animal_info(animal):
    animal_info_label.config(text=animal.animalDetails())

def make_animal_noise(animal):
    noise_label.config(text=animal.makeNoise())



Dog = Animal("Dog", "Hachiko", "Golden Brown", 11, 33, "ARF!!")
Stegosaurus = Animal("Stegosaurus", "Sophie", "Green", 34, 2710, "*Stegosaurus noise")

# Create Tkinter GUI
root = tk.Tk()
root.geometry("800x200")
root.title("Animal Information System")

frame = tk.Frame(root, width="800", height="200")
frame.pack(side="top")

# Display details of the Dog
Dog_info_label = tk.Label(frame, text="Dog Information", font=('Arial', 14), fg="black")
Dog_info_label.grid(row=0, column=0, columnspan=2)

Dog_details_label = tk.Label(frame, text="")
Dog_details_label.grid(row=1, column=0, columnspan=2)

Dog_hello_button = tk.Button(frame, text="Say Hello", command=lambda: display_animal_info(Dog))
Dog_hello_button.grid(row=2, column=0)

Dog_noise_button = tk.Button(frame, text="Make Noise", command=lambda: make_animal_noise(Dog))
Dog_noise_button.grid(row=2, column=1)

# Display details of the Stegosaurus
Stegosaurus_info_label = tk.Label(frame, text="Stegosaurus Information", font=('Arial', 14), fg="black")
Stegosaurus_info_label.grid(row=3, column=0, columnspan=2)

Stegosaurus_details_label = tk.Label(frame, text="")
Stegosaurus_details_label.grid(row=4, column=0, columnspan=2)

Stegosaurus_hello_button = tk.Button(frame, text="Say Hello", command=lambda: display_animal_info(Stegosaurus))
Stegosaurus_hello_button.grid(row=5, column=0)

Stegosaurus_noise_button = tk.Button(frame, text="Make Noise", command=lambda: make_animal_noise(Stegosaurus))
Stegosaurus_noise_button.grid(row=5, column=1)



animal_info_label = tk.Label(frame, text="", font=('Arial', 12), fg="black")
animal_info_label.grid(row=6, column=0, columnspan=2)



noise_label = tk.Label(frame, text="", font=('Arial', 12), fg="black")
noise_label.grid(row=7, column=0, columnspan=2)

root.mainloop()
