n = int(input("Enter a number: "))

div = []

def perfect(n):
    for i in range(1,n):
        if n%i == 0:
            div.append(i)

    if sum(div) == n:
        return True
    else:
        return False


if perfect(n) == True:
    print(f"{n} is perfect")
else:
    print(f"{n} is not perfect")


# examples of perfect numbers: 6, 28, 496 and 8128
