def cube(side):
    volume = side * side * side
    volume = round(volume,2) # rounds the value of the volume to two digits
    return volume
    # defines a function to calculate the cube volume

s = float(input("Enter the side of the cube: "))
    # asks for the side of the cube

result = cube(s)
    # calculates the volume using the defined function

print(f"The volume of a cube with side {s} is {result}")
    # print the result on the screen
