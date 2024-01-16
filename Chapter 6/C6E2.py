list = [20, 23, 82, 40, 32, 15, 67, 52]

indices = [index for index, value in enumerate(list) if value % 2 == 0]
print("The Indices of even numbers are:", indices)

list.sort()
print("Sorted order:", list)

sliced_index_3 = list[3:]
print("Elements from index 3 to the end are:", sliced_index_3)

sliced_from_0_to_4 = list[0:5]
print("Elements from index 0 to index 4:", sliced_from_0_to_4)

negative_slice = list[-5:-2]
print("Negative slices", negative_slice)