print("\n")
n = int(input("Enter a number: "))

quotients = []

def digits(n):
    q = n//10
    i = 0
    while i < n:    
        if q != 0:
            quotients.append(q)
            q = q//10
            i = i + 1
        else:
            quotients.append(0)
            break
    return i + 1
    
print(f"The number {n} has {digits(n)} digits")
print(f"The quotients of successive divisions by 10 are: {quotients}")
