places = ["Japan", "U.S.A.", "Poland", "Canada", "Ukraine"]

#to sort alphabetically
a = sorted(places)
print(a)
print("\n")

#reverse alphabetically sorted
b = sorted(places, reverse = True)
print (b)
print("\n")

#reverse sorted
places.reverse()
print(places)
print("\n")

#changed list so that it's sorted reverse alphabetically
places.reverse()
print(places)
print("\n")

#changed list so that it's sorted alphabetically
places.sort()
print(places)
print("\n")

#final print to show that it's sorted differently
print(places)