#Calculating the Sum of Squared Deviations (SQD)

n = int(input("Entre the number of deviations: "))
print("\n")

list = []

def sqd(n):
    for i in range(1,n+1):
        #print("Enter the deviation:",i)
        element = float(input(f"Enter the deviation {i}: "))
        element = element*element
        list.append(element)
    sqd = round(sum(list),2)
    return sqd
    
print("\n")
print("The sum of the squared deviations is: ",sqd(n))
