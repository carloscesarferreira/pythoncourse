import math as m
    # imports the package math and allows the use of functions such as sqrt

def triangle(side1,side2,side3):
    p = (side1 + side2 + side3)/2
    area = m.sqrt( p * (p - side1) * (p - side2) * (p - side3) )
        # parts of the Heron's Formula
    area = round(area,2)
        # rounds the value of the area to two digits
    return area
        # defines a function to calculate the triangle area based on Heron's Formula

s1 = float(input("Enter the side 1 of the triangle: "))
s2 = float(input("Enter the side 1 of the triangle: "))
s3 = float(input("Enter the side 1 of the triangle: "))
    # asks for the sides of the triangle

result = triangle(s1,s2,s3)
    # calculates the area using the defined function

print(f"The area of a triangle with sides {s1}, {s2} and {s3} is {result}")
    # print the result on the screen
