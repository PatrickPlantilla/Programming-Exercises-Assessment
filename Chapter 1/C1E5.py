var = 0

while True:
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input == 'yes':
        var += 1
    elif user_input == 'no':
        break
    else:
        print("Wrong input. Please enter 'yes' to continue or 'no' to exit.")

if var > 1: #final print when the loop breaks
    print(f"The loop was executed {var} times.")
elif var == 1:
    print("The loop has executed once.")
else:
    print("You just ended it immediately?")