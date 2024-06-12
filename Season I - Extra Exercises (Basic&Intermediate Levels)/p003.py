#Exercise 1
#Implement the function summation(a, b), which returns the sum of a and b.

print("Sum of two numbers a and b \n")

a = float(input("Type the number 'a': "))
b = float(input("Type the number 'b': "))

def summation(a,b):
    s = a + b
    return s

s = summation(a,b)

print("The sum of ", a, "and", b, "is equal to: ", s)

          
