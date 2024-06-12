#Implement a function hypotenuse(a,b) which, given the dimensions a and b of the two sides of a right-angled triangle, calculates the length of the hypotenuse

import math as m

print("Calculating the lenght of the hypotenuse of a right-angled triangle\n")

a = float(input("Type the first side of the right-angled triangle: "))
b = float(input("Type the second side of the right-angled triangle: "))

def hypotenuse(a,b):
    h = m.sqrt(a*a + b*b)
    return round(h,2)

h = hypotenuse(a,b)
print("The hypoptenuse of a right-angled triangle with sides", a, "and", b, "is", h)
