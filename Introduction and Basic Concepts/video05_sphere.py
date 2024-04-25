import math as m # imports the package math and allows the use of functions such as sqrt and number “pi”

def sphere(radius):
    volume = (4/3)* m.pi * radius * radius * radius
    volume = round(volume,2) # rounds the value of the volume to two digits
    return volume
    # defines a function to calculate the sphere volume

r = float(input("Enter the base radius of the sphere: "))
    # asks for the radius of the sphere

result = sphere(r)
    # calculates the volume using the defined function

print(f"The volume of a sphere with radius {r} is {result}")
    # print the result on the screen
