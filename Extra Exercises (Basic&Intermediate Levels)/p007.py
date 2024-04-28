#Given a grade p, obtained in tha test valued from 0 to 100.
#Implement a function that classifies the grade according to:
#< 0 or > 100 -> Grade not Valid
#≥ 0, < 50 -> Not Enough to Pass
#≥ 50, < 70 -> Enough to Pass
#≥ 70, < 80 -> Good
#≥ 80, < 90 -> Very Good
#≥ 90, ≤ 100 -> Excelent

print("Grade Classification\n")

p = float(input("Input the grade: "))

def classification(p):
    if p < 0 or p > 100:
        return "Grade not Valid"
    else:
        if p >= 0 and p < 50:
            return "Not Enough to Pass"
        else:
            if p >= 50 and p < 70:
                return "Enough to Pass"
            else:
                if p >= 70 and p < 80:
                    return "Good"
                else:
                    if p >= 80 and p < 90:
                        return "Very Good"
                    else:
                        return "Excelent"

status = classification(p)

print("The grade's status is: ",status)
