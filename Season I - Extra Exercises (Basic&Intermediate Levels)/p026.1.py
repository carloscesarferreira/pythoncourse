n = int(input("Entre a number: "))

# this is the same function of p026

def mindiv(n):
    for d in range(2,n+1):
        if n%d == 0:
            break
    return d

def prime(n):
    if mindiv(n) == n:
        return True
    else:
        return False


if prime(n) == True:
    print(f"The number {n} is prime")
else:
    print(f"The number {n} is not prime")

print("\n")
