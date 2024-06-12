#Calculating the final capita of a deposit with compound interest capitalised monthly at an annual rate of r

print("Calculating the final value of a deposit\n")
ci = float(input("Enter the inicial deposit in USD: "))
r = float(input("Enter the annual rate (e.g., if 3% type just 3): "))/100
n = int(input("Enter the number of months (only integers numbers) of the ivestment: "))

def final_deposit(n):
    for i in range(1, n + 1):
        cf = ci * (1 + r/12) ** i
        cf = round(cf,2)
        print(f"Month {i} - Final Capital: {cf}")

final_deposit(n)
