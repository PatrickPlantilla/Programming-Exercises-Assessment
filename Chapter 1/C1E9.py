list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#For loop output
print("List using a for loop:")
for x in list:
    print(x)
print("\n")

#Highest and Lowest numbers
max_value = max(list)
min_value = min(list)
print(f"The highest and lowest value are {max_value} and {min_value} respectively.")
print("\n")

#Ascending order
correct_ordered_list = sorted(list)
print("List in ascending order:", correct_ordered_list)
print("\n")

#Descending order
opposite_list = sorted(list, reverse=True)
print("List in descending order:", opposite_list)
print("\n")

#To add 2 new numbers
list.append(11)
list.append(12)

#To print the new list
print("The new list consists of", list)