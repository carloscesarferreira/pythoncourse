#Write a program that reads an integer amount of USD and shows how to pay this amount in $100, $50, $20, $10, $2 and $1 banknotes

print("Selecting $100, $50, $20, $10, $5, $2 and $1  banknotes to pay a determined value \n")

value = int(input("What is the value to be paid (in US$)?: "))
n100 = value//100
n50 = (value - n100*100)//50
n20 = (value - n100*100 - n50*50)//20
n10 = (value - n100*100 - n50*50 - n20*20)//10
n5  = (value - n100*100 - n50*50 - n20*20 - n10*10)//5
n2  = (value - n100*100 - n50*50 - n20*20 - n10*10 - n5*5)//2
n1  = (value - n100*100 - n50*50 - n20*20 - n10*10 - n5*5 - n2*2)

print("Total amount $",value)
print("Number of $100 banknotes = ",n100)
print("Number of $50 banknotes = ",n50)
print("Number of $20 banknotes = ",n20)
print("Number of $10 banknotes = ",n10)
print("Number of $5 banknotes = ",n5)
print("Number of $2 banknotes = ",n2)
print("Number of $1 banknotes = ",n1)
