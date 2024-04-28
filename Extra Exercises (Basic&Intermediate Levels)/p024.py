n = int(input("Enter a number: "))

numbers = []
numbers2 = []

def triangular(n):
    for i in range(1,n+1):
        numbers.append(i)

    def sum_numbers(numbers):
        result = 0
        for k in numbers:
            result = result + k
            numbers2.append(k)
            if result == n:
                break
        return result
    if sum_numbers(numbers) == n:
        return "TRUE"
    else:
        return "FALSE"

if triangular(n) == "TRUE":
    print(f"TRUE: The number {n} is triangular since it is the sum of the {len(numbers2)} first numbers {numbers2}")
else:
    print(f"FALSE: The number {n} is not triangular")
