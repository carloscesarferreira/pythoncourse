#Leap Years

year = int(input("Entre the year: "))

def leap(year):
    if year%4 == 0 and (year%100 == 0 or year%400 != 0):
        return "TRUE"
    else:
        return "FALSE"

result = leap(year)

if result == "TRUE":
    print(f"TRUE: {year} is a leap year")
else:
    print(f"FALSE: {year} is not a leap year")

print("\n")

print("Printing the leap years between Y1 and Y2, Y1 < Y2")
y1 = int(input("Entre Y1: "))
y2 = int(input("Entre Y2: "))

for i in range(y1,y2+1):
    result = leap(i)
    if result == "TRUE":
        print(f"TRUE: {i} is a leap year")

print("\n")
