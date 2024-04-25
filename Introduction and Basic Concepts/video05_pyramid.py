def pyramid(height, length, width):
    volume = (1/3)*height*length*width
    volume = round(volume,2)
    return volume

    # defines a function that calculates the volume, given the radius, and rounds the value to two digits.

h = float(input("Enter the height of the pyramid: "))
    # asks for the height of the pyramid

l = float(input("Enter the base length of the pyramid: "))
    # asks for base length

w = float(input("Enter the base width of the pyramid: "))
    # asks for the base width

result = pyramid(h,l,w)
    # calculates the area using the function circle

print(f"The volume of a pyramid with height {h}, base length {l} and base width {w} is {result}")
    # print the result on the screen.
