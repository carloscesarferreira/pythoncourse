#Write a function celsius(F) that converts a temperature in F (Fahrenheit) to ºC (Celsius)

f = float(input("Type the temperature F to convert to ºC: "))

def celsius(f):
    c = (5/9)*(f-32)
    return round(c,2)

c = celsius(f)

print(f, "F is equal to ", c, "ºC")
print("\n")
print("*****************************")
print("\n")
