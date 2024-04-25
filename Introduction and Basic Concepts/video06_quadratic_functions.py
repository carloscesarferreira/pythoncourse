import math as m
import sys
import numpy as np
import matplotlib.pyplot as plt
    # imports the necessary packages. See video # 004 to a more detailed explanation about the main packages.

def concavity(a):
    if a > 0:
        return "upwards concavity"
    else:
        return "downwards concavity"
    # defines a function to analyse the concavity of the function.

def delta(a,b,c):
    value = b*b - 4*a*c
    if value == 0:
        return "The function has two equals real roots"
    elif value > 0:
        return "The function has two different real roots"
    else:
        return "The function has no real roots"
    # defines a function to analyse the delta of the function.

def max_min(a,b,c):
    if a > 0:
        return "Minimun Point (Xv, Yv)"
    else:
        return "Maximun Point (Xv, Yv)"
    # defines a function to analyse the function’s maximum and minimum points.

a = float(input("Enter the coefficient 'a' of the function: "))
    # asks for the coeficient 'a' of the function.

if a == 0:
    sys.exit("The coefficient 'a' can not be 0. Try again")
    # we need a quadratic function (i.e., degree two), so if a = 0, we do not have a quadratic function.
    # leaves the program

else:
    b = float(input("Enter the coefficient 'b' of the function: "))
    c = float(input("Enter the coefficient 'c' of the function: "))
        # asks for the remaining coefficients once 'a' is different from 0.

    dt = b*b - 4*a*c # calculates de delta

    if dt < 0:
        r1 = "N/A"
        r2 = "N/A"
            # if delta < 0 (negative) real roots are 'Not Available' (N/A)
    else:        
        r1 = ( -b - m.sqrt(dt) ) / 2*a
        r1 = round(r1,2)
        r2 = ( -b + m.sqrt(dt) ) / 2*a
        r2 = round(r2,2)
            # if delta >= 0 (non-negative) calculates the roots using Baskara's Formula.

Xv = -b / 2*a
Yv = -( b*b - 4*a*c ) / 4*a
    # calculates the vertex point (maximun or minimun)

print("\n")
print("Function Analysis: \n")
print("************************************************************")
print(f"Concavity................: {concavity(a)}")
print(f"Delta Analysis...........: {delta(a,b,c)}")
print(f"Roots....................: {r1} and {r2}")
print(f"{max_min(a,b,c)}.........: ({Xv},{Yv})")
    # print on the screen the results

# --- plot the graph of the function ---

x = np.arange(-10, 10, 1) # defines the range of the graph. It should be adjusted.
y = a*(x**2) + b*x + c # general form of quadratic function assuming the coefficients 'a', 'b' and 'c'
plt.plot(x, y) # command to plot

# --- graph formatation ---
plt.title("Quadratic Function") # title
plt.xlabel("Values of x") # axis label
plt.ylabel("Values of y") # axis label
plt.axvline(0, color='k') #  adds a vertical line to the plot in 0
plt.axhline(0, color='k') #  adds a horizontal line to the plot in 0

# --- plot the max/min point and insert subtitle ---
plt.scatter(Xv,Yv, c = 'red', s = 50)
plt.annotate("  Maximun/Minimun Point", (Xv, Yv), horizontalalignment='left')

# --- automatically adjust the size of the graph ---
plt.tight_layout()

# --- shows the graph ---
plt.show() 
    


# Examples:

# delta = 0 -- a = 1, b = – 6 e c = 9
# delta < 0 -- a = 1, b = 5 e c = 7
# delta > 0 -- a = 1, b = 3 e c = – 4




    
    
