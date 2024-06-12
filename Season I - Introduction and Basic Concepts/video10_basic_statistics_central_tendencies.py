import math
import statistics
import numpy as np

ages = [43, 35, 20, 23, 55, 33, 48, 23, 49, 53, 42, 46, 34, 51, 28, 48, 36, 40, 32, 40, 21, 51, 3, 51, 23, 59, 26, 43, 35, 33, 45, 35, 41, 52, 59, 22, 46, 53, 62, 19, 56, 33, 48, 34, 27, 55, 50, 39, 32, 48, 31, 29, 37, 30, 42, 50, 48, 37, 19, 16, 21, 14, 20, 32, 27, 29, 66, 14, 56, 25, 23, 48, 46, 28, 40, 22, 36, 27, 41, 19, 32, 26, 36, 1, 45, 22, 26, 48, 30, 8, 50, 38, 42, 53, 31, 26, 30, 19, 38, 42]
weights = [0.39, 0.52, 0.3, 0.53, 0.6, 0.54, 0.31, 0.42, 0.65, 0.41, 0.57, 0.59, 0.29, 0.42, 0.42, 0.29, 0.32, 0.4, 0.55, 0.26, 0.42, 0.16, 0.16, 0.38, 0.47, 0.42, 0.36, 0.26, 0.53, 0.39, 0.28, 0.39, 0.34, 0.27, 0.44, 0.2, 0.34, 0.39, 0.25, 0.49, 0.31, 0.16, 0.48, 0.5, 0.41, 0.63, 0.32, 0.31, 0.28, 0.42, 0.17, 0.58, 0.38, 0.27, 0.22, 0.26, 0.41, 0.58, 0.46, 0.09, 0.37, 0.57, 0.52, 0.44, 0.4, 0.26, 0.48, 0.18, 0.43, 0.19, 0.27, 0.08, 0.49, 0.38, 0.24, 0.54, 0.4, 0.53, 0.24, 0.35, 0.58, 0.63, 0.41, 0.27, 0.22, 0.46, 0.29, 0.16, 0.45, 0.45, 0.41, 0.28, 0.29, 0.27, 0.5, 0.25, 0.37, 0.16, 0.28, 0.55]


########
# mean #
########

# coding

mean = sum(ages)/len(ages)
    # sum all elements in the list ages and divide by its length
print(f"The mean of ages is: {mean}")
    # print result on the screen.

# with statistics package

mean_statistics = statistics.mean(ages)
    # call the function mean of Statistics package using the list ages as argument
print(f"The mean of ages is: {mean_statistics}")
    # print result on the screen.

print("\n")

#################
# weighted mean #
#################

# coding

ages_weights = []
    # creates an empty list
for i in range(len(ages)):
    ages_weights.append(ages[i] * weights[i])
        # add the multiplication ages * weights for all elements to the list.
weighted_mean = sum(ages_weights) / sum(weights)
    # calculates the Weighted Mean
weighted_mean = round(weighted_mean,2)
    # rounds the Weighted Mean
print(f"The weighted mean of ages/weights is: {weighted_mean}")
    # print result on the screen.

# unisng NumPy

x = np.array(ages)
    # creates an array from list ages
y = np.array(weights)
    # creates an array from list weights
weighted_mean_np = np.average(x, weights=y)
    # call the function average of NumPy package using two arrays as arguments
weighted_mean_np = round(weighted_mean_np,2)
    # rounds the Weighted Mean
print(f"The weighted mean of ages/weights is: {weighted_mean_np}")
    # print result on the screen.

print("\n")

##################
# geometric mean #
##################

# coding

product = 1
    # initializes a variable for product
for i in range(len(ages)):
    product = product * ages[i]
        # calculates the product of all elements in ages
g_mean = (product) ** (1 / len(ages))
    # calculates the geometric mean
g_mean = round(g_mean,2)
    # rounds the geometric mean
print(f"The geometric mean of ages is: {g_mean}")
    # print result on the screen.

# using statistics package

g_mean_statistics = statistics.geometric_mean(ages)
    # call the function geometric_mean of Statistics package using the list ages as argument
g_mean_statistics = round(g_mean_statistics,2)
    # rounds the geometric mean
print(f"The geometric mean of ages is: {g_mean_statistics}")
    # print result on the screen.

print("\n")

#################
# harmonic mean #
#################

# coding

h_values = []
    # creates an empty list
for i in range(len(ages)):
    h_values.append(1 / ages[i])
        # add the division 1 / ages for all elements of ages.
h_mean = len(ages) / sum(h_values)
    # calculates the harmonic mean
h_mean = round(h_mean,2)
    # rounds the harmonic mean
print(f"The harmonic mean of ages is: {h_mean}")
    # print result on the screen.

# using statistics package

h_mean_statistics = statistics.harmonic_mean(ages)
    # call the function harmonic_mean of Statistics package using the list ages as argument
h_mean_statistics = round(h_mean_statistics,2)
    # rounds the harmonic mean
print(f"The harmonic mean of ages is: {h_mean_statistics}")
    # print result on the screen.

print("\n")

##########
# median #
##########

# coding

elements = len(ages)
    # counts the number of elements in ages
ages = sorted(ages)
    # sort ages ascending
if elements % 2:
    # if the remainder of dividing elements by 2 is non-zero, which means if the number of  elements is odd...
    median = ages[round( (elements - 1)/2 )]
        # takes the central element
else:
    # otherwise, if the number of elements is even...
    median = ( ages[ (round(0.5 * elements) - 1) ] + ages[ (round(0.5 * elements)) ] ) / 2
        # sum the two central elements and divide by two
median = round(median,2)
    # rounds the median
print(f"The median of ages is: {median}")
    # print result on the screen.

# using statistics package

median_statistics = statistics.median(ages)
    # call the function median of Statistics package using the list ages as argument
median_statistics = round(median_statistics,2)
    # rounds the median
print(f"The median of ages is: {median_statistics}")
    # print result on the screen.

print("\n")

########
# mode #
########

# coding

frequency = {}
for value in ages:
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1
    # Count occurrences of each value

modes = []
max_frequency = max(frequency.values())
for value, freq in frequency.items():
    if freq == max_frequency:
        modes.append(value)
    # Find the values with the highest frequency (modes)

print(f"The mode of ages is: {modes}")
    # print result on the screen.

# using statistics package

mode_statistics = statistics.multimode(ages)
    # call the function multimode of Statistics package using the list ages as argument
print(f"The mode of ages is: {mode_statistics}")
    # print result on the screen.
