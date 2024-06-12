########################################
# Calculating sin, cos and tan radians #
########################################


import numpy as np
    # imports the numpy package
from tabulate import tabulate
    # imports the tabulate function from the tabulate library

angles = np.array([0, np.pi/4, np.pi/2, 3*(np.pi)/4, np.pi, 5*(np.pi)/4, 3*(np.pi)/2, 7*(np.pi)/4, 2*np.pi])
    # define an array with the angles in radians

x = np.sin(angles)
y = np.cos(angles)
z = np.tan(angles)
    # calculate the sine, cosine, and tangent values for each angle

table = []
    # create an empty list to store rows of the table

for angle, sin_val, cos_val, tan_val in zip(angles, x, y, z):
    # loop through each angle and its corresponding sine, cosine, and tangent values
    # the zip function takes iterables (in this case, arrays angles, x, y, and z) and combines their elements into tuples
    # each tuple contains one element from each of the iterables, paired together based on their positions
    
    table.append([angle, sin_val, cos_val, tan_val])
        # append a row to the table list containing the angle and its sine, cosine, and tangent values

headers = ["Angle (radians)", "sin(angle)", "cos(angle)", "tan(angle)"]
    # define the headers for the table

print(tabulate(table, headers=headers, floatfmt=".4f"))
    # print the table using the tabulate function, specifying the headers and formatting for floating-point numbers

'''

#################################################
# Calculating arcsin, arccos and arctan degrees #
#################################################

import numpy as np
    # imports the numpy package
from tabulate import tabulate
    # imports the tabulate function from the tabulate library

values = np.array([0, 0.5, 1, -1])
    # define an array with the values for sin, cos and tan

x = np.arcsin(values)
y = np.arccos(values)
z = np.arctan(values)
    # calculate each arc for each value of sin, cos and tan

table = []
    # create an empty list to store rows of the table

for value, arcsin_val, arccos_val, arctan_val in zip(values, x, y, z):
    # loop through each arc and its corresponding value
    # the zip function takes iterables (in this case, arrays values, x, y, and z) and combines their elements into tuples
    # each tuple contains one element from each of the iterables, paired together based on their positions
    
    table.append([value, np.rad2deg(arcsin_val), np.rad2deg(arccos_val), np.rad2deg(arctan_val)])
        # append a row to the table list containing the value and its arcsin, arccos, and arctan values
        # these values are now converted to degree by the NumPy function 'rad2deg'

headers = ["Value", "arcsin(value)(deg)", "arccos(value)(deg)", "arctan(value)(deg)"]
    # define the headers for the table

print(tabulate(table, headers=headers, floatfmt=".4f"))
    # print the table using the tabulate function, specifying the headers and formatting for floating-point numbers
'''
