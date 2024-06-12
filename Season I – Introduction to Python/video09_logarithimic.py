################################
# logarithimic function values #
################################


import numpy as np
    # imports the numpy package
import math as m
    # imports the library math
from tabulate import tabulate
    # imports the tabulate function from the tabulate library

values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # define an array with values

log_array = []
for value in values:
    log_array.append(m.log(value))
        # calculates the value of log(value) and append to exp_array list

log_array = np.array(log_array)
        # tranform esp_array list in NumPy array    

table = []
    # create an empty list to store rows of the table

for value, log_val in zip(values, log_array):
    # loop through each value and its corresponding exp(value)
    # the zip function takes iterables (in this case, values and exp_array) and combines their elements into tuples
    # each tuple contains one element from each of the iterables, paired together based on their positions
    
    table.append([value, log_val])
        # append a row to the table list containing the angle and its sine, cosine, and tangent values

headers = ["Value", "log(value)"]
    # define the headers for the table

print(tabulate(table, headers=headers, floatfmt=".4f"))
    # print the table using the tabulate function, specifying the headers and formatting for floating-point numbers

