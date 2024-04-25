
########################################
# 2-D linear system numerical solution #
########################################

import numpy as np
    # imports the munpy package

A = np.array([[2, 3], [4, 9]])
    # defines the matrix A m x n of coefficients
b = np.array([6, 15])
    # defines the column vector with m entries of constants.
x = np.linalg.solve(A, b)
    # solve the linear system

print(f"The solution of the linear system is {x}")
    # print the result on the screen.



########################################
# 2-D linear system graphical solution #
########################################

import numpy as np
    # imports the munpy package
import matplotlib.pyplot as plt
    # imports matplotlib to plot the graphic
from shapely.geometry import LineString
    # imports LineString to find the intersection point
    
x = np.arange(-20, 20)
    # range of x-values used to calculate y-values for each equation

y1 = 2 - 2/3 * x
    # first equation as an y function

y2 = 15/9 - 4/9 * x
    # second equation as an y function

line1 = LineString(list(zip(x, y1)))
line2 = LineString(list(zip(x, y2)))
    # Define the two lines

intersection = line1.intersection(line2)
    # Find the intersection point

######################
# plotting the graph #
######################

plt.plot(x, y1, label='2x + 3y = 6')
plt.plot(x, y2, label='4x + 9y = 15')
    # plotting the lines represented by the equations y1 and y2
plt.plot(intersection.x, intersection.y, 'o')
    # plot the point of intersection between the two lines
plt.axhline(intersection.y, linestyle='dotted')
plt.axvline(intersection.x, linestyle='dotted')
    # draw a horizontal and vertical dotted line through the point of intersection
plt.annotate("  System Solution", (intersection.x, intersection.y), horizontalalignment='left')
    # insert subtitle in the solution point
plt.legend()
    # adds a legend to the plot to label the lines
plt.tight_layout()
    # automatically adjust the size of the graph 
plt.show()
    # display the plot
