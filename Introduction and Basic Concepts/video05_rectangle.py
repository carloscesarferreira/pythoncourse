##########################
# without using function #
##########################


s1 = float(input("Enter the first rectangle's side: "))
    # ask for the rectangle's first side value and convert it to a float number.
    
s2 = float(input("Enter the second rectangle’s side: "))
    # ask for the rectangle’s second side value and convert it to a float number.
    
area = s1 * s2
    # calculates the rectangle area.
    
area = round(area,2)
    # round the area's value to 2 digits.
    
print(f"The area of a rectangle with sides {s1} and {s2} is {area}")
    # print the result on the screen.

print("\n")

##################
# using function #
##################

def rectangle(side1, side2):
    area = side1 * side2
    area = round(area,2)
    return area
    # defines a function that calculates the area, given the parameters side1 and side2, and rounds the value to two digits.

s1 = float(input("Enter the first rectangle's side: "))
    # ask for the rectangle's first side value and convert it to a float number.

s2 = float(input("Enter the second rectangle's side: "))
    # ask for the rectangle's second side value and convert it to a float number.

result = rectangle(s1,s2)
    # calculates the area using the function rectangle

print(f"The area of a rectangle with sides {s1} and {s2} is {result}")
    # print the result on the screen.
