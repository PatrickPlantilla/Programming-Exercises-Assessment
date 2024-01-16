x = int(input("Enter the length of side x: "))
y = int(input("Enter the length of side y: "))
z = int(input("Enter the length of side z: "))

if x + y >= z and y + z >= x and z + x >= y:
    print("Yes, very triangle")
else:
    print("No triangle unforutnately :c")