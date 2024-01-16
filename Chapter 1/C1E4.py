number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

if number_1 > number_2 and number_1 > number_3:
    print(number_1, "is greater than", number_2, "and", number_3)
elif number_2 > number_1 and number_2 > number_3:
    print(number_2, "is greater than", number_1, "and", number_3)
else:
    print(number_3, "is greater than", number_1, "and", number_2)

