##################################
# build a matrix with 'for' loop #
##################################

import random as r
    # imports the module to generate random numbers

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns :"))
    # asks for the number of rows and columns.

matrix = []
    # defines the matrix as an empty list

for i in range(rows):
    # for each row
    row = []
        # defines a new empty list for each row
    for j in range(columns):
            # for each column...
        row.append(r.randint(0,10))
            # ...fills the row with a random number between 0 and 10
    matrix.append(row)
        # fills the matrix with each row created.

print("Matrix built with 'for' loop")
print(matrix)
    # print the result on the screen.

########################### NOTE #########################################
# note that, once we are using random values, each time you run the code #
# you build a different matrix.                                          #
##########################################################################


#############################
# build a matrix with NumPy #
#############################

print("\n")

import numpy as np
    # imports the package NumPy

mtx = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # defines the matrix
print("Matrix built with NumPy")
print(mtx)
    # print the result on the screen.


###################################
# Accessing elements of a matrix  #
###################################

print("\n")

import numpy as np
    # imports the package NumPy

mtx_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    # defines the matrix mtx_1 - 4 rows and 4 columns

#  First element of the first row
print("mtx_1[0][0] =", mtx_1[0][0])  

#  Third element of the second row
print("mtx_1[1][2] =", mtx_1[1][2])  

# Fourth element of the fourth row
print("mtx_1[3][3] =", mtx_1[3][3])



###############################
# sum of matrices with NumPy  #
###############################

print("\n")

import numpy as np
    # imports the package NumPy

mtx1 = np.array([[1, 2], [3, 4]])
    # defines the matrix mtx1
mtx2 = np.array([[5, 6], [7, 8]])
    # defines the matrix mtx2
mtx_sum = mtx1 + mtx2
    # sum mtx1 and mtx2
print("Matrix summation result with NumPy")
print(mtx_sum)
    # print the result on the screen.

#########################################
# multiplication of matrices with NumPy #
#########################################

print("\n")

import numpy as np
    # imports the package NumPy

A = np.array([[1, 2, 3], [4, 5, 6]])
    # defines the matrix A - 2 rows and 3 columns.
B = np.array([[7, 8], [9, 10], [11, 12]])
    # defines the matrix B - 3 rows and 2 columns.
C = A.dot(B)
    # multiply matrices A and B, creating matrix C - 2 rows and 2 columns
print("Matrix multiplication result with NumPy")
print(C)
    # print the result on the screen.


#################################
# transpose a matrix with NumPy #
#################################

print("\n")

import numpy as np
    # imports the package NumPy

mtxA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # defines the matrix A - 3 rows and 3 columns.

mtxAT = mtxA.transpose()
    # transpose the matrix mtxA
print("The transpose of matrix A with NumPy")
print(mtxAT)
    # print the result on the screen.


###########################
# determinant of a matrix #
###########################


print("\n")

import numpy as np
    # imports the package NumPy

mtxA1 = np.array([[1, 3, 2], [5, 4, 6], [9, 8, 7]])
    # defines the matrix A - 3 rows and 3 columns.

determinant = np.linalg.det(mtxA1)
    # calculates the determinant
print("The determinant of the matrix is")
print(determinant)
    # print the result on the screen.



#######################
# inverse of a matrix #
#######################


print("\n")

import numpy as np
    # imports the package NumPy

mtxA2 = np.array([[1, 3, 2], [5, 4, 6], [9, 8, 7]])
    # defines the matrix A - 3 rows and 3 columns.

inverse = np.linalg.inv(mtxA2)
    # calculates the inverse
print("The inverse matrix is")
print(inverse)
    # print the result on the screen.



####################################
# inverse of a matrix with det = 0 #
####################################

# this code will show the error: "numpy.linalg.LinAlgError: Singular matrix"
# this is due to det = 0


print("\n")

import numpy as np
    # imports the package NumPy

mtxA2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # defines the matrix A - 3 rows and 3 columns.

inverse = np.linalg.inv(mtxA2)
    # calculates the inverse
print("The inverse matrix is")
print(inverse)
    # print the result on the screen.
