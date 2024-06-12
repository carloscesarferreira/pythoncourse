
########################################
# 3-D linear system numerical solution #
########################################

import numpy as np
    # imports the munpy package

A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
    # defines the matrix A m x n of coefficients
b = np.array([1, -2, 0])
    # defines the column vector with m entries of constants.
x = np.linalg.solve(A, b)
    # solve the linear system

print(f"The solution of the linear system is {x}")
    # print the result on the screen.



########################################
# 3-D linear system graphical solution #
########################################

import numpy as np
    # imports the munpy package
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
    # imports the matplotlib modules to plot 3d
    
A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
b = np.array([1, -2, 0])
    # define the coefficients matrix A and the constants vector b

x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)
    # define a grid of points in 3D space

Z1 = (b[0] - A[0, 0] * X - A[0, 1] * Y) / A[0, 2]
Z2 = (b[1] - A[1, 0] * X - A[1, 1] * Y) / A[1, 2]
Z3 = (b[2] - A[2, 0] * X - A[2, 1] * Y) / A[2, 2]
    # compute Z values for each plane defined by the equations Ax = b

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
    # create a 3D plot

ax.plot_surface(X, Y, Z1, alpha=0.5)
ax.plot_surface(X, Y, Z2, alpha=0.5)
ax.plot_surface(X, Y, Z3, alpha=0.5)
    # plot the planes

intersection = np.linalg.solve(A, b)
    # find the intersection point

ax.scatter(intersection[0], intersection[1], intersection[2], color='green', s=80, label='Intersection')
    # plot the intersection point

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
    # set labels and title

ax.legend()
    # add a legend

plt.show()
    # show the plot
