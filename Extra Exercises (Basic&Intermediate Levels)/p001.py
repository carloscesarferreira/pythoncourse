#Write a programme that asks the user for the kilometres travelled and the number of litres of fuel a car has used, and prints out the consumption in litres spent at 100 kilometres.

print("How many Km did you run? \n")
km = input()
km = float(km)
print("How many liters of fuel did you use? \n")
l = input()
l = float(l)
consumption = round(l/km,2)
print("The fuel consumption was:", consumption*100, "l/100")
print("\n")
