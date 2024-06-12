################################
# expponential function values #
################################


import numpy as np
    # imports the numpy package
import math as m
    # imports the library math
from tabulate import tabulate
    # imports the tabulate function from the tabulate library

values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # define an array with values

exp_array = []
for i in range(len(values)):
    exp_array.append(m.exp(i))
        # calculates the value of exp(value) and append to exp_array list

exp_array = np.array(exp_array)
        # tranform esp_array list in NumPy array    

table = []
    # create an empty list to store rows of the table

for value, exp_val in zip(values, exp_array):
    # loop through each value and its corresponding exp(value)
    # the zip function takes iterables (in this case, values and exp_array) and combines their elements into tuples
    # each tuple contains one element from each of the iterables, paired together based on their positions
    
    table.append([value, exp_val])
        # append a row to the table list containing the angle and its sine, cosine, and tangent values

headers = ["Value", "exp(value)"]
    # define the headers for the table

print(tabulate(table, headers=headers, floatfmt=".4f"))
    # print the table using the tabulate function, specifying the headers and formatting for floating-point numbers

