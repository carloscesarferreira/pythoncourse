#Consider a circle with a radius of r.
#Your job is to implement a function area_circ(r) that calculates the area of a circle with radius r.

import math as m

# Using Functions
print("Calculating the area of a Circle \n")

r = float(input("Input the radius: "))

def area_circ(r):
    a = m.pi*r*r
    return round(a,2)

area = area_circ(r)
print("The area of a circle with radius", r, " is: ", area)

# Without use Functions

#print("Calculating the area of a Circle \n")
#print("Input the radius: ")
#pi = m.pi
#raio = input()
#raio = float(raio)
#area = round(pi*raio*raio,2)
#print("The area of a circle with radius", raio, " is: ", area)
#print("\n")
