# Implement a function radians(degree, minute, second) that convertes an angle in degree, minute and seconds to radians.
# Remember that 360 degrees correspond to 2.pi radians, each degree has 60 minutes and each minute has 60 seconds.

print("Conveting degrees, minutes and seconds to radians\n")
degree = float(input("Type DEGREES: "))
minute = float(input("Type MINUTES: "))
second = float(input("Type SECOND: "))
print("\n")

def radians(degree, minute, second):
    second = second/3600
    minute = minute/60
    degree = degree + minute + second
    r = (degree * 2 * m.pi) / 360
    return r

r = radians(degree, minute, second)

print(degree, "degrees", minute, "minutes", second, "seconds, correspond to ", round(r,2), "radians")
print("\n")
