##########################
# without using function #
##########################

s = float(input("Enter the side square side: "))
    # ask for the square side value and convert it to a float number.

area = s * s
    # calculates the square area.

area = round(area,2)
    # round the area's value to 2 digits.

print(f"The area of a square with side {s} is {area}")
    # print the result on the screen.


print("\n")

##################
# using function #
##################

def square(side):
    area = side * side
    area = round(area,2)
    return area
    # defines a function that calculates the area, given the parameter side, and rounds the value to two digits.

s = float(input("Enter the square side: "))
    # ask for the square side value and convert it to a float number.

result = square(s)
    # calculates the area using the function square

print(f"The area of a square with side {s} is {result}")
    # print the result on the screen.
