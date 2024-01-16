import math
#almost a copy of exercise 12

print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Quit")

def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("Sum =", result)

def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("Sum =", result)

def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("Sum =", result)

def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("💀💀💀 you can't divide by zero")
    else:
        result = num1 / num2
        print("Sum =", result)

def modulus():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("💀💀💀 you can't modulus by zero")
    else:
        result = num1 % num2
        print("Result: ", result)

while True:
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        add()
    elif choice == '2':
        subtract()
    elif choice == '3':
        multiply()
    elif choice == '4':
        divide()
    elif choice == '5':
        modulus()
    elif choice == '6':
        print("ok")
    break
