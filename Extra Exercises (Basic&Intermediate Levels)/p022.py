#Calculating the factorial of a number n

n = int(input("Enter the number to calculate the factorial: "))

def factorial(n):
    result = n
    for x in range(n,1,-1):
        result = result * (x-1)
    return result

print(f"The factorial of {n} is {factorial(n)}")
print("\n")
