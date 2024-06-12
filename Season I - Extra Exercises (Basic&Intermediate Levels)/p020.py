#Calculating the geometric mean of n numbers

import math as m

print("\n")
n = int(input("Enter the number os elements you want to calculate the geometric average: "))
list = []

def geometric_mean(n):
    for i in range(1,n+1):
        element = float(input(f"Enter the element {i}: "))
        list.append(element)
    def multiply(list):
        result = 1
        for x in list:
            result = result * x
        return result
    mean = round(multiply(list)**(1/n),2)
    return mean

print(f"The geometric mean of the {n} numbers is {geometric_mean(n)}")
print("\n")
