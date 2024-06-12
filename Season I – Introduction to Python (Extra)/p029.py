import math

n = int(input("Enter a number: "))

def coprime(n):
    coprimes = []
    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

list_coprimes = coprime(n)
print(f"The number {n} has the following {len(list_coprimes)} coprimes: {list_coprimes}")
