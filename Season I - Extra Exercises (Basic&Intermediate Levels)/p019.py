#Calculating the arithmetic mean of n numbers.

n = int(input("Enter the number os elements you want to calculate the average: "))
list = []

def arithmetic_mean(n):
    for i in range(1,n+1):
        element = float(input(f"Entre the element {i}: "))
        list.append(element)
    average = round(sum(list)/n,2)
    return average

print(f"The arithmetic mean of the {n} numbers is {arithmetic_mean(n)}")
print("\n")
