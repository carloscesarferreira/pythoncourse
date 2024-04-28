print("Computing the square root of q by Newton's Method")
q = float(input("Enter q: "))
epsilon = float(input("Enter epsilon: "))

def root(q: float, epsilon: float) -> float:

    iterations = []
    iterations.append(q/2)

    for n in range(0,int(10**q)):
        x = 0.5*(iterations[n] + (q/iterations[n]))
        iterations.append(x)

        if abs(iterations[n+1]-iterations[n]) < epsilon:
            break

    return iterations[n+1]


print(f"The square root of {q} is roughly {root(q,epsilon)}")
