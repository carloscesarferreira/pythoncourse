import math as m # imports the package math and allows the use of functions such as sqrt and number "pi"

def cylinder(height, radius):
    volume = m.pi * radius * radius * height
    volume = round(volume,2) # rounds the value of the volume to two digits
    return volume
    # defines a function to calculate the cylinder volume

h = float(input("Enter the height of the cylinder: "))
r = float(input("Enter the base radius of the cylinder: "))
    # asks for the height and base radius of the cylinder

result = cylinder(h,r)
    # calculates the volume using the defined function

print(f"The volume of a cylinder with height {h} and base radius {r} is {result}")
    # print the result on the screen
