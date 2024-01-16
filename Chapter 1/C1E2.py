import math
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

sum = number_1+number_2
diff = number_1-number_2
product = number_1*number_2
quotient = number_1/number_2
remainder = number_1%number_2

print("Using addition, ", number_1, "+", number_2, "=", sum)
print("Using subtration, ", number_1, "-", number_2, "=", diff)
print("Using multiplication, ", number_1, "x", number_2, "=", product)
print("Using quotient, ", number_1, "divided by", number_2, "=", quotient)
print("the remainder of, ", number_1, "and", number_2, "is", remainder)