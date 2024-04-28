#Calculating the total money spent on a travel

n = int(input("Entre the number of stops to fill out during your travel: "))
v = 1.75

list = []
def value(v):
    for i in range(1,n+1):
        diesel = float(input(f"Enter the amount of diesel (in litres) in stop {i}: "))
        list.append(diesel)
    total = round(sum(list)*v,2)
    return total
    
print("\n")
print("The total of money spent in your travel with diesel was USD",value(v))
