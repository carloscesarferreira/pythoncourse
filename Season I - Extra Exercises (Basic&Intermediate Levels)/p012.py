#Implement a function square(n) which, for the first n positive integers, prints on each line the number and its square, separated by a space

print("Calculating the squares of the first n integers numbers\n")
n = int(input("Entre the number of integers: "))

def square(n):
    for i in range(1, n + 1):
        square = i ** 2
        print(f"{i} {square}")

square(n)
