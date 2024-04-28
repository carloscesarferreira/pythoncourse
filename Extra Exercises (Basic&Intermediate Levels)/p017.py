#Checking if three numbers a, b and c define a triangle with sides a, b and c

print("Checking if three numbers a, b and c define a triangle with sides a, b and c")

a = float(input("Entre the number 'a': "))
b = float(input("Entre the number 'b': "))
c = float(input("Entre the number 'c': "))

def triangle(a,b,c):
    if (a < b + c) and (a > abs(b - c)):
        first_check = "TRUE"
    else:
        first_check = "FALSE"

    if (b < a + c) and (b > abs(a - c)):
        second_check = "TRUE"
    else:
        second_check = "FALSE"

    if (c < a + b) and (c > abs(a - b)):
        third_check = "TRUE"
    else:
        third_check = "FALSE"

    if first_check == "TRUE" and second_check == "TRUE" and third_check == "TRUE":
        print(f"The sides {a}, {b} and {c} define a triangle")
    else:
        print(f"The sides {a}, {b} and {c} do not define a triangle")

triangle(a,b,c)
    
