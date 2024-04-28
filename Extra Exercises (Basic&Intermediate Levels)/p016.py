#Area of a triangle based in Heron formule

import math as m

print("Calculating the area of a triangle with sides a, b and c")

a = float(input("Entre the side 'a': "))
b = float(input("Entre the side 'b': "))
c = float(input("Entre the side 'c': "))
          
def triangle_area(a,b,c):
    s = (a + b + c)/2
    area = m.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area,2)

print(f"The area of the triangle with side {a}, {b} and {c} is ",triangle_area(a,b,c))
    
