n = int(input("Entre a number: "))

def mindiv(n):
    for d in range(2,n+1):
        if n%d == 0:
            break
    return d

print(f"The smallest proper divisor of {n} is {mindiv(n)}")
