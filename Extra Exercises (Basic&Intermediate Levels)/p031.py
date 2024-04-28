import math as m

def standard_deviation(lst):

    x_bar = sum(lst)/len(lst)

    deviations = []

    for number in lst:
        deviations.append( (number - x_bar) ** 2 )

    sd = m.sqrt( ( 1/(len(lst) - 1) ) * sum(deviations) )
    
    return round(sd,2)



test = [2, 8, 13, 17, 21, 22, 24, 31, 47]

print(f"The SD of the list {test} is: {standard_deviation(test)}")
