import math
import statistics
import numpy as np

ages = [43, 35, 20, 23, 55, 33, 48, 23, 49, 53, 42, 46, 34, 51, 28, 48, 36, 40, 32, 40, 21, 51, 3, 51, 23, 59, 26, 43, 35, 33, 45, 35, 41, 52, 59, 22, 46, 53, 62, 19, 56, 33, 48, 34, 27, 55, 50, 39, 32, 48, 31, 29, 37, 30, 42, 50, 48, 37, 19, 16, 21, 14, 20, 32, 27, 29, 66, 14, 56, 25, 23, 48, 46, 28, 40, 22, 36, 27, 41, 19, 32, 26, 36, 1, 45, 22, 26, 48, 30, 8, 50, 38, 42, 53, 31, 26, 30, 19, 38, 42]
weights = [0.39, 0.52, 0.3, 0.53, 0.6, 0.54, 0.31, 0.42, 0.65, 0.41, 0.57, 0.59, 0.29, 0.42, 0.42, 0.29, 0.32, 0.4, 0.55, 0.26, 0.42, 0.16, 0.16, 0.38, 0.47, 0.42, 0.36, 0.26, 0.53, 0.39, 0.28, 0.39, 0.34, 0.27, 0.44, 0.2, 0.34, 0.39, 0.25, 0.49, 0.31, 0.16, 0.48, 0.5, 0.41, 0.63, 0.32, 0.31, 0.28, 0.42, 0.17, 0.58, 0.38, 0.27, 0.22, 0.26, 0.41, 0.58, 0.46, 0.09, 0.37, 0.57, 0.52, 0.44, 0.4, 0.26, 0.48, 0.18, 0.43, 0.19, 0.27, 0.08, 0.49, 0.38, 0.24, 0.54, 0.4, 0.53, 0.24, 0.35, 0.58, 0.63, 0.41, 0.27, 0.22, 0.46, 0.29, 0.16, 0.45, 0.45, 0.41, 0.28, 0.29, 0.27, 0.5, 0.25, 0.37, 0.16, 0.28, 0.55]

############
# variance #
############

# coding

list_dif = [] # create an empty list to store the dif values
for age in ages:
        mean_value = sum(ages) / len(ages) # calculates the mean
        dif = (age - mean_value) ** 2 # calculates dif values
        list_dif.append(dif) # append the values to the list

var = 1/(len(ages) - 1) * sum(list_dif) # calculates the variance
var = round(var,2) # round it to two digits

print("Variance: ",var)

# with statistics package

var_statistics = statistics.variance(ages)
    # call the function mean of Statistics package using the list ages as argument
print("Variance: ",var_statistics)
    # print result on the screen.


print("\n")

######################
# standard deviation #
######################

# coding

std = round(var ** 0.5,2)
        # calculates the standard deviation
print("Standard Deviation: ",std)


# with statistics package

std_statistics = round(statistics.stdev(ages),2)
    # call the function mean of Statistics package using the list ages as argument
print("Standard Deviation: ",std_statistics)
    # print result on the screen.


print("\n")

############
# skewness #
############

# coding

def skewness(data):
    # function to calculate skewness
	mean_value = statistics.mean(data)
            # calculates the mean
	std_dev = statistics.stdev(data)
            # calculates the standard deviation
	n = len(data)
            # calculates the length of the dataset
	skew = (sum((x - mean_value) ** 3 for x in data) ) / ((n - 1) * std_dev ** 3)
            # calculates the skewness
	return skew
            # returns the value

data = ages
    # defines the data

# Calculate skewness
result = round(skewness(data),2)
    # use the function to calculate the skewness and round it to two digits
print("Skewness:", result)
    # print the result on the screen


print("\n")

###############
# percentiles #
###############

# coding

intervals = int(input("Enter in how many parts you want to divide your data: "))
        # asks for the number of intervals
result = statistics.quantiles(ages, n=intervals)
        # calculates the intervals
print(f"To divide your dataset into {intervals} intervals, select the following point: {result}")
        # print the result on the screen


print("\n")

##########
# ranges #
##########

# coding

max_value = max(ages)
        # calculates the maximum value
min_value = min(ages)
        # calculates the minimum value
dif_max_min = max_value - min_value
        # calculates the range
print("Range: ", dif_max_min)
        # print the result on the screen

print("\n")

##########################
# plotting the histigram #
##########################

import matplotlib.pyplot as plt
        # imports matplotib library

plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
        # create a histogram with age on the x-axis and frequency on the y-axis, using 20 bins.
        # adjust the number of bins according to your preference
        # you can set the colour of the filling and the edge of the bars

plt.xlabel('Age')
        # add labels to the x-axis
plt.ylabel('Frequency')
        # add labels to the y-axis
plt.title('Age Distribution')
        # add labels to the title

plt.show()
        # show the plot
