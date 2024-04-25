##########################
# without using function #
##########################


import math as m

r = float(input("Enter the radius of the circle: "))
    # asks for the radius of the circle

area = m.pi*r*r
    # calculates the area of the circle
    
area = round(area,2)
    # rounds the value of the area to two digits

print(f"The area of a circle with radius {r} is {area}")
    # print the result on the screen.


print("\n")

##################
# using function #
##################

import math as m
    # imports the package Math, allowing the use of the number pi.

def circle(radius):
    area = m.pi*r*r
    area = round(area,2)
    return area

    # defines a function that calculates the area, given the radius, and rounds the value to two digits.

r = float(input("Enter the radius of the circle: "))
    # asks for the radius of the circle

result = circle(r)
    # calculates the area using the function circle

print(f"The area of a circle with radius {r} is {result}")
    # print the result on the screen.
