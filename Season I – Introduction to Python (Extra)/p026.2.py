n = int(input("Enter a number: "))

div = []

def divisors(n):

    for i in range(1,n):
        if n%i == 0:
            div.append(i)

    return div

print(divisors(n))
