# Implement a function dist(x1, y1, x2, y2) that calculates the distance between two points with cordinates (x1,y1) and (x2,y2)

import math as m

print("First point (x1,y1) \n")
x1 = float(input("Type x1: "))
y1 = float(input("Type y1: "))
print("\n")
print("Second point (x2,y2) \n")
x2 = float(input("Type x2: "))
y2 = float(input("Type y2: "))
print("\n")

def dist(x1, y1, x2, y2):
    distance = m.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    return round(distance,2)

d = dist(x1, y1, x2, y2)

print("The distance between A = (",x1,y1,") and B = (",x2,y2,") is: ", d)
print("\n")
print("*****************************")
print("\n")
