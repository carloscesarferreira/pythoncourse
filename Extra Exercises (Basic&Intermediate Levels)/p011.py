#Sum and manipulate numbers in a list

import math as m

list = [12, 25, 43, 34, 51, 116]

print("The values of the list")
for number in list:
    print(number)

print("\n")

print("The values of the list, their square and their squared-root")
for number in list:
    print(number,"/",number*number,"/",round(m.sqrt(number),2))

print("\n")

print("The number and partial sum until the total value")
total = 0
for i in list:
    total = total + i
    print(i,"/",total)
    
print("\n")

#Using functions
print("The sum of all numbers of the list")
def listsum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

print("The sum of all elementes in the list is: ",listsum(list))


