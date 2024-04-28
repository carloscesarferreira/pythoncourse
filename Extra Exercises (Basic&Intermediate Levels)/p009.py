#Implement a function P(P0, r, t) that returns the value of an investment P0 at time t, at an interest rate r. Use the formula: P(t) = P[0] * exp (r * t)

import math as m

print("Calculating the value an investment \n")
p0 = float(input("Type the inital amount invested: "))
r = float(input("Type the rate of the investment (if 23%, just type 23): "))
r = r/100
t = float(input("Type the time of the investment (in years): "))

def p_final(p0, r, t):
    p = p0*m.exp(r*t)
    return round(p,2)

p_final = p_final(p0, r, t)
print("The final amount for oyur investment was: ",p_final, "USD")
print("\n")
