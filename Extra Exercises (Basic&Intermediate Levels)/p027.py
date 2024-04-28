print("\n")
k = int(input("Enter a number terms of the Leibniz's Formula you want to sum to approximate the value of PI: "))

leibniz_list = []

def leibniz(k):
    for i in range(k):
        leibniz_list.append( ((-1)**i)/(2*i + 1))
    return round(4*sum(leibniz_list),8)

print(f"The approximation of PI using {k} terms of the Leibniz's Formula is {leibniz(k)}")
print("\n")
