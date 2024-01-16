# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2

def modulus(num1, num2):
    return num1 % num2

# Function to find the greater number
def greater_number(num1, num2):
    return max(num1, num2)

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n" \
        "5. Modulus\n" \
        "6. Find Greater Number\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4, 5, 6:"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
elif select == 5:
    print(number_1, "%", number_2, "=", 
		            modulus(number_1, number_2))
elif select == 6:
    print("Greater number between", number_1, "and", number_2, "is:",  
		            greater_number(number_1, number_2))
else:
	print("Invalid input")
